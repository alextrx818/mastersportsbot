import unittest
import sys
import os
import requests
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.core.sports_format import format_volleyball_match

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
            'sport_id': 91,  # 91 is volleyball
            'skip_esports': 'true'
        }

    def get_inplay_events(self):
        """Get in-play events"""
        response = requests.get(self.endpoint, params=self.params)
        return response.json()

class TestVolleyballFormat(unittest.TestCase):
    """Test volleyball match formatting"""
    
    def setUp(self):
        """Set up test case"""
        print("\nRunning volleyball format tests...")
    
    def tearDown(self):
        """Clean up after test"""
        print("\n")
    
    def test_regular_match_format(self):
        match = {
            'home': {'name': 'USA'},
            'away': {'name': 'Brazil'},
            'ss': '2-1',
            'scores': {
                '1': {'home': '25', 'away': '23'},
                '2': {'home': '23', 'away': '25'},
                '3': {'home': '25', 'away': '20'}
            },
            'timer': {'set': '3', 'tm': '15'}
        }
        expected = "🏐 USA vs Brazil\n📊 Sets: 25-23 | 23-25 | 25-20\n⏰ Current Set: 15"
        self.assertEqual(format_volleyball_match(match), expected)
    
    def test_match_start_format(self):
        match = {
            'home': {'name': 'Italy'},
            'away': {'name': 'France'},
            'ss': '0-0',
            'scores': {},
            'timer': {'set': '1', 'tm': '0'}
        }
        expected = "🏐 Italy vs France\n📊 Sets: \n⏰ Current Set: 0"
        self.assertEqual(format_volleyball_match(match), expected)
    
    def test_missing_data_format(self):
        match = {}
        expected = "🏐 Unknown vs Unknown\n📊 Sets: \n⏰ Current Set: 0"
        self.assertEqual(format_volleyball_match(match), expected)

def show_live_volleyball_events():
    """Fetch and display all live volleyball events using the updated formatting"""
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
        print(f"\n📱 Live Volleyball Matches ({num_matches} total)\n")
        
        # Sort matches by league
        current_league = None
        
        for match in matches:
            league = match.get('league', {}).get('name', '')
            # Print league name when it changes
            if league != current_league:
                print(f"\n{league}")
                current_league = league
            
            # Format and print match
            print(format_volleyball_match(match))
            
    else:
        print("No live volleyball events found.")
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
    esport_keywords = ['esoccer', 'esports', 'e-', 'cyber', 'evolleyball']
    league_name = league_name.lower()
    return any(keyword in league_name for keyword in esport_keywords)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Volleyball match formatting tests and live events display')
    parser.add_argument('--live', action='store_true', help='Show live volleyball events')
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.live:
        show_live_volleyball_events()
    elif args.test:
        unittest.main(argv=['dummy'])
    else:
        # If no arguments provided, run both tests and live events
        unittest.main(argv=['dummy'])
        print("\nNow showing live events:")
        show_live_volleyball_events()
