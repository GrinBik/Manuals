# ДЗ
# Просмотри все данные, которые есть в msg, и найди там атрибут с временем отправки сообщения. Выведи его в консоль.
# Используя модуль datetime, переведи полученное значение в понятные значения даты и времени.
import telebot
from dotenv import load_dotenv
import os
import datetime


load_dotenv()
TOKEN = os.getenv('TELEGRAM_RPG_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def start(msg: telebot.types.Message):
    print(msg.date)
    print(datetime.datetime.fromtimestamp(msg.date))


bot.infinity_polling()
