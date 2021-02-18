import logging
from telegram.ext import (
    Updater,
    CommandHandler
)

from .config import TELEGRAM_PROXY_SETTINGS, TELEGRAM_BOT_TOKEN, LOG_LEVEL
from .handlers.start import start_command, help_command, planet_command

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=getattr(logging, LOG_LEVEL),
)

logger = logging.getLogger(__name__)


def mainloop():
    handlers = [
        CommandHandler("start", start_command),
        CommandHandler("help", help_command),
        CommandHandler("planet", planet_command),
    ]
    updater = Updater(
        TELEGRAM_BOT_TOKEN,
        use_context=True,
        request_kwargs=TELEGRAM_PROXY_SETTINGS,
    )
    dp = updater.dispatcher

    for handler in handlers:
        dp.add_handler(handler)

    updater.start_polling()
    updater.idle()
