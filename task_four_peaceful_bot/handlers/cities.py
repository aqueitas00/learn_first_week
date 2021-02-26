import os
import pickle
import os
import random
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler
from typing import Union
from task_four_peaceful_bot.config import assets

CITIES = 1
dataset = {}
with open(f'{assets}/cities', 'rb') as file:
    dataset = pickle.load(file)


def cities_command_start(update: Update, context: CallbackContext) -> int:
    """ Start conversation #1 """
    context.chat_data['cities'] = [[], 0, False]
    update.message.reply_text('You wanna play cities? '
                              'Type a russian city.'
                              '\nRules: exceptions Й, Ь, Ы',
                              reply_markup=
                              ReplyKeyboardMarkup([['/cancel']],
                                                  one_time_keyboard=True))
    return CITIES


def cities_handle(update: Update, context: CallbackContext) \
        -> Union[ConversationHandler, int]:
    exceptions = ('й', 'Ь', 'Ы')
    values = context.chat_data['cities']
    msg = update.message.text.split(' ')[0]

    excepts = lambda m: m[-2] if m[-1] in exceptions else m[-1]
    validate = lambda m: True if m in dataset[m[0].upper()] and m not \
        in values[0] else False

    if not values[2]:
        values[2] = msg[0]

    symbol = excepts(msg).upper()

    if msg[0] == values[2] and validate(msg):
        result = random.choice(dataset[symbol])
        values[0].append(result)
        values[1] += 1
        values[2] = excepts(result).upper()

        update.message.reply_text(f'Your last symbol as {symbol}, '
                                  f'my answer is {result}\n'
                                  f'Current score: {values[1]}')
    else:
        update.message.reply_text(f'That city is not found, you are lose.\n'
                                  f'Your score: {values[1]}', reply_markup=
                                  ReplyKeyboardRemove())
        return ConversationHandler.END
    return CITIES


def cities_cancel(update: Update,
                  context: CallbackContext) -> ConversationHandler:
    update.message.reply_text(f'Conversation ended,'
                              f' your score is ',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
