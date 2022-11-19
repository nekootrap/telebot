import datetime
from urllib.parse import quote
from urllib import request
from telebot import types
from random import randint

from starters.add_bot import bot


def send_help(message: types.Message):
    msg_text = 'эщкере'
    bot.reply_to(message, msg_text)


def exo(message: types.Message):
    bot.reply_to(message, message.text)


def bread(message: types.Message):
    msg_text = 'пизда'
    bot.reply_to(message, msg_text)
    
def bread1(message: types.Message):
    msg_text = 'пидора ответ'
    bot.reply_to(message, msg_text)


def season(message: types.Message):
    seasons = {
        (12, 1, 2): 'зима',
        (3, 4, 5): 'весна',
        (6, 7, 8): 'лето',
        (9, 10, 11): 'осень',
        }

    data = message.text.split()

    if len(data) == 2:
        data = data[1]

        if data.isdigit():
            data = int(data)

            key = [el for el in seasons.keys() if data in el]
            if len(key):
                key = key[0]
            else:
                mess = 'ты тупой?'
                bot.reply_to(message, mess)
                return

            answer = seasons[key]

            bot.reply_to(message, answer)

        else:
            mess = 'ты тупой?'
            bot.reply_to(message, mess)

    elif len(data) == 1:
        month = datetime.datetime.today().month

        key = [el for el in seasons.keys() if month in el]
        key = key[0]

        answer = seasons[key]

        bot.reply_to(message, answer)

    else:
        mess = 'ты тупой?'
        bot.reply_to(message, mess)


def weather(message: types.Message):
    data = message.text.split()
    
    #хачу трахаца

    match data:
        case [command]:
            city = 'Йошкар-Ола'

        case [command, *city]:
            city = ' '.join(city)

    try:
        result = request.urlopen(f'https://wttr.in/{quote(city)}_pq_lang=ru.png')

        with open('./imgs/wttr.png', 'wb') as file_img:
            file_img.write(result.read())

        image = open('./imgs/wttr.png', 'rb')

        bot.send_photo(
            message.chat.id,
            photo=image,
            caption=f'Погода в городе <u><b>{city}</b></u>',
            parse_mode='HTML'
            #я тебя люблю
        )

    except Exception:
        bot.reply_to(message, 'произошли технические шоколадки :<')

def guess_the_number(message: types.Message) -> None:
    intt = randint(1, 11)
    
    user_number = message.text.strip('//')
    
    if user_number.isdigit():
        if user_number == str(intt):
            bot.reply_to(message, 'верно!')
        else:
            bot.reply_to(message, 'не верно(')
        
    else:
        bot.reply_to(message, 'это не число!!')
    