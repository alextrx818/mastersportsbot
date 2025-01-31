import asyncio
from core.api_client import B365Client
from core.api_endpoints import SportID
from core.logging_config import LogConfig

logger = LogConfig.get_component_logger("test_endpoints")

async def test_endpoints():
    """Test various API endpoints"""
    client = B365Client()
    
    try:
        # 1. Get sports
        print("\n1. Testing get_sports()...")
        sports = await client.get_sports()
        print(f"✅ Sports retrieved: {sports}")
        
        # 2. Get leagues for basketball
        print("\n2. Testing get_leagues()...")
        leagues = await client.get_leagues(SportID.BASKETBALL.value)
        print(f"✅ Basketball leagues retrieved: {leagues}")
        
        # 3. Get upcoming basketball events
        print("\n3. Testing get_upcoming_events()...")
        upcoming = await client.get_upcoming_events(SportID.BASKETBALL.value)
        print(f"✅ Upcoming basketball events retrieved: {upcoming}")
        
        # 4. Get live events
        print("\n4. Testing get_live_events()...")
        live = await client.get_live_events(SportID.BASKETBALL.value)
        print(f"✅ Live basketball events retrieved: {live}")
        
        # If we have an event, test more endpoints
        if upcoming.get('results'):
            event_id = upcoming['results'][0]['id']
            
            # 5. Get event odds
            print("\n5. Testing get_event_odds()...")
            odds = await client.get_event_odds(event_id)
            print(f"✅ Event odds retrieved: {odds}")
            
            # 6. Get event stats
            print("\n6. Testing get_event_stats()...")
            stats = await client.get_event_stats(event_id)
            print(f"✅ Event stats retrieved: {stats}")
    
    except Exception as e:
        logger.error(f"Error testing endpoints: {str(e)}")
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("Testing B365 API Endpoints...")
    asyncio.run(test_endpoints())
