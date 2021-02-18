from telegram import Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext
import ephem
import datetime


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("start")


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("help")


def planet_command(update: Update, context: CallbackContext):
    if len(context.args) >= 2:
        day = str(context.args[1])
    else:
        day = datetime.date.today().strftime("%d/%m/%Y")
    result = get_constellation(context.args[0], day)

    if update.message:
        update.message.\
            reply_text(result, reply_to_message_id=update.message.message_id)

    elif update.message is None:
        print(update.edited_message)

        try:
            context.bot.editMessageText(
                text=result,
                chat_id=update.effective_chat.id,
                message_id=update.edited_message.message_id + 1,
            )
        except BadRequest:
            pass


def get_constellation(val, time):
    try:
        obj = getattr(ephem, val.capitalize())
        return ephem.constellation(obj(time))
    except AttributeError:
        return f"{val} is not found"
