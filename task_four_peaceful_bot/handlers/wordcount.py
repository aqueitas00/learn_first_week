import re
from telegram import Update
from telegram.ext import CallbackContext

from .utils import volatile_reply


def wordcount_command(update: Update, context: CallbackContext):
    args = context.args
    args[:] = [val for val in args if
               (lambda x: True if
                re.match(r'[А-я]|[A-zА-яёЁ]\w', x) else False)(val)]
    print(args)
    volatile_reply(make_response(len(args)), update, context)


def make_response(count: int) -> str:
    if count % 10 == 1:
        return f'{count} слово'
    elif count % 10 in (2, 3, 4):
        return f'{count} слова'
    elif count % 10 in (5, 6, 7, 8, 9, 0):
        return f'{count} слов'
