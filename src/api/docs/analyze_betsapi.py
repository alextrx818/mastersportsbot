import requests
from bs4 import BeautifulSoup
import yaml
import json
import re
from typing import Dict, List, Any
import os

class BetsAPIDocAnalyzer:
    """Analyzes BetsAPI documentation and generates OpenAPI/Swagger specification"""
    
    BASE_URL = "https://betsapi.com/docs"
    API_ENDPOINT = "https://api.b365api.com"
    
    def __init__(self):
        self.session = requests.Session()
        self.spec = {
            "openapi": "3.0.0",
            "info": {
                "title": "BetsAPI Integration",
                "description": "Auto-generated API documentation for BetsAPI integration",
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
                        "name": "token"
                    }
                },
                "schemas": {}
            }
        }
    
    def fetch_page(self, url: str) -> str:
        """Fetch a documentation page"""
        response = requests.get(url)
        return response.text
    
    def parse_endpoint(self, content: str) -> Dict[str, Any]:
        """Parse endpoint details from documentation"""
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find endpoint path and method
        endpoint_h1 = soup.find('h1')
        if not endpoint_h1:
            return {}
            
        endpoint_info = {
            "path": "",
            "method": "get",  # Default to GET
            "description": "",
            "parameters": [],
            "responses": {
                "200": {
                    "description": "Successful response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "success": {
                                        "type": "integer",
                                        "enum": [1]
                                    },
                                    "results": {
                                        "type": "array",
                                        "items": {
                                            "type": "object"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        
        # Extract parameters from code blocks
        code_blocks = soup.find_all('code')
        for block in code_blocks:
            if 'curl' in block.text:
                # Extract path and parameters from curl example
                curl_match = re.search(r'curl.*?"([^"]+)"', block.text)
                if curl_match:
                    url = curl_match.group(1)
                    if '?' in url:
                        path, params = url.split('?', 1)
                        endpoint_info["path"] = path.replace(self.API_ENDPOINT, '')
                        
                        # Parse parameters
                        for param in params.split('&'):
                            if '=' in param:
                                name, value = param.split('=', 1)
                                if name != 'token':  # Skip auth token
                                    endpoint_info["parameters"].append({
                                        "name": name,
                                        "in": "query",
                                        "required": True,
                                        "schema": {
                                            "type": "string"
                                        }
                                    })
        
        return endpoint_info
    
    def analyze_documentation(self):
        """Analyze all documentation pages and build OpenAPI spec"""
        # Start with main documentation page
        main_content = self.fetch_page(f"{self.BASE_URL}/events/index.html")
        soup = BeautifulSoup(main_content, 'html.parser')
        
        # Find all documentation links
        for link in soup.find_all('a', href=True):
            if link['href'].startswith(self.BASE_URL):
                page_content = self.fetch_page(link['href'])
                endpoint_info = self.parse_endpoint(page_content)
                
                if endpoint_info and endpoint_info["path"]:
                    path = endpoint_info["path"]
                    method = endpoint_info["method"]
                    
                    if path not in self.spec["paths"]:
                        self.spec["paths"][path] = {}
                    
                    self.spec["paths"][path][method] = {
                        "summary": endpoint_info.get("summary", ""),
                        "description": endpoint_info.get("description", ""),
                        "parameters": endpoint_info["parameters"],
                        "responses": endpoint_info["responses"],
                        "security": [{"ApiKeyAuth": []}]
                    }
    
    def save_spec(self, output_file: str):
        """Save the OpenAPI specification to a YAML file"""
        with open(output_file, 'w') as f:
            yaml.dump(self.spec, f, sort_keys=False)

class BetsAPIDocGenerator:
    """Generates OpenAPI/Swagger specification for known BetsAPI endpoints"""
    
    API_ENDPOINT = "https://api.b365api.com"
    
    def __init__(self):
        self.spec = {
            "openapi": "3.0.0",
            "info": {
                "title": "BetsAPI Integration",
                "description": "API documentation for BetsAPI integration",
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
                "schemas": {
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
                    },
                    "Error": {
                        "type": "object",
                        "properties": {
                            "success": {"type": "integer", "enum": [0]},
                            "error": {"type": "integer"},
                            "error_detail": {"type": "string"}
                        }
                    }
                }
            }
        }
        
        # Add known endpoints
        self.add_known_endpoints()
    
    def add_known_endpoints(self):
        """Add known BetsAPI endpoints"""
        
        # GET /v1/events/inplay
        self.spec["paths"]["/v1/events/inplay"] = {
            "get": {
                "summary": "Get live events",
                "description": "Returns a list of live events, optionally filtered by sport_id",
                "parameters": [
                    {
                        "name": "sport_id",
                        "in": "query",
                        "description": "Sport ID (1=Soccer, 18=Basketball, 91=Volleyball, etc)",
                        "required": True,
                        "schema": {"type": "integer"}
                    },
                    {
                        "name": "league_id",
                        "in": "query",
                        "description": "Filter by league ID",
                        "required": False,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {"type": "integer", "enum": [1]},
                                        "results": {
                                            "type": "array",
                                            "items": {"$ref": "#/components/schemas/Match"}
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "401": {
                        "description": "Authentication error",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                },
                "security": [{"ApiKeyAuth": []}]
            }
        }
        
        # GET /v1/events/upcoming
        self.spec["paths"]["/v1/events/upcoming"] = {
            "get": {
                "summary": "Get upcoming events",
                "description": "Returns a list of upcoming events for a specific sport",
                "parameters": [
                    {
                        "name": "sport_id",
                        "in": "query",
                        "description": "Sport ID (1=Soccer, 18=Basketball, 91=Volleyball, etc)",
                        "required": True,
                        "schema": {"type": "integer"}
                    },
                    {
                        "name": "league_id",
                        "in": "query",
                        "description": "Filter by league ID",
                        "required": False,
                        "schema": {"type": "integer"}
                    },
                    {
                        "name": "day",
                        "in": "query",
                        "description": "Filter by day (YYYYMMDD format)",
                        "required": False,
                        "schema": {"type": "string"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {"type": "integer", "enum": [1]},
                                        "results": {
                                            "type": "array",
                                            "items": {"$ref": "#/components/schemas/Match"}
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "401": {
                        "description": "Authentication error",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                },
                "security": [{"ApiKeyAuth": []}]
            }
        }
        
        # GET /v1/event/view
        self.spec["paths"]["/v1/event/view/{event_id}"] = {
            "get": {
                "summary": "Get event details",
                "description": "Returns detailed information about a specific event",
                "parameters": [
                    {
                        "name": "event_id",
                        "in": "path",
                        "description": "Event ID",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {"type": "integer", "enum": [1]},
                                        "results": {"$ref": "#/components/schemas/Match"}
                                    }
                                }
                            }
                        }
                    },
                    "401": {
                        "description": "Authentication error",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                },
                "security": [{"ApiKeyAuth": []}]
            }
        }
    
    def save_spec(self, output_file: str):
        """Save the OpenAPI specification to a YAML file"""
        with open(output_file, 'w') as f:
            yaml.dump(self.spec, f, sort_keys=False)

def main():
    analyzer = BetsAPIDocAnalyzer()
    print("Analyzing BetsAPI documentation...")
    analyzer.analyze_documentation()
    
    generator = BetsAPIDocGenerator()
    output_file = os.path.join(os.path.dirname(__file__), "betsapi_swagger_auto.yaml")
    analyzer.spec.update(generator.spec)
    analyzer.save_spec(output_file)
    print(f"Generated OpenAPI specification saved to: {output_file}")

if __name__ == "__main__":
    main()
