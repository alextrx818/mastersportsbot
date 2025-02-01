import unittest
import sys
import os
import time
import requests
from datetime import datetime, timezone, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class B365APISync:
    """Synchronous version of B365API for testing"""
    def __init__(self):
        self.base_url = "https://api.b365api.com/v1"
        self.token = "180846-0nb22aL4DeG73U"
        if not self.token:
            raise ValueError("B365_TOKEN environment variable not set")

    def get_inplay_events(self, sport_id):
        """
        Get live events for a specific sport
        sport_id: The B365 sport ID (e.g., 1=soccer, 18=basketball, 91=volleyball)
        """
        endpoint = f"{self.base_url}/events/inplay"
        params = {
            'token': self.token,
            'sport_id': sport_id,
            'skip_esports': 'true'
        }
        print(f"Fetching from: {endpoint} with params: {params}")
        response = requests.get(endpoint, params=params)
        print(f"Response status: {response.status_code}")
        if response.status_code != 200:
            print(f"Error response: {response.text}")
            return None
        return response.json()

class TestEventFormat(unittest.TestCase):
    """Base test class for event formatting"""
    
    def test_prematch(self):
        """Test formatting a match that hasn't started"""
        match = {
            'home': {'name': 'Team A'},
            'away': {'name': 'Team B'},
            'timer': {'tm': '0'},
            'scores': {}
        }
        expected = self.get_expected_prematch_format()
        self.assertEqual(self.format_match(match), expected)

    def test_missing_data(self):
        """Test handling missing or incomplete data"""
        match = {
            'home': {},
            'away': {},
            'timer': {},
            'scores': {}
        }
        result = self.format_match(match)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_score_format(self):
        """Test score formatting"""
        match = {
            'home': {'name': 'Team A'},
            'away': {'name': 'Team B'},
            'ss': '10-5',
            'timer': {'tm': '15'},
            'scores': {'1': {'home': '10', 'away': '5'}}
        }
        result = self.format_match(match)
        self.assertIn('10-5', result)

    def format_match(self, match):
        """Override this method in sport-specific test files"""
        raise NotImplementedError()

    def get_expected_prematch_format(self):
        """Override this method in sport-specific test files"""
        raise NotImplementedError()

def show_live_events(sport_id, sport_emoji, format_match):
    """
    Generic function to show live events for any sport
    
    Args:
        sport_id: The B365 sport ID
        sport_emoji: Emoji to use for this sport (e.g., ⚽, 🏀, 🏐)
        format_match: Function to format a single match
    """
    start_time = time.time()
    
    api = B365APISync()
    try:
        print("Fetching data from API...")
        fetch_start = time.time()
        data = api.get_inplay_events(sport_id)
        fetch_time = time.time() - fetch_start
        print(f"API fetch took: {fetch_time:.2f} seconds")
        
        if not data or 'results' not in data:
            print("No live events found")
            return

        print("\nProcessing matches...")
        process_start = time.time()
        matches = data['results']
        matches = [m for m in matches if not is_esport(m.get('league', {}).get('name', ''))]
        
        print(f"\nFound {len(matches)} live events:\n")
        
        # Sort matches by league
        matches.sort(key=lambda x: x.get('league', {}).get('name', ''))
        current_league = None
        
        format_start = time.time()
        for match in matches:
            league = match.get('league', {}).get('name', '')
            # Print league name when it changes
            if league != current_league:
                if current_league is not None:
                    print("----------------------------------------")
                print(f"🏆 {league}")
                current_league = league
            
            # Format and print match
            print(format_match(match))
        
        format_time = time.time() - format_start
        process_time = time.time() - process_start
        total_time = time.time() - start_time
        
        # Get current time in EST
        utc_now = datetime.now(timezone.utc)
        est_tz = timezone(timedelta(hours=-5))  # EST is UTC-5
        est_now = utc_now.astimezone(est_tz)
        est_time = est_now.strftime("%I:%M:%S %p EST")
        
        print(f"\nTiming:")
        print(f"Current Time: {est_time}")
        print(f"API fetch: {fetch_time:.2f}s")
        print(f"Data processing: {process_time-format_time:.2f}s")
        print(f"Formatting and display: {format_time:.2f}s")
        print(f"Total time: {total_time:.2f}s")
        print(f"Live events found: {len(matches)}")
            
    except Exception as e:
        print(f"Error fetching events: {str(e)}")

def is_esport(league_name):
    """Filter out esports events"""
    esport_leagues = ['ePremier League', 'Virtual Bundesliga', 'ESports']
    return any(esport in league_name for esport in esport_leagues)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Event formatting tests and live events display')
    parser.add_argument('--live', action='store_true', help='Show live events')
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        unittest.main(argv=['dummy'])
    elif args.live:
        print("This is a template file. Use a sport-specific test file instead.")
    else:
        print("This is a template file. Use a sport-specific test file instead.")
