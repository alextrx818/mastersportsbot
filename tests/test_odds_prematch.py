#!/usr/bin/env python3
import requests
import json
import sys

class B365APISync:
    """API client for fetching prematch odds"""
    def __init__(self):
        self.base_url = "https://api.b365api.com/v1"  # Changed to v1
        self.token = "180846-0nb22aL4DeG73U"

    def get_live_events(self):
        """Fetch current live soccer events"""
        endpoint = f"{self.base_url}/events/inplay"
        params = {
            'token': self.token,
            'sport_id': 1,  # 1 is for soccer
            'skip_esports': 'true'
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching live events: {e}")
            return None

    def get_upcoming_events(self, event_id=None):
        """Fetch upcoming events from Bet365"""
        endpoint = f"{self.base_url}/bet365/upcoming"
        params = {
            'token': self.token,
            'sport_id': 1
        }
        if event_id:
            params['event_id'] = event_id
            
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching upcoming events: {e}")
            return None

    def get_prematch_odds(self, event_id):
        """Fetch prematch odds for soccer events"""
        endpoint = f"{self.base_url}/bet365/start_sp"  # Using the correct endpoint
        params = {
            'token': self.token,
            'event_id': event_id
        }
            
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching prematch odds: {e}")
            return None

def show_live_events_prematch_odds():
    """Display prematch odds for current live soccer matches"""
    api = B365APISync()
    
    # First get live events
    print("\nFetching live soccer events...")
    live_data = api.get_live_events()
    
    if not live_data or not live_data.get('results'):
        print("No live events found")
        return
        
    live_events = live_data['results']
    print(f"\nFound {len(live_events)} live soccer events")
    
    # Now get prematch odds for each live event
    for event in live_events:
        try:
            event_id = event.get('id')
            home = event.get('home', {}).get('name', 'Unknown')
            away = event.get('away', {}).get('name', 'Unknown')
            league = event.get('league', {}).get('name', 'Unknown League')
            score = event.get('ss', 'No score')
            
            print(f"\n{'='*60}")
            print(f"LIVE MATCH: {home} vs {away}")
            print(f"Current Score: {score}")
            print(f"League: {league}")
            print(f"Event ID: {event_id}")
            
            # First check if this event exists in upcoming events
            print("\nChecking Bet365 upcoming events...")
            upcoming_data = api.get_upcoming_events(event_id)
            
            if not upcoming_data or not upcoming_data.get('results'):
                print("Match not found in Bet365 upcoming events")
                continue
            
            # Get prematch odds for this event
            print("Fetching prematch odds...")
            odds_data = api.get_prematch_odds(event_id)
            
            if not odds_data or not odds_data.get('results'):
                print("No prematch odds found for this match")
                continue
                
            # Display the odds
            results = odds_data.get('results', [])
            if results:
                print("\nPrematch Odds:")
                for market in results:
                    name = market.get('name', 'Unknown Market')
                    odds = market.get('odds', {})
                    print(f"\n  {name}:")
                    for selection, price in odds.items():
                        print(f"    {selection}: {price}")
            else:
                print("No odds markets found")
                
        except Exception as e:
            print(f"Error processing event: {e}")
            continue
            
        print(f"{'='*60}\n")

if __name__ == '__main__':
    show_live_events_prematch_odds()
