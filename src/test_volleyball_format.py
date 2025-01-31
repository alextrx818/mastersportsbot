import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Copy of standard sports dictionary with test modifications for volleyball
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

def format_volleyball_match(match):
    """Test function for volleyball specific formatting"""
    league = match.get('league', {}).get('name', 'Unknown League')
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', 'vs')
    scores = match.get('scores', {})
    
    # Format set scores
    set_scores = []
    for i in range(1, 6):  # Volleyball can have up to 5 sets
        set_score = scores.get(str(i))
        if set_score:
            set_scores.append(f"{set_score['home']}-{set_score['away']}")
    sets_display = ' | '.join(set_scores)
    
    return f"{league}\n🏐 {home} vs {away}\n📊 Sets: {sets_display}\n⏰ Current Set: {score}\n"

def test_volleyball_format():
    """Test volleyball specific formatting"""
    api_key = os.getenv('SPORTS_API_KEY')
    api_host = os.getenv('SPORTS_API_HOST')
    
    url = f"https://{api_host}/v3/events/inplay"
    params = {
        'token': api_key,
        'sport_id': 91  # Volleyball
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success') == 1:
                matches = data.get('results', [])
                print(f"\n📱 Testing Volleyball Format ({len(matches)} matches)\n")
                
                for match in matches:
                    print(format_volleyball_match(match))
            else:
                print("\n❌ API returned success = 0")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error connecting to API: {str(e)}")

if __name__ == "__main__":
    test_volleyball_format()
