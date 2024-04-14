# Внедрить в телеграмм бота запись в базу данных:
# 1. id пользователя, который запустил таймер
# 2. время запуска таймера,
# 3. продолжительность таймера.
# Создать команду для вывода данных из таблицы.
import telebot
import time
import os
from dotenv import load_dotenv
import s_taper
from s_taper.consts import *
from datetime import datetime


scheme = {
    'user_id': INT,
    'timer': TEXT,
    'duration': INT
}

timers = s_taper.Taper('timers', 'data.db').create_table(scheme)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_RPG_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(['start'])
def starting(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Я бот - таймер!\nНачнем?')
    bot.register_next_step_handler(message, question)


@bot.message_handler(['stats'])
def stats(msg: telebot.types.Message):
    data = timers.read_all()
    answer = ''
    for line in data:
        answer += f'{line[0]}   {line[1]}   {line[2]}\n'
    if answer == '':
        bot.send_message(msg.chat.id, 'Нет записей в базе!')
    else:
        answer = 'id поль-ля    /          время       запуска        / длительность\n\n' + answer
        bot.send_message(msg.chat.id, answer)


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
        timers.write([message.chat.id, str(datetime.now()), seconds])
        timer(message, seconds)
    except ValueError:
        bot.send_message(message.chat.id, "Введено некорректное количество секунд! Начнем заново!")
        bot.register_next_step_handler(message, question)


def timer(message: telebot.types.Message, seconds):
    time.sleep(seconds)
    bot.send_message(message.chat.id, "Дзынь-дзынь!\nЧтобы запустить будильник еще раз нажмите /start")


bot.infinity_polling()
