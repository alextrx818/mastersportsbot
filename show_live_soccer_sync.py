import os
import requests
from src.sports_format import format_soccer_match

def get_live_soccer_events():
    """Get live soccer events using synchronous requests"""
    base_url = "https://api.b365api.com/v1/events/inplay"
    token = os.getenv("B365_TOKEN")
    
    if not token:
        print("Error: B365_TOKEN environment variable not set")
        return []
    
    params = {
        "token": token,
        "sport_id": 1  # Soccer
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data.get('results', [])
    except Exception as e:
        print(f"Error fetching matches: {e}")
        return []

def main():
    matches = get_live_soccer_events()
    
    if not matches:
        print("No live matches found")
        return
        
    print(f"\nLive Soccer Matches: {len(matches)}")
    print("=" * 50)
    
    for match in matches:
        try:
            formatted_match = format_soccer_match(match)
            print(formatted_match)
            print("-" * 50)
        except Exception as e:
            print(f"Error formatting match: {e}")
            print(f"Raw match data: {match}")
            print("-" * 50)

if __name__ == "__main__":
    main()
