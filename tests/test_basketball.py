import unittest
import sys
import os
import requests
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.core.sports_format import format_basketball_match

class B365APISync:
    """Synchronous version of B365API for testing"""
    def __init__(self):
        """Initialize API client"""
        self.base_url = "https://api.b365api.com/v1"
        self.token = "180846-0nb22aL4DeG73U"  # Using same token as b365api.py
        if not self.token:
            raise ValueError("B365_TOKEN environment variable not set")

    @property
    def endpoint(self):
        """Get API endpoint"""
        return f"{self.base_url}/events/inplay"
    
    @property
    def params(self):
        """Get API parameters"""
        return {
            'token': self.token,
            'sport_id': 18,  # 18 is basketball
            'skip_esports': 'true'
        }
    
    def get_inplay_events(self):
        """Get in-play events"""
        response = requests.get(self.endpoint, params=self.params)
        return response.json()

class TestBasketballFormat(unittest.TestCase):
    """Test basketball match formatting"""
    
    def setUp(self):
        """Set up test case"""
        print("\nRunning basketball format tests...")
    
    def tearDown(self):
        """Clean up after test"""
        pass
    
    def test_regular_game_format(self):
        match = {
            'home': {'name': 'Lakers'},
            'away': {'name': 'Celtics'},
            'ss': '85-82',
            'timer': {'q': '3', 'tm': '8'},
            'scores': {
                '1': {'home': '25', 'away': '22'},
                '2': {'home': '30', 'away': '28'},
                '3': {'home': '30', 'away': '32'}
            }
        }
        expected = "🏀 Lakers vs Celtics\n⏰ 8' Q3 (85-82)\n📊 Q1:25-22 | Q2:30-28 | Q3:30-32\n"
        self.assertEqual(format_basketball_match(match), expected)
    
    def test_game_start_format(self):
        match = {
            'home': {'name': 'Warriors'},
            'away': {'name': 'Nets'},
            'ss': '0-0',
            'timer': {'q': '1', 'tm': '12'},
            'scores': {}
        }
        expected = "🏀 Warriors vs Nets\n⏰ 12' Q1 (0-0)\n📊 \n"
        self.assertEqual(format_basketball_match(match), expected)
    
    def test_missing_data_format(self):
        match = {}
        expected = "🏀 Unknown vs Unknown\n⏰ 0' Q1 (0-0)\n📊 \n"
        self.assertEqual(format_basketball_match(match), expected)

def show_live_basketball_events():
    """Fetch and display all live basketball events using the updated formatting"""
    print("Fetching data from API...")
    start_time = time.time()
    
    # Fetch live events
    api = B365APISync()
    api_start = time.time()
    events = api.get_inplay_events()
    api_time = time.time() - api_start
    print(f"Fetching from: {api.endpoint} with params: {api.params}")
    print(f"Response status: {events.get('success')}")
    print(f"API fetch took: {api_time:.2f} seconds\n")

    # Process data
    process_start = time.time()
    matches = []
    if events.get('results'):
        for event in events['results']:
            matches.append(event)
    matches.sort(key=lambda x: x.get('league', {}).get('name', ''))
    process_time = time.time() - process_start
    
    print("Processing matches...\n")
    
    # Format and display
    display_start = time.time()
    if matches:
        num_matches = len(matches)
        print(f"\n📱 Live Basketball Matches ({num_matches} total)\n")
        
        # Sort matches by league
        current_league = None
        
        for match in matches:
            league = match.get('league', {}).get('name', '')
            # Print league name when it changes
            if league != current_league:
                print(f"\n{league}")
                current_league = league
            
            # Format and print match
            print(format_basketball_match(match))
            
    else:
        print("No live basketball events found.")
    display_time = time.time() - display_start
    
    total_time = time.time() - start_time
    print("\nTiming:")
    print(f"API fetch: {api_time:.2f}s")
    print(f"Data processing: {process_time:.2f}s")
    print(f"Formatting and display: {display_time:.2f}s")
    print(f"Total time: {total_time:.2f}s")
    print(f"Live events found: {len(matches)}")

def is_esport(league_name):
    """Check if the league is an e-sport league"""
    esport_keywords = ['esoccer', 'esports', 'e-', 'cyber', 'ebasketball']
    league_name = league_name.lower()
    return any(keyword in league_name for keyword in esport_keywords)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Basketball match formatting tests and live events display')
    parser.add_argument('--live', action='store_true', help='Show live basketball events')
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.live:
        show_live_basketball_events()
    elif args.test:
        unittest.main(argv=['dummy'])
    else:
        # If no arguments provided, run both tests and live events
        unittest.main(argv=['dummy'])
        print("\nNow showing live events:")
        show_live_basketball_events()
