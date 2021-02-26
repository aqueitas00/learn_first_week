import ephem
from datetime import datetime
from telegram import Update
from telegram.ext import CallbackContext

from task_four_peaceful_bot.handlers.utils import volatile_reply


def planet_command(update: Update, context: CallbackContext):
    if context.args:
        if len(context.args) >= 2:
            day = datetime.strptime(str(context.args[1]), '%d/%m/%Y')
        else:
            day = datetime.today().strftime("%d/%m/%Y")
        result = get_constellation(context.args[0], day)
    else:
        result = 'You need a chose the planet'

    volatile_reply(result, update, context)


def next_full_moon_command(update: Update, context: CallbackContext):
    if context.args:
        day = datetime.strptime(str(context.args[0]), '%d/%m/%Y')
    else:
        day = datetime.today().strftime('%d/%m/%Y')
    result = ephem.next_full_moon(day)

    volatile_reply(result, update, context)


def get_constellation(val, time):
    try:
        obj = getattr(ephem, val.capitalize())
        return ephem.constellation(obj(time))[1]
    except AttributeError:
        return f"{val} is not found"


