import s_taper
import telebot
from dotenv import load_dotenv
import os


def check_in(a, b):
    if a in b:
        print("Всё верно!")
    else:
        print("Ошибка")


def test(data: list):
    print(type(data))


# Переменная и её тип данных
a = 17  # int
a = 19.33  # float
a = "Hello"  # str
a = True  # bool
a = [12.3213234, 54342, 54353]  # list
a = {23: True, 45: ("Ай люли, люли", 1)}  # dict
print(a)  # выведет последнее заданное значение

check_in("люли", "Ай люли, люли")
# check_in("люли", 123456789)

s = s_taper.Taper('1', '1.db')
# s.read(121, 232)

name: str = "Рюрик"
name += "овичи"
print(name)

test("Тест")

load_dotenv()
TOKEN = os.getenv('TELEGRAM_RPG_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def start(msg: telebot.types.Message):
    print(msg)


bot.infinity_polling()
