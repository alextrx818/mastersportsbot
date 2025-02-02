import requests
from datetime import datetime

# Your API token
API_TOKEN = '180846-0nb22aL4DeG73U'

def get_live_events(api_token, sport_id=1):
    """
    Retrieve live events for a given sport.
    Args:
        api_token (str): API authentication token
        sport_id (int): Sport ID (default: 1 for soccer)
    Returns:
        dict: JSON response containing live events
    """
    inplay_url = f'https://api.b365api.com/v3/events/inplay'
    params = {
        'sport_id': sport_id,
        'token': api_token,
        'skip_esports': 'true',
        'stats': 'true'
    }
    
    try:
        print(f"\nFetching live events from: {inplay_url}")
        print(f"Parameters: {params}")
        response = requests.get(inplay_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"Live events API response status: {data.get('success')}")
        if not data.get('success'):
            print(f"Error message: {data.get('error', 'No error message')}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching live events: {e}")
        return None

def get_prematch_odds(api_token, event_id):
    """
    Retrieve pre-match odds for a specific event.
    Args:
        api_token (str): API authentication token
        event_id (str): Event ID/FI from live events
    Returns:
        dict: JSON response containing pre-match odds
    """
    prematch_url = f'https://api.b365api.com/v3/bet365/prematch'
    params = {
        'token': api_token,
        'FI': event_id
    }
    
    try:
        print(f"\nFetching pre-match odds for event {event_id} from: {prematch_url}")
        print(f"Parameters: {params}")
        response = requests.get(prematch_url, params=params, timeout=10)
        
        # Print the raw response for debugging
        print(f"Response status code: {response.status_code}")
        try:
            data = response.json()
            print(f"Response data: {data}")
        except:
            print(f"Raw response text: {response.text}")
            
        response.raise_for_status()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pre-match odds: {e}")
        if hasattr(e.response, 'text'):
            print(f"Error response text: {e.response.text}")
        return None

def get_live_odds(api_token, event_id):
    """
    Retrieve live odds for a specific event.
    Args:
        api_token (str): API authentication token
        event_id (str): Event ID/FI from live events
    Returns:
        dict: JSON response containing live odds
    """
    live_url = f'https://api.b365api.com/v3/bet365/event'
    params = {
        'token': api_token,
        'FI': event_id,
        'stats': 'true',
        'odds': 'true'
    }
    
    try:
        print(f"\nFetching live odds for event {event_id} from: {live_url}")
        print(f"Parameters: {params}")
        response = requests.get(live_url, params=params, timeout=10)
        
        # Print the raw response for debugging
        print(f"Response status code: {response.status_code}")
        try:
            data = response.json()
            print(f"Response data: {data}")
        except:
            print(f"Raw response text: {response.text}")
            
        response.raise_for_status()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching live odds: {e}")
        if hasattr(e.response, 'text'):
            print(f"Error response text: {e.response.text}")
        return None

def format_time(timestamp):
    """Convert timestamp to readable time format."""
    try:
        if str(timestamp).isdigit():
            return datetime.fromtimestamp(int(timestamp)).strftime('%H:%M')
    except:
        pass
    return 'Unknown Time'

def display_event_info(event, live_odds=None, prematch_odds=None):
    """Display formatted event information and odds."""
    # Extract basic event information
    league = event.get('league', {}).get('name', 'Unknown League')
    home = event.get('home', {}).get('name', 'Unknown Home')
    away = event.get('away', {}).get('name', 'Unknown Away')
    score = event.get('ss', '0-0')
    time = format_time(event.get('time', ''))
    
    # Print event details
    print(f"\n {league}\n")
    print(f"⚽ {home} - {away}")
    print(f"📊 Score: {score}")
    print(f"⏰ {time}")
    
    # Print live odds if available
    print("-" * 40 + " LIVE ODDS " + "-" * 40)
    if live_odds and live_odds.get('results'):
        print("\n Money Line (1X2) - Live Odds:")
        # Process live odds here
        print("Live odds data available but processing not implemented")
    else:
        print("\n Money Line (1X2) - Live Odds:")
        print("No live odds available")
    
    # Print pre-match odds if available
    print("\n" + "-" * 40 + " PREMATCH ODDS " + "-" * 39)
    if prematch_odds and prematch_odds.get('results'):
        print("\n Money Line (1X2) - Pre-match Odds:")
        # Process pre-match odds here
        print("Pre-match odds data available but processing not implemented")
    else:
        print("\n Money Line (1X2) - Pre-match Odds:")
        print("No pre-match odds available")
    
    print("\n" + "=" * 80)

def main():
    """Main function to fetch and display live soccer events and odds."""
    try:
        # Get live events
        print("\nFetching live soccer events...")
        live_events = get_live_events(API_TOKEN)
        
        if not live_events or not live_events.get('results'):
            print("No live events found.")
            return
        
        events = live_events['results']
        if isinstance(events, list) and len(events) > 0 and isinstance(events[0], list):
            events = events[0]
        
        print(f"\nFound {len(events)} live events")
        
        # Process each event
        for event in events:
            if not isinstance(event, dict):
                continue
                
            event_id = event.get('id')
            if not event_id:
                continue
            
            try:
                # Get live odds
                live_odds = get_live_odds(API_TOKEN, event_id)
                
                # Get pre-match odds
                prematch_odds = get_prematch_odds(API_TOKEN, event_id)
                
                # Display event information and odds
                display_event_info(event, live_odds, prematch_odds)
                
            except Exception as e:
                print(f"Error processing event {event_id}: {str(e)}")
                continue

    except Exception as e:
        print(f"An error occurred in main: {e}")

if __name__ == "__main__":
    main()
