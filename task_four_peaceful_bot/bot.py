import logging
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackQueryHandler,
    Filters
)
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, \
    InlineKeyboardMarkup

from .config import TELEGRAM_PROXY_SETTINGS, TELEGRAM_BOT_TOKEN, LOG_LEVEL
from .handlers.start import start_command, help_command
from .handlers.space import planet_command, next_full_moon_command
from .handlers.wordcount import wordcount_command
from .handlers.cities import cities_command_start, cities_handle, \
    cities_cancel, CITIES

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=getattr(logging, LOG_LEVEL),
)

logger = logging.getLogger(__name__)


def mainloop():
    updater = Updater(
        TELEGRAM_BOT_TOKEN,
        use_context=True,
        request_kwargs=TELEGRAM_PROXY_SETTINGS,
    )
    dp = updater.dispatcher

    handlers = [
        CommandHandler("start", start_command),
        CommandHandler("help", help_command),
        CommandHandler("planet", planet_command),
        CommandHandler("next_full_moon", next_full_moon_command),
        CommandHandler("wordcount", wordcount_command),
        ConversationHandler(
            entry_points=[CommandHandler('cities', cities_command_start)],
            states={
                CITIES: [MessageHandler(Filters.text & ~Filters.command,
                                        cities_handle)]
            },
            fallbacks=[MessageHandler(Filters.command, cities_cancel)]
        )
    ]

    for handler in handlers:
        dp.add_handler(handler)

    updater.start_polling()
    updater.idle()
