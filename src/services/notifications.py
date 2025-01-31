from twilio.rest import Client
import telegram
from ..core.config import get_settings
import logging
from typing import List

logger = logging.getLogger(__name__)
settings = get_settings()

class NotificationService:
    def __init__(self):
        self.twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.telegram_bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
        self.telegram_chats: List[int] = []  # Store subscribed chat IDs

    async def send_telegram(self, message: str):
        """Send notification via Telegram."""
        try:
            for chat_id in self.telegram_chats:
                await self.telegram_bot.send_message(
                    chat_id=chat_id,
                    text=message,
                    parse_mode='HTML'
                )
        except Exception as e:
            logger.error(f"Error sending Telegram message: {str(e)}")

    def send_sms(self, message: str, to_number: str):
        """Send notification via SMS."""
        try:
            self.twilio_client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=to_number
            )
        except Exception as e:
            logger.error(f"Error sending SMS: {str(e)}")

    async def broadcast_alert(self, message: str, notification_type: str = "all"):
        """Broadcast alert through specified channels."""
        if notification_type in ["telegram", "all"]:
            await self.send_telegram(message)
        
        if notification_type in ["sms", "all"]:
            # You would typically maintain a list of subscribed phone numbers
            # For now, we'll just log the message
            logger.info(f"Would send SMS: {message}")

    async def add_telegram_subscriber(self, chat_id: int):
        """Add a new Telegram subscriber."""
        if chat_id not in self.telegram_chats:
            self.telegram_chats.append(chat_id)
            await self.send_telegram("Successfully subscribed to sports alerts!")
