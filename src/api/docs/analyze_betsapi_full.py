import requests
from bs4 import BeautifulSoup
import yaml
import json
import re
from typing import Dict, List, Any, Set
from urllib.parse import urljoin
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BetsAPIFullAnalyzer:
    """Comprehensive analyzer for BetsAPI documentation"""
    
    BASE_URL = "https://betsapi.com/docs"
    API_ENDPOINT = "https://api.b365api.com"
    
    def __init__(self):
        self.session = requests.Session()
        self.visited_urls: Set[str] = set()
        self.endpoints: Dict[str, Dict] = {}
        self.json_schemas: Dict[str, Dict] = {}
        self.sport_ids: Dict[int, str] = {
            1: "Soccer",
            18: "Basketball",
            91: "Volleyball",
            78: "Handball",
            16: "Baseball",
            17: "Ice Hockey",
            13: "Tennis",
            14: "Snooker",
            12: "American Football",
            3: "Cricket"
        }
        # Add API token
        self.token = "180846-0nb22aL4DeG73U"
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }
        
    def fetch_page(self, url: str) -> str:
        """Fetch a documentation page"""
        try:
            # Add token to URL if it's an API endpoint
            if self.API_ENDPOINT in url:
                if "?" in url:
                    url += f"&token={self.token}"
                else:
                    url += f"?token={self.token}"
            
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return ""

    def extract_json_examples(self, html_content: str) -> List[Dict]:
        """Extract JSON examples from documentation"""
        json_examples = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all code blocks
        code_blocks = soup.find_all('code')
        for block in code_blocks:
            try:
                # Try to parse as JSON
                if '{' in block.text and '}' in block.text:
                    json_data = json.loads(block.text)
                    json_examples.append(json_data)
            except json.JSONDecodeError:
                continue
        
        return json_examples

    def analyze_json_structure(self, json_data: Dict) -> Dict:
        """Recursively analyze JSON structure to create schema"""
        if isinstance(json_data, dict):
            properties = {}
            for key, value in json_data.items():
                if isinstance(value, dict):
                    properties[key] = self.analyze_json_structure(value)
                elif isinstance(value, list):
                    if value:
                        # Analyze first item as example
                        properties[key] = {
                            "type": "array",
                            "items": self.analyze_json_structure(value[0])
                        }
                    else:
                        properties[key] = {
                            "type": "array",
                            "items": {"type": "object"}
                        }
                else:
                    properties[key] = {
                        "type": type(value).__name__,
                        "example": value
                    }
            return {
                "type": "object",
                "properties": properties
            }
        else:
            return {"type": type(json_data).__name__}

    def extract_endpoints(self, html_content: str) -> List[Dict]:
        """Extract API endpoints from documentation"""
        endpoints = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find endpoint descriptions in various formats
        for heading in soup.find_all(['h1', 'h2', 'h3', 'h4']):
            endpoint_info = {
                "path": "",
                "method": "GET",  # Default to GET
                "description": heading.text.strip(),
                "parameters": []
            }
            
            # Look for endpoint URL in various formats
            url_patterns = [
                r'https?://[^\s<>"\']+',  # Standard URL
                r'/v\d+/[^\s<>"\']+',     # Path format
                r'api\.b365api\.com[^\s<>"\']+',  # Domain specific
            ]
            
            # Search in the heading and next siblings
            search_elements = [heading] + list(heading.find_next_siblings())[:3]
            for element in search_elements:
                for pattern in url_patterns:
                    urls = re.findall(pattern, str(element))
                    for url in urls:
                        if '/v1/' in url:  # Only capture API endpoints
                            endpoint_info["path"] = url.split('api.b365api.com')[-1].split('?')[0]
                            break
                    if endpoint_info["path"]:
                        break
                if endpoint_info["path"]:
                    break
            
            # Look for parameters in tables or lists
            param_table = None
            for sibling in heading.find_next_siblings():
                if sibling.name == 'table':
                    param_table = sibling
                    break
                elif sibling.name in ['h1', 'h2', 'h3', 'h4']:
                    break
            
            if param_table:
                rows = param_table.find_all('tr')
                for row in rows[1:]:  # Skip header row
                    cols = row.find_all('td')
                    if len(cols) >= 2:
                        param_info = {
                            "name": cols[0].text.strip(),
                            "description": cols[1].text.strip(),
                            "required": "required" in cols[1].text.lower() or "mandatory" in cols[1].text.lower(),
                            "type": "string"  # Default type
                        }
                        # Try to infer parameter type
                        desc = cols[1].text.lower()
                        if any(num_type in desc for num_type in ['integer', 'number', 'digit']):
                            param_info["type"] = "integer"
                        elif any(bool_type in desc for bool_type in ['boolean', 'true/false', 'true or false']):
                            param_info["type"] = "boolean"
                        endpoint_info["parameters"].append(param_info)
            
            if endpoint_info["path"]:
                endpoints.append(endpoint_info)
        
        return endpoints

    def crawl_documentation(self):
        """Crawl through all documentation pages"""
        def crawl_page(url: str, depth=0):
            if url in self.visited_urls or depth > 5:  # Prevent infinite recursion
                return
            
            logger.info(f"Analyzing page: {url}")
            self.visited_urls.add(url)
            
            content = self.fetch_page(url)
            if not content:
                return
            
            # Extract information from current page
            json_examples = self.extract_json_examples(content)
            for example in json_examples:
                schema = self.analyze_json_structure(example)
                self.json_schemas[url] = schema
            
            endpoints = self.extract_endpoints(content)
            for endpoint in endpoints:
                if endpoint["path"]:
                    self.endpoints[endpoint["path"]] = endpoint
            
            # Find links to other documentation pages
            soup = BeautifulSoup(content, 'html.parser')
            
            # First, find navigation links (these are usually the most important)
            nav_links = set()
            for nav in soup.find_all(['nav', 'div'], class_=['nav', 'navigation', 'sidebar']):
                for link in nav.find_all('a', href=True):
                    nav_links.add(link['href'])
            
            # Then find all links in the main content
            content_div = soup.find(['div', 'main'], class_=['content', 'main', 'documentation'])
            if content_div:
                for link in content_div.find_all('a', href=True):
                    href = link['href']
                    # Skip API endpoint examples
                    if 'api.b365api.com' in href or 'token=' in href:
                        continue
                    # Skip known protected pages
                    if 'pro/' in href or 'premium/' in href:
                        continue
                    if href.startswith(('/docs/', 'docs/', '/v1/', 'v1/')):
                        full_url = urljoin(self.BASE_URL, href)
                        crawl_page(full_url, depth + 1)
            
            # Follow navigation links last (they're usually more important)
            for href in nav_links:
                if href.startswith(('/docs/', 'docs/', '/v1/', 'v1/')):
                    full_url = urljoin(self.BASE_URL, href)
                    crawl_page(full_url, depth + 1)
        
        # Start crawling from main page
        crawl_page(self.BASE_URL)
        
        # Also try known documentation sections
        known_sections = [
            '/docs/events/',
            '/docs/results/',
            '/docs/odds/',
            '/docs/soccer/',
            '/docs/basketball/',
            '/docs/volleyball/',
            '/docs/tennis/',
            '/docs/glossary/'
        ]
        
        for section in known_sections:
            full_url = urljoin(self.BASE_URL, section)
            if full_url not in self.visited_urls:
                crawl_page(full_url)

    def analyze_api_endpoints(self):
        """Directly analyze API endpoints with example data"""
        # Analyze live events endpoint
        for sport_id in self.sport_ids.keys():
            url = f"{self.API_ENDPOINT}/v1/events/inplay?sport_id={sport_id}&token={self.token}"
            logger.info(f"Analyzing live events for sport {sport_id}")
            content = self.fetch_page(url)
            if content:
                try:
                    json_data = json.loads(content)
                    schema = self.analyze_json_structure(json_data)
                    self.json_schemas[f"/v1/events/inplay?sport_id={sport_id}"] = schema
                except json.JSONDecodeError:
                    continue

        # Analyze upcoming events endpoint
        for sport_id in self.sport_ids.keys():
            url = f"{self.API_ENDPOINT}/v1/events/upcoming?sport_id={sport_id}&token={self.token}"
            logger.info(f"Analyzing upcoming events for sport {sport_id}")
            content = self.fetch_page(url)
            if content:
                try:
                    json_data = json.loads(content)
                    schema = self.analyze_json_structure(json_data)
                    self.json_schemas[f"/v1/events/upcoming?sport_id={sport_id}"] = schema
                except json.JSONDecodeError:
                    continue

    def generate_openapi_spec(self) -> Dict:
        """Generate OpenAPI specification from analyzed data"""
        spec = {
            "openapi": "3.0.0",
            "info": {
                "title": "BetsAPI Full Documentation",
                "description": "Complete API documentation for BetsAPI integration",
                "version": "1.0.0"
            },
            "servers": [
                {
                    "url": self.API_ENDPOINT,
                    "description": "BetsAPI Production Server"
                }
            ],
            "paths": {},
            "components": {
                "securitySchemes": {
                    "ApiKeyAuth": {
                        "type": "apiKey",
                        "in": "query",
                        "name": "token",
                        "description": "API token from BetsAPI"
                    }
                },
                "schemas": {}
            }
        }
        
        # Add endpoints
        for path, endpoint_info in self.endpoints.items():
            spec["paths"][path] = {
                "get": {
                    "summary": endpoint_info["description"],
                    "parameters": endpoint_info["parameters"],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": self.json_schemas.get(path, {
                                        "type": "object",
                                        "properties": {
                                            "success": {"type": "integer"},
                                            "results": {"type": "object"}
                                        }
                                    })
                                }
                            }
                        }
                    },
                    "security": [{"ApiKeyAuth": []}]
                }
            }
        
        # Add common schemas
        spec["components"]["schemas"].update({
            "Team": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                }
            },
            "League": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "cc": {"type": "string", "description": "Country code"}
                }
            },
            "Match": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "sport_id": {"type": "integer"},
                    "time_status": {"type": "string", "enum": ["0", "1", "2", "3", "4"]},
                    "time": {"type": "integer"},
                    "league": {"$ref": "#/components/schemas/League"},
                    "home": {"$ref": "#/components/schemas/Team"},
                    "away": {"$ref": "#/components/schemas/Team"},
                    "ss": {"type": "string", "description": "Score"},
                    "timer": {
                        "type": "object",
                        "properties": {
                            "tm": {"type": "integer", "description": "Current minute"},
                            "ts": {"type": "integer", "description": "Current second"},
                            "tt": {"type": "string", "description": "Period text"}
                        }
                    }
                }
            }
        })
        
        return spec

    def save_results(self, output_dir: str):
        """Save analysis results"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Save OpenAPI spec
        spec = self.generate_openapi_spec()
        with open(os.path.join(output_dir, 'betsapi_full_spec.yaml'), 'w') as f:
            yaml.dump(spec, f, sort_keys=False)
        
        # Save raw JSON schemas
        with open(os.path.join(output_dir, 'json_schemas.json'), 'w') as f:
            json.dump(self.json_schemas, f, indent=2)
        
        # Save endpoints
        with open(os.path.join(output_dir, 'endpoints.json'), 'w') as f:
            json.dump(self.endpoints, f, indent=2)
        
        # Save analysis report
        with open(os.path.join(output_dir, 'analysis_report.md'), 'w') as f:
            f.write("# BetsAPI Documentation Analysis\n\n")
            
            f.write("## Analyzed Pages\n")
            for url in self.visited_urls:
                f.write(f"- {url}\n")
            
            f.write("\n## Found Endpoints\n")
            for path, info in self.endpoints.items():
                f.write(f"### {path}\n")
                f.write(f"- Description: {info['description']}\n")
                f.write("- Parameters:\n")
                for param in info['parameters']:
                    f.write(f"  - {param['name']}: {param['description']}\n")
            
            f.write("\n## Sport IDs\n")
            for sport_id, sport_name in self.sport_ids.items():
                f.write(f"- {sport_id}: {sport_name}\n")

def main():
    analyzer = BetsAPIFullAnalyzer()
    
    logger.info("Starting comprehensive BetsAPI documentation analysis...")
    analyzer.crawl_documentation()
    
    logger.info("Analyzing live API endpoints...")
    analyzer.analyze_api_endpoints()
    
    output_dir = os.path.join(os.path.dirname(__file__), "betsapi_analysis")
    analyzer.save_results(output_dir)
    
    logger.info(f"Analysis complete. Results saved to: {output_dir}")
    logger.info(f"- Full OpenAPI spec: {os.path.join(output_dir, 'betsapi_full_spec.yaml')}")
    logger.info(f"- JSON schemas: {os.path.join(output_dir, 'json_schemas.json')}")
    logger.info(f"- Endpoints: {os.path.join(output_dir, 'endpoints.json')}")
    logger.info(f"- Analysis report: {os.path.join(output_dir, 'analysis_report.md')}")

if __name__ == "__main__":
    main()
