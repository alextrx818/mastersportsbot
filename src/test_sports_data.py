import asyncio
from core.sports_data import SportsData
from core.logging_config import LogConfig

# Setup logging
logger = LogConfig.get_component_logger("sports_test")

async def test_sports_data():
    """Test sports data fetching and formatting"""
    sports_handler = SportsData()
    
    print("Testing sports data fetching...")
    matches = await sports_handler.test_all_sports()
    
    for match_info in matches:
        print(match_info)

if __name__ == "__main__":
    # Run the test
    asyncio.run(test_sports_data())
