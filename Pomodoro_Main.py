#!/usr/bin/env python3
from email import message
import os
import telebot
from telebot import types
import nltk
from dotenv import load_dotenv
from nltk.tokenize import sent_tokenize, word_tokenize

load_dotenv() # pulls .env variables

# set API key and activate bot
TOKEN = "1919206158:AAGnh3XIc24QyS-iKzfS7A8SO77erHmIwWk"
# API_KEY = os.getenv("1919206158:AAGnh3XIc24QyS-iKzfS7A8SO77erHmIwWk", default = 'No API key exists')
bot = telebot.TeleBot(TOKEN, parse_mode=None)

"""
# Natural Language Processing

example_string = 
... Muad'Dib learned rapidly because his first training was in how to learn.
... And the first lesson of all was the basic trust that he could learn.
... It's shocking to find how many people do not believe they can learn,
... and how many more believe learning to be difficult.

example_list = sent_tokenize(example_string)
"""

# Message Handers
# message handlers : non-reply commands
@bot.message_handler(func=lambda message: message.text == "hi")
def send_welcome(m):
    bot.send_message(m.chat.id, "Hello!")

# message handlers : reply-to commands
@bot.message_handler(commands=['help'])
def send_command(message):
    bot.reply_to(message, "The commands you can use are: \n \
    /help \
    /pomodoro \
    /testing123")

@bot.message_handler(commands = ['pomodoro'])
def bot_command(m):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('status')
    itembtn2 = types.KeyboardButton('start')
    itembtn3 = types.KeyboardButton('end')
    itembtn4 = types.KeyboardButton('break')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(m.chat.id, "Choose one command:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'status')
def get_status(m):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(m.chat.id, "Current status:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'start')
def get_status(m):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(m.chat.id, "Current status:", reply_markup=markup)
        


bot.infinity_polling()