import telebot
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('TELEGRAM_RPG_TOKEN')
bot = telebot.TeleBot(TOKEN)

n = 0
m = 0


@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, "Назови число от 1 до 10")
    bot.register_next_step_handler(msg, number_two)


def number_two(msg: telebot.types.Message):
    global n
    n = int(msg.text)
    if n not in range(1, 11):
        bot.send_message(msg.chat.id, "Ты ошибся в диапазоне!")
        start(msg)
        return
    bot.send_message(msg.chat.id, "Назови еще одно число от 1 до 10")
    bot.register_next_step_handler(msg, result)


def result(msg: telebot.types.Message):
    global m
    m = int(msg.text)
    if m not in range(1, 11):
        bot.send_message(msg.chat.id, "Ты ошибся в диапазоне!")
        bot.send_message(msg.chat.id, "Назови еще одно число от 1 до 10")
        bot.register_next_step_handler(msg, result)
        return

    bot.send_message(msg.chat.id, f"Если возвести {n} в {m} степень, то получится число {int(n) ** int(m)}")


bot.infinity_polling()
