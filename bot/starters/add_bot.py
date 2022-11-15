import telebot
import logging
import tomllib


with open('./config.toml', 'rb') as config:
    config = tomllib.load(config)

TOKEN = config['bot_settings']['key']

telebot.logger.setLevel(logging.INFO)
logger = telebot.logger

bot = telebot.TeleBot(TOKEN)