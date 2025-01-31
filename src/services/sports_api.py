import aiohttp
from ..core.config import get_settings
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)
settings = get_settings()

class SportsAPI:
    def __init__(self):
        self.api_key = settings.SPORTS_API_KEY
        self.base_url = "https://api.sportsdata.io/v3"
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def get_live_games(self, sport: str) -> List[Dict]:
        """Fetch live games for a specific sport."""
        try:
            endpoint = f"{self.base_url}/{sport}/scores/json/LiveGames"
            async with self.session.get(endpoint, params={"key": self.api_key}) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logger.error(f"Error fetching live games: {response.status}")
                    return []
        except Exception as e:
            logger.error(f"Error in get_live_games: {str(e)}")
            return []

    async def get_game_odds(self, game_id: str) -> Optional[Dict]:
        """Fetch odds for a specific game."""
        try:
            endpoint = f"{self.base_url}/odds/json/GameOdds/{game_id}"
            async with self.session.get(endpoint, params={"key": self.api_key}) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logger.error(f"Error fetching game odds: {response.status}")
                    return None
        except Exception as e:
            logger.error(f"Error in get_game_odds: {str(e)}")
            return None
