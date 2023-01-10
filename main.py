import telebot
from telebot import types

bot = telebot.TeleBot('5960231197:AAEtytP6APVeJJ0OBdiODy5FImnSY2FDWik')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hey, Daddy! Help me! I am stuck at Telegram")

bot.polling(none_stop=True)