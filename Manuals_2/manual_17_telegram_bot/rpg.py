import telebot
from dotenv import load_dotenv
import os
from text import reg, tren_square, camp
import s_taper
from s_taper.consts import *
import time


def is_new_player(msg: telebot.types.Message):
    result = users.read_all()
    for user in result:
        if user[0] == msg.chat.id:
            return False
    return True


load_dotenv()
TOKEN = os.getenv('TELEGRAM_RPG_TOKEN')
bot = telebot.TeleBot(TOKEN)

user_scheme = {
    "userid": INT + KEY,
    "name": TEXT,
    "power": TEXT,
    "hp": INT,
    "dmg": INT,
    "lvl": INT,
    "xp": INT
}

users = s_taper.Taper("users", "data.db").create_table(user_scheme)

temp = {}


@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    if is_new_player(msg):
        reg_1(msg)
        temp[msg.chat.id] = {"name": None}
    else:
        pass


def reg_1(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, reg % msg.from_user.first_name)
    bot.register_next_step_handler(msg, reg_2)


def reg_2(msg: telebot.types.Message):
    if not temp[msg.chat.id]["name"]:
        temp[msg.chat.id]["name"] = msg.text
    bot.send_message(msg.chat.id, "Выбери свою стихию, падаван. Земля 🌍, Вода 💦, Огонь 🔥, Воздух 🌬️")
    bot.register_next_step_handler(msg, reg_3)


def reg_3(msg: telebot.types.Message):
    if msg.text == "Огонь":
        bot.send_message(msg.chat.id, "Магия Огня под запретом в городе!")
        bot.register_next_step_handler(msg, reg_2)
        return
    temp[msg.chat.id]["power"] = msg.text
    users.write([msg.chat.id,
                 temp[msg.chat.id]["name"],
                 msg.text,
                 100,
                 10,
                 1,
                 0])
    bot.send_message(msg.chat.id, text='Игрок создан!')
    time.sleep(2)
    menu(msg)


@bot.message_handler(['menu'])
def menu(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, text='Menu')


bot.infinity_polling()

# ДЗ
# Написать текст для меню. Этот текст должен содержать одну строку текста и список команд управления игрой.

menu = 'Что будешь делать?\n' \
       '/square — площадь\n' \
       '/home — лагерь\n' \
       '/stats — статистика'
