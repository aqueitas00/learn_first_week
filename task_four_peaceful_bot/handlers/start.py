from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text('Hello!',
                              reply_markup=
                              ReplyKeyboardMarkup([['/help']],
                              one_time_keyboard=True))


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/planet\n'
                              f'/next_full_moon\n'
                              f'/wordcount\n'
                              f'/cities')
