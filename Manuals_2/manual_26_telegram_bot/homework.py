# ДЗ
# Создать бота опросника. Можно подключить базу данных. Бот должен делать следующее:
# 1. по команде в ЛС с пользователем создавать новый опрос;
# 2. в ЛС с пользователем спрашивать название нового опроса;
# 3. в ЛС с пользователем спрашивать список возможных ответов;
# 4. где-то сохранять в связке id пользователя и id опроса;
# 5. отправлять готовый опрос и в канал, где есть бот, и в группу, где есть бот;
# 6. собирать анонимные ответы, считая их количество;
# 7. по команде в ЛС с пользователем выдавать результат обоих опросов.
import telebot
from dotenv import load_dotenv
import os
import s_taper
from s_taper.consts import *


load_dotenv()
TOKEN = os.getenv("TELEGRAM_INLINE_TOKEN")
bot = telebot.TeleBot(TOKEN)

scheme = {
    'user_id': INT + KEY,
    'poll_ids': INT
}

users = s_taper.Taper('users', 'data.db').create_table(scheme)

# Хранение локальной информации
temp = {}


@bot.message_handler(["start"])
def start(msg):
    bot.send_message(msg.chat.id, f"Да-да, я слушаю")


@bot.message_handler(["create_poll"])
def create_poll(msg: telebot.types.Message):
    global temp
    temp.clear()
    temp['poll_info'] = {}
    temp['user_id'] = msg.from_user.id
    if msg.chat.type == 'group':
        bot.send_message(temp['user_id'], "Подтвердите желание запустить команду /create_poll")
    else:
        bot.send_message(temp['user_id'], "Давайте создадим новый опрос. Введите название опроса:")
        bot.register_next_step_handler(msg, create_poll_title)


def create_poll_title(msg: telebot.types.Message):
    global temp
    temp['poll_title'] = msg.text
    bot.send_message(temp['user_id'], f'Название опроса установлено "{temp['poll_title']}".'
                                      f'\nТеперь перечислите варианты ответов (каждый с новой строки):')
    bot.register_next_step_handler(msg, create_poll_answers)


def create_poll_answers(msg: telebot.types.Message):
    global temp
    temp['poll_answers'] = msg.text.split('\n')
    temp['poll_id'] = bot.send_poll(temp['user_id'], temp['poll_title'], temp['poll_answers']).message_id

    users.write([temp['user_id'], temp['poll_id']])

    bot.send_message(temp['user_id'], "Опрос создан и разослан!")
    bot.send_poll(-4190979732, temp['poll_title'], temp['poll_answers'])
    bot.send_poll(-1002050227868, temp['poll_title'], temp['poll_answers'])


@bot.message_handler(["poll_info"])
def poll_info(msg):
    keys = temp['poll_info'].keys()
    answer = ""
    for key in keys:
        answer += f'{key} — {temp['poll_info'][key]} голосов!\n'
    bot.send_message(temp['user_id'], answer)


@bot.message_handler(content_types=['text'])
def test(msg):
   pass


@bot.channel_post_handler(content_types=['text'])
def post_check(msg):
    pass


@bot.poll_handler(func=lambda poll: True)
def handle_poll_answer(poll: telebot.types.Poll):
    global temp
    options = poll.options
    for o in options:
        keys = temp['poll_info'].keys()
        if o.text in keys:
            temp['poll_info'][o.text] += o.voter_count
        else:
            temp['poll_info'][o.text] = o.voter_count


bot.infinity_polling()
