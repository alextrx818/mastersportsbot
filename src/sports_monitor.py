import os
import requests
import asyncio
from dotenv import load_dotenv
from loguru import logger
import sys
import signal

# Load environment variables
load_dotenv()

# Configure logging with proper encoding
logger.remove()  # Remove default handler
logger.add(
    "sports_monitor.log",
    rotation="1 day",
    encoding="utf-8",
    enqueue=True,  # Thread-safe writing
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name}:{function}:{line} - {message}"
)
logger.add(sys.stdout)  # Add stdout handler

# Sport configurations with emojis
SPORTS = {
    1: {'name': 'Soccer', 'emoji': '⚽'},
    18: {'name': 'Basketball', 'emoji': '🏀'},
    13: {'name': 'Tennis', 'emoji': '🎾'},
    91: {'name': 'Volleyball', 'emoji': '🏐'},
    17: {'name': 'Ice Hockey', 'emoji': '🏒'},
    78: {'name': 'Handball', 'emoji': '🤾'},
    16: {'name': 'Baseball', 'emoji': '⚾'},
    12: {'name': 'American Football', 'emoji': '🏈'},
    14: {'name': 'Snooker', 'emoji': '🎱'},
    15: {'name': 'Darts', 'emoji': '🎯'},
    92: {'name': 'Table Tennis', 'emoji': '🏓'},
    94: {'name': 'Badminton', 'emoji': '🏸'},
    19: {'name': 'Rugby League', 'emoji': '🏉'},
    36: {'name': 'Australian Rules', 'emoji': '🏉'},
    95: {'name': 'Beach Volleyball', 'emoji': '🏐'}
}

class SportsMonitorBot:
    def __init__(self):
        self.api_key = os.getenv('SPORTS_API_KEY')
        self.api_host = os.getenv('SPORTS_API_HOST')

    def is_esport(self, league_name):
        """Check if the league is an e-sport league"""
        esport_keywords = ['esoccer', 'esports', 'e-', 'cyber', 'ebasketball', 'etennis', 'evolleyball', 'ehockey']
        league_name = league_name.lower()
        return any(keyword in league_name for keyword in esport_keywords)

    def get_period(self, match, sport_id):
        """Get the current period of the match"""
        timer = match.get('timer', {})
        time = timer.get('tm', '0')
        
        if sport_id == 1:  # Soccer
            if not time or time == '0':
                return 'Not Started'
            time_int = int(time)
            if time_int <= 45:
                return f'{time}min 1H'
            elif time_int == 45:
                return '45+min HT'
            elif time_int <= 90:
                return f'{time}min 2H'
            elif time_int == 90:
                return '90+min'
            else:
                return 'ET' if time_int > 90 else '-'
                
        elif sport_id == 18:  # Basketball
            period = timer.get('q', '1')
            if period == '5':
                return 'OT'
            else:
                return f'Q{period}'
                
        elif sport_id == 13:  # Tennis
            score = match.get('ss', '')
            if not score:
                return '-'
            sets = score.split(',')
            current_set = len(sets)
            return f'Set {current_set}'
            
        elif sport_id == 91:  # Volleyball
            current_set = timer.get('set', '1')
            return f'Set {current_set}'
            
        elif sport_id == 17:  # Ice Hockey
            period = timer.get('p', '1')
            if period == '4':
                return 'OT'
            elif period == '5':
                return 'SO'  # Shootout
            else:
                return f'P{period}'
                
        elif sport_id == 78:  # Handball
            time_int = int(time) if time else 0
            if time_int <= 30:
                return f'{time}min 1H'
            else:
                return f'{time}min 2H'
                
        elif sport_id == 16:  # Baseball
            inning = timer.get('q', '1')
            tb = timer.get('tb', 't')  # top/bottom
            tb_text = 'Top' if tb == 't' else 'Bot'
            if inning == '10':
                return 'Extra Inn.'
            return f'{tb_text} {inning}'
            
        elif sport_id == 12:  # American Football
            quarter = timer.get('q', '1')
            if quarter == '5':
                return 'OT'
            return f'Q{quarter}'
            
        elif sport_id == 14:  # Snooker
            frame = timer.get('game', '1')
            return f'Frame {frame}'
            
        elif sport_id == 15:  # Darts
            set_info = timer.get('set', '1')
            leg = timer.get('leg', '1')
            return f'S{set_info}L{leg}'
            
        elif sport_id == 92:  # Table Tennis
            game = timer.get('game', '1')
            return f'Game {game}'
            
        elif sport_id == 94:  # Badminton
            game = timer.get('game', '1')
            return f'Game {game}'
            
        elif sport_id == 19:  # Rugby League
            time_int = int(time) if time else 0
            if time_int <= 40:
                return f'{time}min 1H'
            else:
                return f'{time}min 2H'
                
        elif sport_id == 36:  # Australian Rules
            quarter = timer.get('q', '1')
            return f'Q{quarter}'
            
        elif sport_id == 95:  # Beach Volleyball
            set_info = timer.get('set', '1')
            return f'Set {set_info}'
            
        return '-'

    def format_match(self, match, sport_id):
        """Format match with minimal essential information"""
        league = match.get('league', {}).get('name', 'Unknown League')
        home = match.get('home', {}).get('name', 'Unknown')
        away = match.get('away', {}).get('name', 'Unknown')
        score = match.get('ss', 'vs')
        timer = match.get('timer', {})
        time = timer.get('tm', '0')
        period = self.get_period(match, sport_id)
        sport_info = SPORTS.get(sport_id, {'emoji': '🎮'})
        return f"{league}\n{sport_info['emoji']} {home} {score} {away}\n⏰ {time}' ({period})\n"

    async def fetch_live_matches(self):
        """Fetch live matches from the API for all sports"""
        url = f"https://{self.api_host}/v3/events/inplay"
        all_matches = []
        
        for sport_id, sport_info in SPORTS.items():
            try:
                params = {
                    'token': self.api_key,
                    'sport_id': sport_id
                }
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    if data.get('success') == 1:
                        matches = data.get('results', [])
                        # Filter out e-sports matches
                        real_matches = [m for m in matches if not self.is_esport(m.get('league', {}).get('name', ''))]
                        if real_matches:
                            logger.info(f"\n📱 Live {sport_info['name']} Matches ({len(real_matches)} total)\n")
                            # Sort matches by time (descending)
                            real_matches.sort(key=lambda x: int(x.get('timer', {}).get('tm', 0)), reverse=True)
                            for match in real_matches:
                                logger.info(self.format_match(match, sport_id))
                            all_matches.extend(real_matches)
                        # Pause between sports to make it easier to read
                        await asyncio.sleep(2)
                    else:
                        logger.error(f"❌ API returned success = 0 for {sport_id}")
                else:
                    logger.error(f"❌ Error: {response.status_code}")
            except Exception as e:
                logger.error(f"❌ Error fetching {sport_info['name']} matches: {str(e)}")
        return all_matches

async def run_monitoring():
    bot = SportsMonitorBot()
    try:
        logger.info("Starting Sports Monitor Bot...")
        while True:
            await bot.fetch_live_matches()
            await asyncio.sleep(60)  # Wait for 60 seconds before next update
    except asyncio.CancelledError:
        logger.info("Shutting down Sports Monitor Bot...")
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt, shutting down...")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
    finally:
        logger.info("Sports Monitor Bot stopped.")

def handle_shutdown(signum, frame):
    logger.info("Received shutdown signal, cleaning up...")
    sys.exit(0)

if __name__ == "__main__":
    import signal
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)
    
    try:
        asyncio.run(run_monitoring())
    except KeyboardInterrupt:
        logger.info("Goodbye! 👋")
