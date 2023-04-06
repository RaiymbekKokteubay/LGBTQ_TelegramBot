import telebot
from telebot import types
import os

bot = telebot.TeleBot('5960231197:AAH0-PBqMfKepR8cWONIvh7WFMuqZInOzu8')

@bot.message_handler(commands = ['start', 'hello'])
def welcome(message):
    bot.reply_to(message,
                 "Hi, how can I hel you? Use the following commands to interact with the bot:\n/recources - to find useful materials\n/organizations - to find organizations that hep minorities\n/hotlines - in case you need urgent help\n/mission - to find the mission of the bot")

@bot.message_handler(commands = ['recources'])
def recources(message):
    bot.reply_to(message, "")

@bot.message_handler(commands = ['organizations'])
def organizations(message):
    bot.reply_to(message,
                 "•Общественный Фонд «Адали» (Алма-Аты)\n•ОМОО «AS AKТИВ» Архивная копия от 16 мая 2020 на Wayback Machine (Усть-Каменогорск)\n•Казахстанская феминистская инициатива «Феминита» Архивная копия от 29 января 2018 на Wayback Machine\n•Инициативная группа «Alma-TQ»\n•ЛГБТ-объединение #Калейдоскоп Архивная копия от 23 августа 2019 на Wayback Machine\nЛГБТ-портал о жизни казахстанского сообщества «Kok.team Архивная копия от 24 марта 2017 на Wayback Machine»[37]")

@bot.message_handler(commands = ['hotlines'])
def hotlines(message):
    bot.reply_to(message, "")

@bot.message_handler(commands = ['mission'])
def mission(message):
    bot.reply_to(message, "According to research, the suicide rate among minorities is pressing. The bot provides help for minorities in Middle Asia")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()