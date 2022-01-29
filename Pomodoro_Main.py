#!/usr/bin/env python3
import os
import telebot
import nltk
from dotenv import load_dotenv
from nltk.tokenize import sent_tokenize, word_tokenize

load_dotenv() # pulls .env variables

# set API key and activate bot
API_KEY = os.getenv('API_KEY', default = 'No API key exists')
bot = telebot.TeleBot(API_KEY, parse_mode=None)

# Natural Language Processing

example_string = """
... Muad'Dib learned rapidly because his first training was in how to learn.
... And the first lesson of all was the basic trust that he could learn.
... It's shocking to find how many people do not believe they can learn,
... and how many more believe learning to be difficult."""

example_list = sent_tokenize(example_string)

# Message Handers
# message handlers : non-reply commands
@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    bot.send_message(m.chat.id, "Waddup")

# message handlers : reply-to commands
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "The commands you can use are: \n \
    /greet \
    /help \
    /testing123")










bot.polling()