from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # Sports API
    SPORTS_API_KEY: str

    # Telegram
    TELEGRAM_BOT_TOKEN: str

    # Twilio
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_PHONE_NUMBER: str

    # Monitoring Settings
    MONITOR_INTERVAL: int = 60  # seconds
    ALERT_THRESHOLD: float = 0.15  # 15% change threshold

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
