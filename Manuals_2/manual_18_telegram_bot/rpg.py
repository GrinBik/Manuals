import telebot
from dotenv import load_dotenv
import os
import text
import s_taper
from s_taper.consts import *
import time
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove


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

clear = ReplyKeyboardRemove()


@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    if is_new_player(msg):
        reg_1(msg)
        temp[msg.chat.id] = {"name": None}
    else:
        pass


def reg_1(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, text.reg % msg.from_user.first_name)
    bot.register_next_step_handler(msg, reg_2)


def reg_2(msg: telebot.types.Message):
    if not temp[msg.chat.id]["name"]:
        temp[msg.chat.id]["name"] = msg.text
        kb = ReplyKeyboardMarkup(True, True)
        kb.row("Земля 🌍", "Вода 💦")
        kb.row("Огонь 🔥", "Воздух 🌬️")
        bot.send_message(msg.chat.id, "Выбери свою стихию, падаван.", reply_markup=kb)
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
    bot.send_message(msg.chat.id, text='Игрок создан!', reply_markup=clear)
    time.sleep(2)
    menu(msg)


@bot.message_handler(['menu'])
def menu(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, text=text.menu)


@bot.message_handler(['square'])
def square(msg: telebot.types.Message):
    kb = telebot.types.ReplyKeyboardMarkup(True, True)
    kb.row("Тренироваться")
    kb.row("Проверить силы")
    bot.send_message(msg.chat.id, "Ты на площади тренировок", reply_markup=kb)
    bot.register_next_step_handler(msg, square_handler)


def square_handler(msg: telebot.types.Message):
    if msg.text == "Тренироваться":
        pass
    if msg.text == "Проверить силы":
        pass


# ДЗ
# Создать такие же пары функций для остальных квестов в игре.
@bot.message_handler(['home'])
def home(msg: telebot.types.Message):
    kb = telebot.types.ReplyKeyboardMarkup(True, True)
    kb.row("Отдохнуть")
    kb.row("Перекусить")
    bot.send_message(msg.chat.id, "Ты в своем лагере, в безопасности - дома!", reply_markup=kb)
    bot.register_next_step_handler(msg, home_handler)


def home_handler(msg: telebot.types.Message):
    if msg.text == "Отдохнуть":
        pass
    if msg.text == "Перекусить":
        pass


bot.infinity_polling()
