import aiohttp
from typing import Dict, Any, Optional
from .api_config import B365APIConfig
from .api_endpoints import B365Endpoints
from .logging_config import LogConfig

logger = LogConfig.get_component_logger("api_client")

class B365Client:
    """Client for interacting with B365 API"""
    
    def __init__(self):
        self.config = B365APIConfig
        self.endpoints = B365Endpoints
    
    async def _make_request(self, endpoint_name: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a request to the API"""
        params = params or {}
        endpoint = self.endpoints.get_endpoint(endpoint_name)
        
        # Validate parameters
        self.endpoints.validate_params(endpoint_name, params)
        
        # Add authentication
        params.update(self.config.get_auth_params())
        
        # Build URL
        url = self.config.get_full_url(endpoint.path)
        
        try:
            logger.debug(f"Making request to {url} with params: {params}")
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    data = await response.json()
                    
                    if response.status != 200:
                        logger.error(f"API error: {data}")
                        raise Exception(f"API error: {data.get('error', 'Unknown error')}")
                    
                    return data
                    
        except Exception as e:
            logger.error(f"Error making request to {url}: {str(e)}")
            raise
    
    async def get_sports(self) -> Dict[str, Any]:
        """Get list of available sports"""
        return await self._make_request("sports")
    
    async def get_leagues(self, sport_id: int) -> Dict[str, Any]:
        """Get leagues for a sport"""
        return await self._make_request("leagues", {"sport_id": sport_id})
    
    async def get_upcoming_events(self, sport_id: int, league_id: Optional[int] = None, 
                                day: Optional[str] = None, page: Optional[int] = None) -> Dict[str, Any]:
        """Get upcoming events"""
        params = {"sport_id": sport_id}
        if league_id:
            params["league_id"] = league_id
        if day:
            params["day"] = day
        if page:
            params["page"] = page
        return await self._make_request("upcoming_events", params)
    
    async def get_live_events(self, sport_id: int, league_id: Optional[int] = None) -> Dict[str, Any]:
        """Get live events"""
        params = {"sport_id": sport_id}
        if league_id:
            params["league_id"] = league_id
        return await self._make_request("live_events", params)
    
    async def get_event_odds(self, event_id: int, market_id: Optional[int] = None) -> Dict[str, Any]:
        """Get odds for an event"""
        params = {"event_id": event_id}
        if market_id:
            params["market_id"] = market_id
        return await self._make_request("event_odds", params)
    
    async def get_event_results(self, event_id: int) -> Dict[str, Any]:
        """Get results for an event"""
        return await self._make_request("event_results", {"event_id": event_id})
    
    async def get_league_results(self, league_id: int, day: Optional[str] = None, 
                               page: Optional[int] = None) -> Dict[str, Any]:
        """Get results for a league"""
        params = {"league_id": league_id}
        if day:
            params["day"] = day
        if page:
            params["page"] = page
        return await self._make_request("league_results", params)
    
    async def get_event_stats(self, event_id: int) -> Dict[str, Any]:
        """Get statistics for an event"""
        return await self._make_request("event_stats", {"event_id": event_id})
    
    async def get_league_stats(self, league_id: int) -> Dict[str, Any]:
        """Get statistics for a league"""
        return await self._make_request("league_stats", {"league_id": league_id})
