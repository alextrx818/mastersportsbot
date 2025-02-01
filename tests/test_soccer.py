import unittest
import sys
import os
import requests
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.core.sports_format import format_soccer_match

class B365APISync:
    """Synchronous version of B365API for testing"""
    def __init__(self):
        self.base_url = "https://api.b365api.com/v3"  # Updated to v3
        self.token = "180846-0nb22aL4DeG73U"  # Using same token as b365api.py
        if not self.token:
            raise ValueError("B365_TOKEN environment variable not set")

    def get_inplay_events(self, sport='soccer'):
        endpoint = f"{self.base_url}/events/inplay"
        params = {
            'token': self.token,
            'sport_id': 1,  # 1 is for soccer
            'skip_esports': 'true'
        }
        print(f"Fetching from: {endpoint} with params: {params}")  # Debug output
        response = requests.get(endpoint, params=params)
        print(f"Response status: {response.status_code}")  # Debug output
        if response.status_code != 200:
            print(f"Error response: {response.text}")  # Debug output
            return None
        return response.json()

    def get_event_view(self, event_id):
        """Get detailed match statistics including time-stamped events"""
        endpoint = f"{self.base_url}/event/view"
        params = {
            'token': self.token,
            'event_id': event_id
        }
        print(f"\nFetching event view from: {endpoint} with params: {params}")
        response = requests.get(endpoint, params=params)
        print(f"Response status: {response.status_code}")
        if response.status_code != 200:
            print(f"Error response: {response.text}")
            return None
        return response.json()

class TestSoccerFormat(unittest.TestCase):
    """Test soccer match formatting"""
    
    def setUp(self):
        """Set up test case"""
        print("\nRunning soccer format tests...")
    
    def tearDown(self):
        """Clean up after test"""
        print()
    
    def test_prematch(self):
        match = {
            'home': {'name': 'Manchester United'},
            'away': {'name': 'Arsenal'},
            'timer': {'tm': '0'},
            'scores': {}
        }
        expected = ("⚽ Manchester United - Arsenal\n"
                   "📊 Score: None\n"
                   "⏰ 0' First Half (0:0-0:0)")
        self.assertEqual(format_soccer_match(match), expected)

    def test_first_half_with_scores(self):
        match = {
            'home': {'name': 'Barcelona'},
            'away': {'name': 'Real Madrid'},
            'ss': '2-1',
            'timer': {'tm': '35'},
            'scores': {
                '1': {'home': '2', 'away': '1'}
            }
        }
        expected = ("⚽ Barcelona - Real Madrid\n"
                   "📊 Score: 2-1\n"
                   "⏰ 35' First Half (2:0-1:0)")
        self.assertEqual(format_soccer_match(match), expected)
    
    def test_first_half_injury_time(self):
        match = {
            'home': {'name': 'Liverpool'},
            'away': {'name': 'Everton'},
            'ss': '1-0',
            'timer': {'tm': '45+2'},
            'scores': {
                '1': {'home': '1', 'away': '0'}
            }
        }
        expected = ("⚽ Liverpool - Everton\n"
                   "📊 Score: 1-0\n"
                   "⏰ 45+2' First Half (1:0-0:0)")
        self.assertEqual(format_soccer_match(match), expected)

    def test_halftime(self):
        match = {
            'home': {'name': 'Chelsea'},
            'away': {'name': 'Tottenham'},
            'ss': '2-2',
            'timer': {'tm': 'HT'},
            'scores': {
                '1': {'home': '2', 'away': '2'}
            }
        }
        expected = ("⚽ Chelsea - Tottenham\n"
                   "📊 Score: 2-2\n"
                   "⏰ Halftime Break (2:0-2:0)")
        self.assertEqual(format_soccer_match(match), expected)
    
    def test_second_half_with_scores(self):
        match = {
            'home': {'name': 'Liverpool'},
            'away': {'name': 'Manchester City'},
            'ss': '3-1',
            'timer': {'tm': '75'},
            'scores': {
                '1': {'home': '2', 'away': '0'},
                '2': {'home': '1', 'away': '1'}
            }
        }
        expected = ("⚽ Liverpool - Manchester City\n"
                   "📊 Score: 3-1\n"
                   "⏰ 75' Second Half (2:1-0:1)")
        self.assertEqual(format_soccer_match(match), expected)

    def test_second_half_injury_time(self):
        match = {
            'home': {'name': 'Ajax'},
            'away': {'name': 'PSV'},
            'ss': '3-2',
            'timer': {'tm': '90+3'},
            'scores': {
                '1': {'home': '2', 'away': '1'},
                '2': {'home': '1', 'away': '1'}
            }
        }
        expected = ("⚽ Ajax - PSV\n"
                   "📊 Score: 3-2\n"
                   "⏰ 90+3' Second Half (2:1-1:1)")
        self.assertEqual(format_soccer_match(match), expected)
    
    def test_second_half_with_first_half_goals(self):
        """Test a match where goals were scored in both halves"""
        match = {
            'home': {'name': 'Team A'},
            'away': {'name': 'Team B'},
            'timer': {'tm': '75'},
            'ss': '1-3',  # Final score
            'scores': {
                '1': {'home': '1', 'away': '2'},  # First half score
                '2': {'home': '0', 'away': '1'}   # Second half score
            }
        }
        expected = ("⚽ Team A - Team B\n"
                   "📊 Score: 1-3\n"
                   "⏰ 75' Second Half (1:0-2:1)")
        self.assertEqual(format_soccer_match(match), expected)

    def test_missing_scores(self):
        match = {
            'home': {'name': 'Arsenal'},
            'away': {'name': 'Chelsea'},
            'ss': '0-0',
            'timer': {'tm': '15'}
        }
        expected = ("⚽ Arsenal - Chelsea\n"
                   "📊 Score: 0-0\n"
                   "⏰ 15' First Half (0:0-0:0)")
        self.assertEqual(format_soccer_match(match), expected)

    def test_missing_all_data(self):
        match = {}
        expected = ("⚽ Unknown - Unknown\n"
                   "📊 Score: None\n"
                   "⏰ 0' First Half (0:0-0:0)")
        self.assertEqual(format_soccer_match(match), expected)

def get_match_time_value(match):
    """
    Get a numeric value for sorting matches by time.
    Returns a tuple of (period_priority, minutes) where:
    - period_priority: 0=not started, 1=first half, 2=second half
    - minutes: converted to int, with injury time handled
    """
    timer = match.get('timer', {})
    time = str(timer.get('tm', '0'))
    
    # Not started
    if time == '0':
        return (0, 0)
    
    # Half time
    if time == 'HT':
        return (1, 45)
        
    # Handle injury time (e.g., "45+2", "90+3")
    base_time = time.split('+')[0] if '+' in time else time
    try:
        minutes = int(base_time)
        # First half
        if minutes <= 45:
            return (1, minutes)
        # Second half
        else:
            return (2, minutes)
    except ValueError:
        return (0, 0)

def show_live_soccer_events():
    """Fetch and display all live soccer events using the updated formatting"""
    import time
    start_time = time.time()
    
    api = B365APISync()
    try:
        print("Fetching data from API...")
        fetch_start = time.time()
        data = api.get_inplay_events()
        fetch_time = time.time() - fetch_start
        print(f"API fetch took: {fetch_time:.2f} seconds")
        
        if not data or 'results' not in data:
            print("No live soccer events found")
            return

        print("\nProcessing matches...")
        process_start = time.time()
        matches = data['results']
        matches = [m for m in matches if not is_esport(m.get('league', {}).get('name', ''))]
        
        # Sort matches:
        # 1. First by period (not started → first half → second half)
        # 2. Then by minutes within each period (ascending)
        matches.sort(key=get_match_time_value)
        
        print(f"\nFound {len(matches)} live soccer events (sorted by match time):\n")
        
        current_league = None
        format_start = time.time()
        
        for i, match in enumerate(matches):
            league = match.get('league', {}).get('name', '')
            # Print league name when it changes
            if league != current_league:
                if current_league is not None:
                    print("----------------------------------------")
                print(f"🏆 {league}")
                current_league = league
            
            # Get event view data for Point Fortin match
            if "Point Fortin" in match.get('home', {}).get('name', '') or "Point Fortin" in match.get('away', {}).get('name', ''):
                event_id = match.get('id')
                if event_id:
                    event_data = api.get_event_view(event_id)
                    if event_data:
                        print("\nEvent View Data:")
                        print(event_data)
            
            # Format and print match
            print(format_soccer_match(match))
            
            # Add separator between matches, unless it's the last match
            if i < len(matches) - 1:
                # If next match is from a different league, separator will be added above
                if matches[i + 1].get('league', {}).get('name', '') == current_league:
                    print("· · · · · · · · · ·")
        
        format_time = time.time() - format_start
        process_time = time.time() - process_start
        total_time = time.time() - start_time
        
        print(f"\nTiming:")
        print(f"API fetch: {fetch_time:.2f}s")
        print(f"Data processing: {process_time-format_time:.2f}s")
        print(f"Formatting and display: {format_time:.2f}s")
        print(f"Total time: {total_time:.2f}s")
        print(f"Live events found: {len(matches)}")
            
    except Exception as e:
        print(f"Error fetching events: {str(e)}")

def format_soccer_match(match):
    """Format soccer match with league information and clearer display"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    timer = match.get('timer', {})
    time = str(timer.get('tm', '0'))
    scores = match.get('scores', {})
    
    # Current score
    score = match.get('ss')
    if not score or score == 'None':
        return "\n".join([
            f"⚽ {home} - {away}",
            f"📊 Score: None",
            f"⏰ {time}' First Half (0:0-0:0)"
        ])
    
    try:
        # Get scores for each half
        first_half = scores.get('1', {})
        second_half = scores.get('2', {})
        
        # Get current total score
        current_home, current_away = map(int, score.split('-'))
        
        # Calculate scores for each 45-minute period
        if time == 'HT':
            # Get first half score
            fh_home = int(first_half.get('home', '0'))
            fh_away = int(first_half.get('away', '0'))
            time_display = f"Halftime Break ({fh_home}:0-{fh_away}:0)"
        else:
            # Calculate half scores
            if int(time.split('+')[0]) <= 45:
                # Still in first half - show current score for first half only
                fh_home, fh_away = map(int, score.split('-'))
                time_display = f"{time}' First Half ({fh_home}:0-{fh_away}:0)"
            else:
                # In second half or overtime
                # Get first half scores
                fh_home = int(first_half.get('home', '0'))
                fh_away = int(first_half.get('away', '0'))
                
                # Calculate second half scores by subtracting first half from total
                sh_home = current_home - fh_home
                sh_away = current_away - fh_away
                
                # Check if in overtime (90+ minutes)
                minutes = int(time.split('+')[0])
                if minutes > 90:
                    overtime_minutes = minutes - 90
                    time_display = f"90+{overtime_minutes}' Second Half ({fh_home}:{sh_home}-{fh_away}:{sh_away})"
                else:
                    time_display = f"{time}' Second Half ({fh_home}:{sh_home}-{fh_away}:{sh_away})"
        
        output = [
            f"⚽ {home} - {away}",
            f"📊 Score: {score}",
            f"⏰ {time_display}"
        ]
        
        return "\n".join(output)
    except Exception as e:
        return "\n".join([
            f"⚽ {home} - {away}",
            f"📊 Score: {score}",
            f"⏰ {time}' First Half (0:0-0:0)"
        ])

def is_esport(league_name):
    # Add esport league names to this list as needed
    esport_leagues = ['ePremier League', 'Virtual Bundesliga']
    return league_name in esport_leagues

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Soccer match formatting tests and live events display')
    parser.add_argument('--live', action='store_true', help='Show live events')
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        import unittest
        unittest.main(argv=['dummy'])
    elif args.live:
        show_live_soccer_events()
    else:
        # Sample match for testing format
        sample_match = {
            'league': {'name': 'Premier League'},
            'home': {'name': 'Manchester United'},
            'away': {'name': 'Liverpool'},
            'ss': '2-1',
            'timer': {'tm': '75'},
            'scores': {
                '1': {'home': '1', 'away': '1'},
                '2': {'home': '1', 'away': '0'}
            }
        }
        print("\nSample match with new format:")
        print(f"🏆 {sample_match['league']['name']}")
        print(format_soccer_match(sample_match))
