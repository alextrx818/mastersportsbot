import aiohttp
import logging
from typing import Dict, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class OddsApiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.the-odds-api.com/v4"
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def get_sports(self) -> List[Dict]:
        """Get all available sports."""
        try:
            url = f"{self.base_url}/sports"
            params = {"apiKey": self.api_key}
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    # Log remaining requests
                    remaining = response.headers.get('x-requests-remaining', 'unknown')
                    logger.info(f"Remaining API requests: {remaining}")
                    return data
                else:
                    logger.error(f"Error fetching sports: {response.status}")
                    return []
        except Exception as e:
            logger.error(f"Error in get_sports: {str(e)}")
            return []

    async def get_odds(self, sport_key: str, regions: str = 'us', markets: str = 'h2h,spreads,totals') -> List[Dict]:
        """Get live odds for a specific sport.
        
        Args:
            sport_key: The sport key (e.g., 'basketball_nba')
            regions: Comma-separated regions (default: 'us')
            markets: Comma-separated markets (default: 'h2h,spreads,totals')
        """
        try:
            url = f"{self.base_url}/sports/{sport_key}/odds"
            params = {
                "apiKey": self.api_key,
                "regions": regions,
                "markets": markets,
                "oddsFormat": "decimal"
            }
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    remaining = response.headers.get('x-requests-remaining', 'unknown')
                    logger.info(f"Remaining API requests: {remaining}")
                    return data
                else:
                    logger.error(f"Error fetching odds: {response.status}")
                    return []
        except Exception as e:
            logger.error(f"Error in get_odds: {str(e)}")
            return []

    async def get_scores(self, sport_key: str, daysFrom: int = 1) -> List[Dict]:
        """Get scores for a specific sport.
        
        Args:
            sport_key: The sport key (e.g., 'basketball_nba')
            daysFrom: Number of days from current date (default: 1)
        """
        try:
            url = f"{self.base_url}/sports/{sport_key}/scores"
            params = {
                "apiKey": self.api_key,
                "daysFrom": daysFrom
            }
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    remaining = response.headers.get('x-requests-remaining', 'unknown')
                    logger.info(f"Remaining API requests: {remaining}")
                    return data
                else:
                    logger.error(f"Error fetching scores: {response.status}")
                    return []
        except Exception as e:
            logger.error(f"Error in get_scores: {str(e)}")
            return []

    def _log_api_usage(self, response) -> None:
        """Log API usage information from response headers."""
        remaining = response.headers.get('x-requests-remaining', 'unknown')
        used = response.headers.get('x-requests-used', 'unknown')
        logger.info(f"API Requests - Remaining: {remaining}, Used: {used}")
