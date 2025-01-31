import requests
import os
from datetime import datetime

# Sport IDs and their emojis
SPORTS = {
    '1': {'name': 'Soccer', 'emoji': '⚽'},
    '2': {'name': 'Tennis', 'emoji': '🎾'},
    '3': {'name': 'Basketball', 'emoji': '🏀'},
    '4': {'name': 'Ice Hockey', 'emoji': '🏒'},
    '5': {'name': 'Baseball', 'emoji': '⚾'},
    '91': {'name': 'Volleyball', 'emoji': '🏐'},
    '92': {'name': 'Handball', 'emoji': '🤾‍♀️'},
    '94': {'name': 'Badminton', 'emoji': '🏸'},
    '78': {'name': 'Darts', 'emoji': '🎯'},
    '19': {'name': 'Snooker', 'emoji': '🎱'},
    '20': {'name': 'Table Tennis', 'emoji': '🏓'},
}

def is_esport(league_name):
    """Check if a league is an e-sport"""
    esport_keywords = ['esport', 'e-sport', 'cs:', 'dota', 'league of legends']
    return any(keyword in league_name.lower() for keyword in esport_keywords)

def get_period(match, sport_id):
    """Get the current period/status of a match"""
    time_status = match.get('time_status', '0')
    timer = match.get('timer', {})
    period = timer.get('p', '1')
    
    if sport_id == '3':  # Basketball
        return f'Q{period}'
    elif sport_id == '4':  # Ice Hockey
        return f'P{period}'
    elif sport_id == '1':  # Soccer
        return '2H' if period == '2' else '1H'
    else:
        return '-'

def format_match(match, sport_id):
    """Format match with minimal essential information"""
    league = match.get('league', {}).get('name', 'Unknown League')
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', 'vs')
    timer = match.get('timer', {})
    time = timer.get('tm', '0')
    period = get_period(match, sport_id)
    
    sport_info = SPORTS.get(sport_id, {'emoji': '🎮'})
    
    # Special formatting for volleyball
    if sport_id == '91':  # Volleyball
        scores = match.get('scores', {})
        set_scores = []
        for i in range(1, 6):  # Volleyball can have up to 5 sets
            set_score = scores.get(str(i))
            if set_score:
                set_scores.append(f"{set_score['home']}-{set_score['away']}")
        sets_display = ' | '.join(set_scores)
        return f"{league}\n{sport_info['emoji']} {home} vs {away}\n📊 Sets: {sets_display}\n⏰ Current Set: {score}\n"
    
    return f"{league}\n{sport_info['emoji']} {home} {score} {away}\n⏰ {time}' ({period})\n"

def fetch_live_matches(sport_id):
    """Fetch live matches for a specific sport"""
    url = "https://api.b365api.com/v1/events/inplay"
    params = {
        "sport_id": sport_id,
        "token": "180846-0nb22aL4DeG73U"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get('success') != 1:
            return []
        
        matches = data.get('results', [])
        # Filter out e-sports matches
        matches = [m for m in matches if not is_esport(m.get('league', {}).get('name', ''))]
        return matches
    except Exception as e:
        print(f"Error fetching matches for sport {sport_id}: {str(e)}")
        return []

def main():
    print("🔍 Fetching live matches for all sports...\n")
    
    for sport_id, sport_info in SPORTS.items():
        matches = fetch_live_matches(sport_id)
        if matches:
            print(f"📱 Live {sport_info['name']} Matches ({len(matches)} total)\n")
            for match in matches:
                print(format_match(match, sport_id))
            print()

if __name__ == "__main__":
    main()
