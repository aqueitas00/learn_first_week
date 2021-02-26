from telegram.error import BadRequest
from telegram.ext import CallbackContext
from telegram import Update


def volatile_reply(message, update: Update, context: CallbackContext):
    if update.message:
        update.message. \
            reply_text(message, reply_to_message_id=update.message.message_id)

    elif update.message is None:
        try:
            context.bot.edit_message_text(
                text=message,
                chat_id=update.effective_chat.id,
                message_id=update.edited_message.message_id + 1,
            )
        except BadRequest:
            pass



