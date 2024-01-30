# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('7096447091:AAEX6cc3WC9fVBtN_aEkRjBJHBw0IcoVm1A')
#
# @bot.message_handlers(commands=(['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, 'Howdy, how are you doing?')
#
# @bot.message_handlers(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
# bot.infinity_polling()


import telebot

bot = telebot.TeleBot("7096447091:AAEX6cc3WC9fVBtN_aEkRjBJHBw0IcoVm1A")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()