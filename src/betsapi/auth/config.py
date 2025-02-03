"""
BetsAPI Authentication Configuration

This module handles the base configuration for BetsAPI including:
- API endpoints
- Authentication token
- Base URL configuration
"""

class BetsAPIConfig:
    # Primary API endpoint
    PRIMARY_URL = "https://api.b365api.com"
    
    # Backup API endpoint in case of issues with primary
    BACKUP_URL = "https://api.betsapi.com"
    
    # API token - this should be kept secure
    TOKEN = "180846-0nb22aL4DeG73U"
    
    @classmethod
    def get_base_url(cls) -> str:
        """Get the primary API endpoint"""
        return cls.PRIMARY_URL
        
    @classmethod
    def get_backup_url(cls) -> str:
        """Get the backup API endpoint"""
        return cls.BACKUP_URL
    
    @classmethod
    def get_token(cls) -> str:
        """Get the API token"""
        return cls.TOKEN
    
    @classmethod
    def add_token_to_params(cls, params: dict) -> dict:
        """Add token to the given parameters dict"""
        params['token'] = cls.TOKEN
        return params
