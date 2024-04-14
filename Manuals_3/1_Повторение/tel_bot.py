# Написать телеграмм бота, который будет выполнять роль таймера.
import telebot
import time
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TELEGRAM_RPG_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def starting(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Я бот - таймер!\nНачнем?')
    bot.register_next_step_handler(message, question)


def question(message: telebot.types.Message):
    if message.text == 'да':
        bot.send_message(message.chat.id, "Через сколько секунд вам написать?")
        bot.register_next_step_handler(message, check_timer)
    else:
        bot.send_message(message.chat.id, "Начнем заново!")
        starting(message)


def check_timer(message: telebot.types.Message):
    try:
        seconds = int(message.text)
        timer(message, seconds)
    except ValueError:
        bot.send_message(message.chat.id, "Введено некорректное количество секунд! Начнем заново!")
        bot.register_next_step_handler(message, question)


def timer(message: telebot.types.Message, seconds):
    time.sleep(seconds)
    bot.send_message(message.chat.id, "Дзынь-дзынь!\nЧтобы запустить будильник еще раз нажмите /start")


bot.infinity_polling()
