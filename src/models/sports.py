from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from .base import Base
from datetime import datetime

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    sport = Column(String, index=True)
    league = Column(String, index=True)
    home_team = Column(String)
    away_team = Column(String)
    home_score = Column(Integer)
    away_score = Column(Integer)
    odds = Column(JSON)
    status = Column(String)
    start_time = Column(DateTime)
    last_updated = Column(DateTime, default=datetime.utcnow)

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, index=True)
    alert_type = Column(String)  # score_change, odds_change, etc.
    message = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    sent = Column(Boolean, default=False)
    notification_type = Column(String)  # sms, telegram, etc.
