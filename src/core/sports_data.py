from typing import Dict, List, Optional
import os
from .api_client import B365Client
from .logging_config import LogConfig

logger = LogConfig.get_component_logger("sports_data")

class SportsData:
    """Handler for sports data and formatting"""
    
    SPORTS = {
        1: {'name': 'Soccer', 'emoji': '⚽'},
        18: {'name': 'Basketball', 'emoji': '🏀'},
        13: {'name': 'Tennis', 'emoji': '🎾'},
        91: {'name': 'Volleyball', 'emoji': '🏐'},
        17: {'name': 'Ice Hockey', 'emoji': '🏒'},
        14: {'name': 'Snooker', 'emoji': '🎱'},
        78: {'name': 'Handball', 'emoji': '🤾‍♀️'},
        15: {'name': 'Darts', 'emoji': '🎯'},
        92: {'name': 'Table Tennis', 'emoji': '🏓'}
    }

    ESPORT_KEYWORDS = ['esoccer', 'esports', 'e-', 'cyber', 'ebasketball', 
                      'etennis', 'evolleyball', 'ehockey']

    def __init__(self):
        """Initialize sports data handler"""
        self.api_client = B365Client()

    @staticmethod
    def is_esport(league_name: str) -> bool:
        """Check if the league is an e-sport league"""
        league_name = league_name.lower()
        return any(keyword in league_name for keyword in SportsData.ESPORT_KEYWORDS)

    @staticmethod
    def get_period(match: Dict, sport_id: int) -> str:
        """Get the current period of the match"""
        time_status = match.get('time_status')
        timer = match.get('timer', {})
        time = timer.get('tm', '0')
        
        if time_status == '1':  # Match is live
            if sport_id == 1:  # Soccer
                if int(time) <= 45:
                    return '1H'
                else:
                    return '2H'
            elif sport_id == 18:  # Basketball
                quarter = timer.get('q', '1')
                return f'Q{quarter}'
            elif sport_id == 13:  # Tennis
                score = match.get('ss', '')
                if score:
                    completed_sets = score.count(',')
                    current_set = completed_sets + 1
                    return f'Set {current_set}'
            elif sport_id == 91:  # Volleyball
                set_info = timer.get('set', '1')
                return f'Set {set_info}'
            elif sport_id == 17:  # Ice Hockey
                period = timer.get('p', '1')
                return f'P{period}'
            elif sport_id == 14:  # Snooker
                frame = timer.get('f', '1')
                return f'Frame {frame}'
            elif sport_id == 78:  # Handball
                half = int(time) <= 30 and '1H' or '2H'
                return half
            elif sport_id == 15:  # Darts
                set_info = timer.get('set', '1')
                leg = timer.get('leg', '1')
                return f'Set {set_info} Leg {leg}'
            elif sport_id == 92:  # Table Tennis
                game = timer.get('game', '1')
                return f'Game {game}'
        return '-'

    @staticmethod
    def format_match(match: Dict, sport_id: int) -> str:
        """Format match with minimal essential information"""
        league = match.get('league', {}).get('name', 'Unknown League')
        home = match.get('home', {}).get('name', 'Unknown')
        away = match.get('away', {}).get('name', 'Unknown')
        score = match.get('ss', 'vs')
        timer = match.get('timer', {})
        time = timer.get('tm', '0')
        period = SportsData.get_period(match, sport_id)
        
        sport_info = SportsData.SPORTS.get(sport_id, {'emoji': '🎮'})
        return f"{league}\n{sport_info['emoji']} {home} {score} {away}\n⏰ {time}' ({period})\n"

    async def fetch_live_matches(self, sport_id: int) -> List[str]:
        """Fetch and format live matches for a specific sport"""
        try:
            data = await self.api_client.get_live_events(sport_id)
            
            if data:
                matches = data.get('results', [])
                # Filter out e-sports matches
                real_matches = [m for m in matches if not self.is_esport(m.get('league', {}).get('name', ''))]
                sport_info = self.SPORTS.get(sport_id, {'name': 'Unknown'})
                
                formatted_matches = []
                formatted_matches.append(f"\n📱 Live {sport_info['name']} Matches ({len(real_matches)} total)\n")
                
                # Sort matches by time (descending)
                real_matches.sort(key=lambda x: int(x.get('timer', {}).get('tm', 0)), reverse=True)
                
                for match in real_matches:
                    formatted_matches.append(self.format_match(match, sport_id))
                
                return formatted_matches
            
            logger.error(f"No data returned for sport ID {sport_id}")
            return []
            
        except Exception as e:
            logger.error(f"Error fetching matches for sport {sport_id}: {str(e)}")
            return []

    async def test_all_sports(self) -> List[str]:
        """Test API connection for all supported sports"""
        all_matches = []
        for sport_id in self.SPORTS.keys():
            matches = await self.fetch_live_matches(sport_id)
            all_matches.extend(matches)
        return all_matches
