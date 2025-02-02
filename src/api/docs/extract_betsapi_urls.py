import requests
from bs4 import BeautifulSoup
import logging
import json
import os
import time
from typing import Dict, List
from urllib.parse import urljoin

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BetsAPIDocExtractor:
    def __init__(self, output_dir: str = "betsapi_api_docs"):
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }
        self.session.headers.update(self.headers)
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def extract_api_docs(self, url: str):
        """Extract API documentation"""
        logger.info(f"Fetching API documentation from: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            # Get all the chunks from the documentation
            chunks = self.get_doc_chunks(url)
            
            endpoints = []
            # Process each chunk
            for chunk in chunks:
                if 'headers' in chunk and chunk['headers']:
                    endpoint = self.process_chunk(chunk)
                    if endpoint:
                        endpoints.append(endpoint)
            
            # Save the extracted data
            self.save_endpoints(endpoints)
            
            logger.info(f"Successfully extracted {len(endpoints)} endpoints")
            
        except Exception as e:
            logger.error(f"Error extracting API docs: {str(e)}")
    
    def get_doc_chunks(self, url: str) -> List[Dict]:
        """Get all documentation chunks"""
        chunks = []
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            # Get the list of chunks from the initial response
            content_response = response.text
            
            # Parse the chunks from the content
            lines = content_response.split('\n')
            current_chunk = {'headers': [], 'text': ''}
            
            for line in lines:
                if line.startswith('- [Position:'):
                    if current_chunk['headers'] or current_chunk['text']:
                        chunks.append(current_chunk.copy())
                    current_chunk = {'headers': [], 'text': ''}
                    
                    # Extract position and content
                    parts = line.split(']', 1)
                    if len(parts) > 1:
                        content = parts[1].strip()
                        headers = content.split('/')
                        current_chunk['headers'] = [h.strip() for h in headers if h.strip()]
            
            # Add the last chunk
            if current_chunk['headers'] or current_chunk['text']:
                chunks.append(current_chunk)
            
            # Now get the actual content for each chunk
            for i, chunk in enumerate(chunks):
                chunk_content = self.get_chunk_content(url, i)
                if chunk_content:
                    chunk['text'] = chunk_content
            
            return chunks
            
        except Exception as e:
            logger.error(f"Error getting doc chunks: {str(e)}")
            return []
    
    def get_chunk_content(self, url: str, position: int) -> str:
        """Get content for a specific chunk"""
        try:
            response = requests.get(f"{url}#position={position}")
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.error(f"Error getting chunk content: {str(e)}")
            return ""
    
    def process_chunk(self, chunk: Dict) -> Dict:
        """Process a documentation chunk into an endpoint definition"""
        if not chunk['headers']:
            return None
            
        # Only process chunks that look like API endpoints
        if not any(api in chunk['headers'][0].lower() for api in ['events api', 'bet365 api', 'bwin api']):
            return None
            
        endpoint = {
            'name': ' - '.join(chunk['headers']),
            'category': chunk['headers'][0] if chunk['headers'] else '',
            'method': 'GET',  # Default to GET as most endpoints are GET
            'url': '',
            'description': '',
            'parameters': [],
            'response_example': '',
            'curl_example': ''
        }
        
        text = chunk['text']
        
        # Extract URL
        if 'HTTP Request' in text:
            lines = text.split('\n')
            for line in lines:
                if line.startswith('GET ') or line.startswith('POST '):
                    endpoint['method'] = line.split(' ')[0]
                    endpoint['url'] = line.split(' ')[1]
                    break
        
        # Extract curl example
        if '```' in text:
            curl_start = text.find('curl')
            if curl_start != -1:
                curl_end = text.find('```', curl_start)
                if curl_end != -1:
                    endpoint['curl_example'] = text[curl_start:curl_end].strip()
        
        # Extract parameters
        if 'Parameters' in text:
            param_section = text[text.find('Parameters'):]
            param_end = param_section.find('###')
            if param_end != -1:
                param_section = param_section[:param_end]
            
            # Parse parameters
            lines = param_section.split('\n')
            for line in lines:
                if '|' in line and not line.startswith('|--'):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 3:
                        param = {
                            'name': parts[1],
                            'description': parts[2],
                            'required': 'required' in parts[2].lower(),
                            'type': 'string'
                        }
                        endpoint['parameters'].append(param)
        
        # Extract response example
        if 'Response' in text:
            resp_section = text[text.find('Response'):]
            if '```' in resp_section:
                resp_start = resp_section.find('```') + 3
                resp_end = resp_section.find('```', resp_start)
                if resp_end != -1:
                    endpoint['response_example'] = resp_section[resp_start:resp_end].strip()
        
        return endpoint
    
    def save_endpoints(self, endpoints: List[Dict]):
        """Save extracted endpoints"""
        # Save as JSON
        json_path = os.path.join(self.output_dir, "api_endpoints.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(endpoints, f, indent=2, ensure_ascii=False)
        
        # Save as Markdown for easy reading
        md_path = os.path.join(self.output_dir, "api_endpoints.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write("# BetsAPI Endpoints\n\n")
            
            # Group by category
            categories = {}
            for endpoint in endpoints:
                category = endpoint['category']
                if category not in categories:
                    categories[category] = []
                categories[category].append(endpoint)
            
            for category, category_endpoints in categories.items():
                f.write(f"## {category}\n\n")
                
                for endpoint in category_endpoints:
                    f.write(f"### {endpoint['name']}\n\n")
                    
                    f.write(f"**Method:** {endpoint['method']}\n")
                    f.write(f"**URL:** `{endpoint['url']}`\n\n")
                    
                    if endpoint['parameters']:
                        f.write("#### Parameters\n\n")
                        f.write("| Name | Description | Required | Type |\n")
                        f.write("|------|-------------|----------|------|\n")
                        for param in endpoint['parameters']:
                            f.write(f"| {param['name']} | {param['description']} | {'Yes' if param['required'] else 'No'} | {param['type']} |\n")
                        f.write("\n")
                    
                    if endpoint['curl_example']:
                        f.write("#### Example Request\n\n")
                        f.write("```bash\n")
                        f.write(endpoint['curl_example'])
                        f.write("\n```\n\n")
                    
                    if endpoint['response_example']:
                        f.write("#### Example Response\n\n")
                        f.write("```json\n")
                        f.write(endpoint['response_example'])
                        f.write("\n```\n\n")
                    
                    f.write("---\n\n")
        
        logger.info(f"Saved endpoints to {json_path} and {md_path}")

def main():
    url = "https://betsapi.com/api-doc/index.html"
    extractor = BetsAPIDocExtractor()
    extractor.extract_api_docs(url)

if __name__ == "__main__":
    main()
