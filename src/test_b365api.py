import asyncio
from core.b365api import B365API, SportID

def is_esport(event):
    """Check if an event is an esport"""
    league_name = event.get('league', {}).get('name', '').lower()
    return any(x in league_name for x in ['esport', 'esoccer', 'ebasketball', 'evirtual'])

async def test_inplay():
    """Test getting in-play events for all sports"""
    total_events = 0
    print("\nLive Events by Sport (excluding esports):")
    print("=" * 50)
    
    # Test all sports
    for sport in SportID:
        try:
            result = await B365API.get_inplay_events(sport.value)
            # Filter out esports events
            real_events = [event for event in result.get('results', []) 
                         if not is_esport(event)]
            event_count = len(real_events)
            total_events += event_count
            
            if event_count > 0:
                print(f"{sport.name:<20} ({sport.value:>3}): {event_count:>3} live events")
                # Show first real sport event as example
                first_event = real_events[0]
                if first_event:
                    home = first_event.get('home', {}).get('name', 'Unknown')
                    away = first_event.get('away', {}).get('name', 'Unknown')
                    score = first_event.get('ss', 'No score')
                    league = first_event.get('league', {}).get('name', 'Unknown League')
                    print(f"   └─ Example: [{league}] {home} vs {away} ({score})")
            
        except Exception as e:
            print(f"Error getting {sport.name} events: {str(e)}")
    
    print("\n" + "=" * 50)
    print(f"Total Live Events (excluding esports): {total_events}")

if __name__ == "__main__":
    print("Testing B365 API - Live Events")
    asyncio.run(test_inplay())
