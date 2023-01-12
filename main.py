import telebot
from telebot import types
from Constants import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commmands = ["recources"])
def send_resources(message):
    bot.reply_to(message, "here are some links")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btns = types.KeyboardButton("/back")
    markup.add(btns)

@bot.message_handler(commmands = ["organizations"])
def send_organizations(message):
    bot.reply_to(message, "here are some organizations")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btns = types.KeyboardButton("/back")
    markup.add(btns)

@bot.message_handler(commmands = ["hotlines"])
def send_hotlines(message):
    bot.reply_to(message, "here are some hotlines")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btns = types.KeyboardButton("/back")
    markup.add(btns)

@bot.message_handler(commmands = ["back"])
shto s etim delat??
    
@bot.message_handler(commands=["start!"])
def welcome(message):
    bot.reply_to(message, "How can I help you?")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("/recources")
    btn2 = types.KeyboardButton("/organizations")
    btn3 = types.KeyboardButton("/hotlines")
    markup.add(btn1, btn2, btn3)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Hey! Press the button to start!")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btns = types.KeyboardButton("/start!")
    markup.add(btns)

bot.polling()