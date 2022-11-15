from telebot import types

from starters.add_bot import bot


def send_help(message: types.Message):
    msg_text = 'эщкере'
    bot.reply_to(message, msg_text)


def exo(message: types.Message):
    bot.reply_to(message, message.text)
