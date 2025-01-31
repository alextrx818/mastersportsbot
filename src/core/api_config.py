from typing import Dict

class B365APIConfig:
    """Configuration for the B365 API"""
    
    BASE_URL = "https://api.b365api.com"
    TOKEN = "180846-RVi16IBGld4Pvr"
    
    @classmethod
    def get_base_url(cls) -> str:
        """Get the base URL for the API"""
        return cls.BASE_URL
    
    @classmethod
    def get_full_url(cls, endpoint: str) -> str:
        """Get the full URL for a specific endpoint"""
        return f"{cls.BASE_URL}/{endpoint.lstrip('/')}"
    
    @classmethod
    def get_auth_params(cls) -> Dict[str, str]:
        """Get authentication parameters for API requests"""
        return {
            "token": cls.TOKEN
        }
