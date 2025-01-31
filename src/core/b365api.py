import aiohttp
from typing import Dict, Any
from enum import Enum

class SportID(Enum):
    """Sport IDs for B365 API"""
    SOCCER = 1
    BASKETBALL = 18
    TENNIS = 13
    VOLLEYBALL = 91
    HANDBALL = 78
    BASEBALL = 16
    ICE_HOCKEY = 17
    AMERICAN_FOOTBALL = 12
    SNOOKER = 14
    DARTS = 15
    TABLE_TENNIS = 92
    BADMINTON = 94
    RUGBY_LEAGUE = 19
    AUSTRALIAN_RULES = 36
    BEACH_VOLLEYBALL = 95

class B365API:
    """Simple B365 API Client"""
    
    BASE_URL = "https://api.b365api.com"
    TOKEN = "180846-RVi16IBGld4Pvr"
    
    @classmethod
    async def get_inplay_events(cls, sport_id: int) -> Dict[str, Any]:
        """Get in-play events for a specific sport"""
        endpoint = f"{cls.BASE_URL}/v3/events/inplay"
        params = {
            "sport_id": sport_id,
            "token": cls.TOKEN
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint, params=params) as response:
                return await response.json()
    
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
