from src.core.b365api import B365API, SportID
from src.sports_format import format_soccer_match

def main():
    # Fetch live soccer events
    response = B365API.get_inplay_events(SportID.SOCCER.value)
    
    if 'results' not in response:
        print("Error fetching matches or no matches available")
        return
        
    matches = response['results']
    
    print(f"\nLive Soccer Matches: {len(matches)}")
    print("=" * 50)
    
    for match in matches:
        print(format_soccer_match(match))
        print("-" * 50)

if __name__ == "__main__":
    main()
