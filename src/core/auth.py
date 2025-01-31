from fastapi import HTTPException, Security, Depends, Request
from fastapi.security import APIKeyQuery
from starlette.status import HTTP_403_FORBIDDEN
from .config import get_settings
from .logging_config import LogConfig

# Initialize logger
logger = LogConfig.get_component_logger("auth")

# Define API token
API_TOKEN = "180846-RVi16IBGld4Pvr"
API_TOKEN_NAME = "token"

# Use APIKeyQuery for query parameter-based authentication
api_token_query = APIKeyQuery(name=API_TOKEN_NAME, auto_error=False)

async def verify_token(
    request: Request,
    api_token: str = Security(api_token_query)
) -> str:
    """Verify API token from query parameter."""
    if not api_token:
        logger.error("No API token provided")
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="No API token provided. Use ?token=YOUR-TOKEN in the URL."
        )
    
    if api_token != API_TOKEN:
        logger.error("Invalid API token provided")
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Invalid API token"
        )
    
    logger.debug(f"Successfully authenticated request to {request.url.path}")
    return api_token

class AuthConfig:
    """Authentication configuration for external APIs."""
    
    @staticmethod
    def get_sports_api_params():
        """Get common query parameters for sports API requests."""
        return {
            "token": API_TOKEN
        }
    
    @staticmethod
    def get_sports_api_headers():
        """Get headers for sports API requests."""
        return {
            "Accept": "application/json"
        }
    
    @staticmethod
    async def verify_api_token(token: str) -> bool:
        """Verify if the provided token is valid."""
        return token == API_TOKEN
