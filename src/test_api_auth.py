import aiohttp
import asyncio
from core.api_config import B365APIConfig
from core.logging_config import LogConfig

# Setup logging
logger = LogConfig.get_component_logger("api_test")

async def test_api_authentication():
    """Test authentication with B365 API"""
    # Get API configuration
    base_url = B365APIConfig.get_base_url()
    auth_params = B365APIConfig.get_auth_params()
    
    # Test endpoint (we'll use a simple endpoint to verify auth)
    test_url = f"{base_url}/v3/events/upcoming"
    
    try:
        async with aiohttp.ClientSession() as session:
            logger.info(f"Testing API authentication with URL: {test_url}")
            logger.debug(f"Using auth params: {auth_params}")
            
            async with session.get(test_url, params=auth_params) as response:
                status = response.status
                text = await response.text()
                
                logger.info(f"API Response Status: {status}")
                logger.debug(f"API Response Body: {text}")
                
                if status == 200:
                    print("✅ Authentication successful!")
                    print(f"Response: {text}")
                else:
                    print("❌ Authentication failed!")
                    print(f"Status: {status}")
                    print(f"Response: {text}")
                
                return status == 200
                
    except Exception as e:
        logger.error(f"Error testing API authentication: {str(e)}")
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    # Run the test
    print("Testing B365 API Authentication...")
    asyncio.run(test_api_authentication())
