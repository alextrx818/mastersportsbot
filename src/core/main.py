import os
import requests
from dotenv import load_dotenv
from .sports_format import (
    format_soccer_match,
    format_basketball_match,
    format_hockey_match,
    format_volleyball_match,
    format_tennis_match,
    format_snooker_match,
    format_handball_match,
    format_darts_match,
    format_table_tennis_match
)

# Load environment variables
load_dotenv()

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

def is_esport(league_name):
    """Check if the league is an e-sport league"""
    esport_keywords = ['esoccer', 'esports', 'e-', 'cyber', 'ebasketball', 'etennis', 'evolleyball', 'ehockey']
    league_name = league_name.lower()
    return any(keyword in league_name for keyword in esport_keywords)

def get_period(match, sport_id):
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
            quarter = match.get('timer', {}).get('q', '1')
            return f'Q{quarter}'
        elif sport_id == 13:  # Tennis
            # Get the current score which includes set information
            score = match.get('ss', '')
            if score:
                # Count the number of completed sets by counting commas
                completed_sets = score.count(',')
                # Current set is the number of completed sets + 1
                current_set = completed_sets + 1
                return f'Set {current_set}'
        elif sport_id == 91:  # Volleyball
            set_info = match.get('timer', {}).get('set', '1')
            return f'Set {set_info}'
        elif sport_id == 17:  # Ice Hockey
            period = match.get('timer', {}).get('p', '1')
            return f'P{period}'
        elif sport_id == 14:  # Snooker
            frame = match.get('timer', {}).get('f', '1')
            return f'Frame {frame}'
        elif sport_id == 78:  # Handball
            half = int(time) <= 30 and '1H' or '2H'
            return half
        elif sport_id == 15:  # Darts
            set_info = match.get('timer', {}).get('set', '1')
            leg = match.get('timer', {}).get('leg', '1')
            return f'Set {set_info} Leg {leg}'
        elif sport_id == 92:  # Table Tennis
            game = match.get('timer', {}).get('game', '1')
            return f'Game {game}'
    return '-'

def format_match(match, sport_id):
    """Format match with minimal essential information"""
    # Use sport-specific formatters
    if sport_id == 1:  # Soccer
        return format_soccer_match(match)
    elif sport_id == 18:  # Basketball
        return format_basketball_match(match)
    elif sport_id == 13:  # Tennis
        return format_tennis_match(match)
    elif sport_id == 91:  # Volleyball
        return format_volleyball_match(match)
    elif sport_id == 17:  # Ice Hockey
        return format_hockey_match(match)
    elif sport_id == 14:  # Snooker
        return format_snooker_match(match)
    elif sport_id == 78:  # Handball
        return format_handball_match(match)
    elif sport_id == 15:  # Darts
        return format_darts_match(match)
    elif sport_id == 92:  # Table Tennis
        return format_table_tennis_match(match)
    
    # Default format for any unhandled sports
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', 'vs')
    timer = match.get('timer', {})
    time = timer.get('tm', '0')
    
    sport = SPORTS.get(sport_id, {})
    emoji = sport.get('emoji', '')
    
    return f"{emoji} {home} {score} {away}\n⏰ {time}'"

def fetch_live_matches(sport_id):
    """Fetch live matches for a specific sport"""
    api_key = "180846-0nb22aL4DeG73U"
    api_host = "api.b365api.com"
    
    # Make API request
    url = f'https://{api_host}/v1/events/inplay?sport_id={sport_id}&token={api_key}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching matches: {response.status_code}")
        return []
    
    try:
        data = response.json()
        if 'results' not in data:
            print("No live matches found")
            return []
        
        matches = data['results']
        # Filter out e-sport matches
        matches = [m for m in matches if not is_esport(m.get('league', {}).get('name', ''))]
        
        # Print sport header with match count
        sport_info = SPORTS.get(sport_id, {'name': 'Unknown', 'emoji': '🎮'})
        print(f"\n📱 Live {sport_info['name']} Matches ({len(matches)} total)\n")
        
        # Sort matches by league
        matches.sort(key=lambda x: x.get('league', {}).get('name', ''))
        current_league = None
        
        for match in matches:
            league = match.get('league', {}).get('name', '')
            # Print league name when it changes
            if league != current_league:
                print(f"{league}")
                current_league = league
            
            # Format and print match
            print(format_match(match, sport_id))
        
        return matches
    except Exception as e:
        print(f"Error processing matches: {str(e)}")
        return []

def test_api_connection():
    """Test API connection for multiple sports"""
    # Fetch matches for each sport
    for sport_id in SPORTS.keys():
        fetch_live_matches(sport_id)

if __name__ == "__main__":
    test_api_connection()