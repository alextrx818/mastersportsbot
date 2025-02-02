import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging
from typing import Set, Dict, List
import os
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BetsAPIDocCrawler:
    """Simple crawler to gather all content from BetsAPI docs"""
    
    def __init__(self):
        self.base_url = "https://betsapi.com"
        self.docs_url = "https://betsapi.com/docs"
        self.visited_urls: Set[str] = set()
        self.content_map: Dict[str, str] = {}
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        
        # Known documentation sections
        self.known_sections = [
            '/docs',
            '/docs/events',
            '/docs/events/inplay',
            '/docs/events/upcoming',
            '/docs/events/ended',
            '/docs/events/league',
            '/docs/odds',
            '/docs/odds/inplay',
            '/docs/odds/prematch',
            '/docs/results',
            '/docs/results/events',
            '/docs/results/league',
            '/docs/sports',
            '/docs/sports/list',
            '/docs/sports/league',
            '/docs/sports/team'
        ]
    
    def fetch_page(self, url: str) -> str:
        """Fetch a page's content"""
        try:
            logger.info(f"Fetching: {url}")
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return ""
    
    def extract_text_content(self, html_content: str) -> str:
        """Extract readable text from HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(['script', 'style']):
            script.decompose()
        
        # Get text content
        text = soup.get_text(separator='\n', strip=True)
        
        # Clean up excessive newlines
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return '\n'.join(lines)
    
    def extract_sections(self, html_content: str) -> Dict[str, str]:
        """Extract individual sections from the documentation"""
        soup = BeautifulSoup(html_content, 'html.parser')
        sections = {}
        
        # Find all headings that might start a section
        headings = soup.find_all(['h1', 'h2', 'h3'])
        
        for i, heading in enumerate(headings):
            section_title = heading.get_text(strip=True)
            section_content = []
            
            # Get all content until the next heading
            current = heading.next_sibling
            while current and (i == len(headings) - 1 or current != headings[i + 1]):
                if isinstance(current, str):
                    text = current.strip()
                    if text:
                        section_content.append(text)
                else:
                    text = current.get_text(strip=True)
                    if text:
                        section_content.append(text)
                        
                    # If it's a table, also preserve its structure
                    if current.name == 'table':
                        rows = []
                        for row in current.find_all('tr'):
                            cols = [col.get_text(strip=True) for col in row.find_all(['th', 'td'])]
                            rows.append(' | '.join(cols))
                        section_content.append('\n'.join(rows))
                        
                    # If it's a code block, preserve it
                    if current.name == 'code' or current.name == 'pre':
                        section_content.append('```\n' + current.get_text(strip=True) + '\n```')
                        
                    # If it's a list, preserve its structure
                    if current.name in ['ul', 'ol']:
                        items = []
                        for item in current.find_all('li'):
                            items.append('- ' + item.get_text(strip=True))
                        section_content.append('\n'.join(items))
                
                current = current.next_sibling
            
            sections[section_title] = '\n\n'.join(section_content)
        
        return sections
    
    def extract_api_endpoints(self, html_content: str) -> List[Dict]:
        """Extract API endpoint details"""
        soup = BeautifulSoup(html_content, 'html.parser')
        endpoints = []
        
        # Look for endpoint sections
        for section in soup.find_all(['div', 'section']):
            endpoint_info = {
                'name': '',
                'url': '',
                'method': 'GET',
                'description': '',
                'parameters': [],
                'response_example': '',
                'curl_example': ''
            }
            
            # Find heading
            heading = section.find(['h1', 'h2', 'h3', 'h4'])
            if heading:
                endpoint_info['name'] = heading.get_text(strip=True)
            
            # Find URL examples
            code_blocks = section.find_all('code')
            for block in code_blocks:
                text = block.get_text(strip=True)
                if 'api.b365api.com' in text:
                    endpoint_info['url'] = text
                elif 'curl' in text.lower():
                    endpoint_info['curl_example'] = text
                else:
                    endpoint_info['response_example'] = text
            
            # Find parameters table
            tables = section.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                for row in rows[1:]:  # Skip header
                    cols = row.find_all(['td', 'th'])
                    if len(cols) >= 2:
                        param = {
                            'name': cols[0].get_text(strip=True),
                            'description': cols[1].get_text(strip=True),
                            'required': 'required' in cols[1].get_text(strip=True).lower(),
                            'type': 'string'
                        }
                        # Try to infer type
                        desc = cols[1].get_text(strip=True).lower()
                        if any(t in desc for t in ['integer', 'number']):
                            param['type'] = 'integer'
                        elif any(t in desc for t in ['boolean', 'true/false']):
                            param['type'] = 'boolean'
                        endpoint_info['parameters'].append(param)
            
            if endpoint_info['url'] or endpoint_info['curl_example']:
                endpoints.append(endpoint_info)
        
        return endpoints
    
    def crawl(self):
        """Crawl the documentation"""
        # Fetch main documentation page
        content = self.fetch_page(self.docs_url)
        if not content:
            return
        
        # Extract sections
        sections = self.extract_sections(content)
        
        # Extract API endpoints
        endpoints = self.extract_api_endpoints(content)
        
        # Save each section
        for title, content in sections.items():
            self.content_map[title] = content
        
        # Save endpoints as a separate file
        if endpoints:
            self.content_map['API Endpoints'] = json.dumps(endpoints, indent=2)
        
        # Save the full page
        self.content_map['Full Documentation'] = self.extract_text_content(content)
    
    def save_content(self):
        """Save all gathered content to files"""
        output_dir = os.path.join(os.path.dirname(__file__), "betsapi_docs_content")
        os.makedirs(output_dir, exist_ok=True)
        
        # Save individual page contents
        for url, content in self.content_map.items():
            # Create a filename from the URL
            filename = url.lower().replace(' ', '_').replace('/', '_').replace('\\', '_')
            filename = ''.join(c for c in filename if c.isalnum() or c in '_-')
            filename += '.txt'
            
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"URL: {url}\n")
                f.write("=" * 80 + "\n\n")
                f.write(content)
        
        # Create an index file
        index_path = os.path.join(output_dir, "index.txt")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write("BetsAPI Documentation Index\n")
            f.write("=" * 80 + "\n\n")
            for url in sorted(self.content_map.keys()):
                f.write(f"- {url}\n")
        
        logger.info(f"Content saved to: {output_dir}")
        logger.info(f"Total pages crawled: {len(self.content_map)}")

def main():
    crawler = BetsAPIDocCrawler()
    logger.info("Starting BetsAPI documentation crawl...")
    crawler.crawl()
    crawler.save_content()

if __name__ == "__main__":
    main()
