import asyncio
from datetime import datetime
from typing import Dict, List
import logging
from sqlalchemy.orm import Session
from ..core.config import get_settings
from ..models.base import SessionLocal
from ..models.sports import Game, Alert
from .sports_api import SportsAPI
from .notifications import NotificationService

logger = logging.getLogger(__name__)
settings = get_settings()

class SportsMonitor:
    def __init__(self):
        self.notification_service = NotificationService()
        self.monitored_sports = ["NBA", "NFL", "MLB", "NHL"]
        self.running = False

    async def start_monitoring(self):
        """Start the monitoring process."""
        self.running = True
        while self.running:
            try:
                async with SportsAPI() as api:
                    for sport in self.monitored_sports:
                        await self.monitor_sport(sport, api)
                await asyncio.sleep(settings.MONITOR_INTERVAL)
            except Exception as e:
                logger.error(f"Error in monitoring loop: {str(e)}")
                await asyncio.sleep(10)  # Short delay before retry

    async def monitor_sport(self, sport: str, api: SportsAPI):
        """Monitor games for a specific sport."""
        games = await api.get_live_games(sport)
        if not games:
            return

        db = SessionLocal()
        try:
            for game_data in games:
                await self.process_game(game_data, db, api)
        finally:
            db.close()

    async def process_game(self, game_data: Dict, db: Session, api: SportsAPI):
        """Process updates for a single game."""
        game = self._update_or_create_game(game_data, db)
        
        # Check for significant changes
        if self._check_score_change(game, game_data):
            alert = Alert(
                game_id=game.id,
                alert_type="score_change",
                message=f"Score update: {game.home_team} {game_data['home_score']} - {game_data['away_score']} {game.away_team}"
            )
            db.add(alert)
        
        # Update odds and check for significant changes
        odds_data = await api.get_game_odds(game_data['game_id'])
        if odds_data and self._check_odds_change(game, odds_data):
            alert = Alert(
                game_id=game.id,
                alert_type="odds_change",
                message=f"Significant odds change for {game.home_team} vs {game.away_team}"
            )
            db.add(alert)
        
        db.commit()

    def _update_or_create_game(self, game_data: Dict, db: Session) -> Game:
        """Update or create a game record."""
        game = db.query(Game).filter(Game.id == game_data['game_id']).first()
        if not game:
            game = Game(
                id=game_data['game_id'],
                sport=game_data['sport'],
                league=game_data['league'],
                home_team=game_data['home_team'],
                away_team=game_data['away_team']
            )
            db.add(game)
        
        game.home_score = game_data['home_score']
        game.away_score = game_data['away_score']
        game.status = game_data['status']
        game.last_updated = datetime.utcnow()
        return game

    def _check_score_change(self, game: Game, new_data: Dict) -> bool:
        """Check if there's a significant score change."""
        return (game.home_score != new_data['home_score'] or 
                game.away_score != new_data['away_score'])

    def _check_odds_change(self, game: Game, new_odds: Dict) -> bool:
        """Check if there's a significant odds change."""
        if not game.odds:
            return False
        
        threshold = settings.ALERT_THRESHOLD
        old_odds = game.odds
        return abs(float(new_odds['money_line']) - float(old_odds['money_line'])) > threshold

monitor = SportsMonitor()
