from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)
import telebot
from telebot import types

from time import sleep


bot = Bot(token='2675221255:BHIekrkhitibolw4i85oi6itjiffdhow43')
dp = Dispatcher(bot)

# language selection
button1 = KeyboardButton('Organizations')  
button2 = KeyboardButton('Hotlines')
button3 = KeyboardButton('Recources')
buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3)


# sends welcome message after start
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Hello! How can I help you?', reply_markup = buttons)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('text describing mission')

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == buttons["back"]:
        welcome(message)
    elif message.text == buttons["Organizations"]:
        bot.send_message(message, "text here")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton(buttons["back"]),)
    elif message.text == buttons["Hotlines"]:
        bot.send_message(message, "text here")
        markup.add(
            types.KeyboardButton(buttons["back"]),)
    elif message.text == buttons["Recources"]:
        bot.send_message(message, "text here")
        markup.add(
            types.KeyboardButton(buttons["back"]),)

executor.start_polling(dp)