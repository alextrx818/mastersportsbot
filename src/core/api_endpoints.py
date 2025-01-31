from enum import Enum
from typing import Dict, Optional, List

class SportID(Enum):
    """Sport IDs for B365 API"""
    SOCCER = 1
    BASKETBALL = 18
    TENNIS = 13
    VOLLEYBALL = 91
    TABLE_TENNIS = 92
    BASEBALL = 16
    AMERICAN_FOOTBALL = 12
    ICE_HOCKEY = 17
    ESPORTS = 151

class B365Endpoints:
    """B365 API Endpoints Configuration"""
    
    class Endpoint:
        def __init__(self, path: str, required_params: List[str], optional_params: Optional[List[str]] = None):
            self.path = path
            self.required_params = required_params
            self.optional_params = optional_params or []
    
    # Define all available endpoints
    ENDPOINTS = {
        # Sports and Leagues
        "sports": Endpoint(
            path="/v3/sports",
            required_params=[],
            optional_params=["sport_id"]
        ),
        "leagues": Endpoint(
            path="/v3/leagues",
            required_params=["sport_id"]
        ),
        
        # Events and Games
        "upcoming_events": Endpoint(
            path="/v3/events/upcoming",
            required_params=["sport_id"],
            optional_params=["league_id", "day", "page"]
        ),
        "live_events": Endpoint(
            path="/v3/events/inplay",
            required_params=["sport_id"],
            optional_params=["league_id"]
        ),
        "event_odds": Endpoint(
            path="/v3/event/odds",
            required_params=["event_id"],
            optional_params=["market_id"]
        ),
        
        # Results
        "event_results": Endpoint(
            path="/v3/event/result",
            required_params=["event_id"]
        ),
        "league_results": Endpoint(
            path="/v3/league/result",
            required_params=["league_id"],
            optional_params=["day", "page"]
        ),
        
        # Statistics
        "event_stats": Endpoint(
            path="/v3/event/stats",
            required_params=["event_id"]
        ),
        "league_stats": Endpoint(
            path="/v3/league/stats",
            required_params=["league_id"]
        )
    }
    
    @classmethod
    def get_endpoint(cls, name: str) -> Endpoint:
        """Get endpoint configuration by name"""
        if name not in cls.ENDPOINTS:
            raise ValueError(f"Unknown endpoint: {name}")
        return cls.ENDPOINTS[name]
    
    @classmethod
    def validate_params(cls, endpoint_name: str, params: Dict) -> bool:
        """Validate parameters for an endpoint"""
        endpoint = cls.get_endpoint(endpoint_name)
        
        # Check required parameters
        missing_params = [param for param in endpoint.required_params if param not in params]
        if missing_params:
            raise ValueError(f"Missing required parameters for {endpoint_name}: {missing_params}")
        
        # Check if there are any unknown parameters
        all_valid_params = endpoint.required_params + endpoint.optional_params
        unknown_params = [param for param in params if param not in all_valid_params]
        if unknown_params:
            raise ValueError(f"Unknown parameters for {endpoint_name}: {unknown_params}")
        
        return True

    @classmethod
    def get_sport_name(cls, sport_id: int) -> str:
        """Get sport name from ID"""
        try:
            return [sport for sport in SportID if sport.value == sport_id][0].name
        except IndexError:
            raise ValueError(f"Unknown sport ID: {sport_id}")
    
    @classmethod
    def get_sport_id(cls, sport_name: str) -> int:
        """Get sport ID from name"""
        try:
            return SportID[sport_name.upper()].value
        except KeyError:
            raise ValueError(f"Unknown sport name: {sport_name}")
