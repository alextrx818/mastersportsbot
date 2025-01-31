import asyncio
import os
from services.odds_api_client import OddsApiClient
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_api():
    api_key = "180846-RVi16IBGld4Pvr"  # In production, get this from environment variables
    
    async with OddsApiClient(api_key) as client:
        # Test getting available sports
        logger.info("Fetching available sports...")
        sports = await client.get_sports()
        if sports:
            logger.info(f"Found {len(sports)} sports")
            # Print first sport as example
            logger.info(f"Example sport: {sports[0]}")

        # Test getting odds for NBA
        logger.info("\nFetching NBA odds...")
        nba_odds = await client.get_odds('basketball_nba')
        if nba_odds:
            logger.info(f"Found odds for {len(nba_odds)} NBA games")
            # Print first game as example
            if nba_odds:
                logger.info(f"Example game odds: {nba_odds[0]}")

if __name__ == "__main__":
    asyncio.run(test_api())
