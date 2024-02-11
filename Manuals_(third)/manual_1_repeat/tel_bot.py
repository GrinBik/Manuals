import telebot
import time
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TELEGRAM_RPG_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def starting(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Я бот - таймер!')
    question(message)


def question(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Через сколько секунд вам написать?")
    bot.register_next_step_handler(message, check_timer)


def check_timer(message: telebot.types.Message):
    try:
        seconds = int(message.text)
        timer(message, seconds)
    except ValueError:
        bot.send_message(message.chat.id, "Введено некорректное количество секунд! Начнем заново!")
        question(message)


def timer(message: telebot.types.Message, seconds):
    time.sleep(seconds)
    bot.send_message(message.chat.id, "Дзынь-дзынь!\nЧтобы запустить будильник еще раз нажмите /start")

bot.infinity_polling()
