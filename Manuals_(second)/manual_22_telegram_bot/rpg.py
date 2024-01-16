import telebot
from dotenv import load_dotenv
import os
import text, fight
import s_taper
from s_taper.consts import *
import time, random, datetime
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


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
    "xp": INT,
    "can": BLN
}

users = s_taper.Taper("users", "data.db").create_table(user_scheme)

heal_scheme = {
    "userid": INT + KEY,
    "food": TEXT
}

heals = s_taper.Taper("heals", "data.db").create_table(heal_scheme)

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
    hp, dmg = fight.powers[msg.text]
    users.write([msg.chat.id,
                 temp[msg.chat.id]["name"],
                 msg.text,
                 hp,
                 dmg,
                 1,
                 0,
                 False])
    heals.write([msg.chat.id, {}])
    bot.send_message(msg.chat.id, text='Игрок создан!', reply_markup=clear)
    time.sleep(2)
    menu(msg)


@bot.message_handler(['menu'])
def menu(msg: telebot.types.Message):
    try:
        temp[msg.chat.id]
    except KeyError:
        temp[msg.chat.id] = {}
    message = text.menu
    bot.send_message(msg.chat.id, message, reply_markup=clear)


@bot.message_handler(['square'])
def square(msg: telebot.types.Message):
    kb = telebot.types.ReplyKeyboardMarkup(True, True)
    kb.row("Тренироваться")
    kb.row("Проверить силы")
    bot.send_message(msg.chat.id, "Ты на площади тренировок", reply_markup=kb)
    bot.register_next_step_handler(msg, square_handler)


def square_handler(msg: telebot.types.Message):
    if msg.text == "Тренироваться":
        workout(msg)
    if msg.text == "Проверить силы":
        exam(msg)


@bot.message_handler(['home'])
def home(msg: telebot.types.Message):
    kb = telebot.types.ReplyKeyboardMarkup(True, True)
    kb.row("Отдохнуть")
    kb.row("Перекусить")
    bot.send_message(msg.chat.id, "Ты в своем лагере, в безопасности - дома!", reply_markup=kb)
    bot.register_next_step_handler(msg, home_handler)


def home_handler(msg: telebot.types.Message):
    if msg.text == "Отдохнуть":
        sleep(msg)
    if msg.text == "Перекусить":
        eat(msg)


@bot.message_handler(commands=['add_heal'])
def add_heal(msg: telebot.types.Message):
    _, food = heals.read("userid", msg.chat.id)

    food["Хлеб"] = [1, 15]
    food["Айва"] = [1, 50]

    heals.write([msg.chat.id, food])
    bot.send_message(msg.chat.id, "Выдали еду!")


def eat(msg: telebot.types.Message):
    kb = InlineKeyboardMarkup()
    _, food = heals.read("userid", msg.chat.id)
    if food != {}:
        for key in food:
            kb.row(InlineKeyboardButton(f"{key} {food[key][1]}❤️ -- {food[key][0]}шт.",
                                        callback_data=f"food_{key}_{food[key][1]}"))
        bot.send_message(msg.chat.id, "Что будешь есть?", reply_markup=kb)
    else:
        bot.send_message(msg.chat.id, "У тебя нет еды (", reply_markup=clear)
        bot.send_message(msg.chat.id, text=text.menu)


@bot.callback_query_handler(func=lambda call: True)
def callback(call: telebot.types.CallbackQuery):
    if call.data.startswith("food_"):
        a = call.data.split("_")
        eating(call.message, a[1], a[2])
        kb = InlineKeyboardMarkup()
        _, food = heals.read("userid", call.message.chat.id)
        for key in food:
            kb.row(InlineKeyboardButton(f"{key} {food[key][1]}❤️ -- {food[key][0]}шт.",
                                        callback_data=f"food_{key}_{food[key][1]}"))

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb)
    elif call.data.startswith("sleep_"):
        a = call.data.split("_")
        t = int(a[1])
        if t < 2:
            t = 1
        else:
            t //= 2
        bot.send_message(call.message.chat.id, f"Ты лег отдыхать на {t} минут")

        sleeping(call.message, a[1])
        time.sleep(t * 60)

        bot.delete_message(call.message.chat.id, call.message.message_id)
        menu(call.message)
    elif call.data == '0':
        menu(call.message)
    elif call.data == "menu":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        menu(call.message)
    elif call.data == "workout":
        player = users.read("userid", call.message.chat.id)
        player[4] += player[5] / 10
        player[4] = round(player[4], 4)
        users.write(player)
        bot.answer_callback_query(call.id, "Ты тренируешься и твоя сила увеличивается! \n"
                                           f"Теперь ты наносишь {player[4]}⚔️", True)


def eating(msg, ft, hp):
    _, food = heals.read("userid", msg.chat.id)
    player = users.read("userid", msg.chat.id)
    # Отнимаем еду
    if food[ft][0] == 1:
        del food[ft]
    else:
        food[ft][0] -= 1

    heals.write([msg.chat.id, food])

    # Добавляем ХП
    player[3] += int(hp)
    users.write(player)
    if food == {}:
        bot.send_message(msg.chat.id, "У тебя не осталось еды (", reply_markup=clear)
        bot.send_message(msg.chat.id, text=text.menu)


def sleep(msg: telebot.types.Message):
    player = users.read("userid", msg.chat.id)
    low = int(fight.powers[player[2]][0] * player[5]) // 2 - player[3]
    high = int(fight.powers[player[2]][0] * player[5]) - player[3]
    kb = InlineKeyboardMarkup()
    if low > 0:
        kb.row(InlineKeyboardButton(f"Вздремнуть: +{low}❤️", callback_data=f"sleep_{low}"))
    if high > 0:
        kb.row(InlineKeyboardButton(f"Поспать: +{high}❤️", callback_data=f"sleep_{high}"))
    if len(kb.keyboard) == 0:
        kb.row(InlineKeyboardButton("Спать не хочется", callback_data="0"))
        bot.send_message(msg.chat.id, "Вы полны сил, зачем же отдыхать!", reply_markup=kb)
    else:
        bot.send_message(msg.chat.id, "Выбери, сколько будешь отдыхать:", reply_markup=kb)


def sleeping(msg, hp):
    player = users.read("userid", msg.chat.id)
    player[3] += int(hp)
    users.write(player)


@bot.message_handler(['stats'])
def stats(msg: telebot.types.Message):
    player = users.read_obj("userid", msg.chat.id)
    t = f"{player.power[-1]} {player.name}:\n" \
        f"Здоровье: {player.hp}❤️\n" \
        f"Урон: {player.dmg}⚔️\n" \
        f"LVL: {player.lvl}.{player.xp}⚜️\n\n" \

    _, food = heals.read("userid", msg.chat.id)
    if food != {}:
        t += "Еда:\n"
        for f in food:
            t += f"{f} ❤️{food[f][1]} — {food[f][0]}шт.\n"
    bot.send_message(msg.chat.id, t)
    time.sleep(3)
    menu(msg)


def workout(msg: telebot.types.Message):
    kb = InlineKeyboardMarkup()
    kb.row(InlineKeyboardButton("Тренироваться", callback_data="workout"))
    kb.row(InlineKeyboardButton("Назад", callback_data="menu"))
    bot.send_message(msg.chat.id, "Жми, чтобы тренироваться!", reply_markup=kb)


def exam(msg: telebot.types.Message):
    player = users.read_obj("userid", msg.chat.id)
    bot.send_message(msg.chat.id, f"Приготовься к испытанию, {player.name}!", reply_markup=clear)
    time.sleep(2)
    temp[msg.chat.id]["attack_count"] = 0
    start_exam(msg)


def start_exam(msg: telebot.types.Message):
    random.choice((block, attack))(msg)


def block(msg: telebot.types.Message):
    # Создаём список сторон и перемешиваем его
    sides = ["Слева", "Справа", "Сверху", "Снизу"]
    random.shuffle(sides)

    # Создаём клавиатуру
    kb = telebot.types.ReplyKeyboardMarkup(True, False)
    kb.row(sides[0], sides[3])
    kb.row(sides[1], sides[2])

    # Выбираем сторону удара и отправляем сообщение
    right = random.choice(sides)
    bot.send_message(msg.chat.id, f"Защищайся! Удар {right}!", reply_markup=kb)
    temp[msg.chat.id]["block_start"] = datetime.datetime.now().timestamp()
    bot.register_next_step_handler(msg, block_handler, right)


def block_handler(msg: telebot.types.Message, side: str):
    final = datetime.datetime.now().timestamp()
    player = users.read_obj("userid", msg.chat.id)
    if final - temp[msg.chat.id]["block_start"] > player.dmg / 5 or side != msg.text:
        bot.send_message(msg.chat.id, "Твоя реакция слишком медлительна! Ты не готов!")
        time.sleep(1)
        menu(msg)
        return

    temp[msg.chat.id]["attack_count"] += 1
    if temp[msg.chat.id]["attack_count"] == 10:
        player = users.read("userid", msg.chat.id)
        if player[4] > 40:
            player[7] = True
            users.write(player)
            bot.send_message(msg.chat.id, "Ты готов к защите города, поздравляю!")
        else:
            bot.send_message(msg.chat.id, "Ты прошел тренировку! Но твой уровень урона недостаточен!")
        time.sleep(1)
        menu(msg)
        return
    bot.send_message(msg.chat.id, f"Ты справился, продолжаем!"
                                  f"\nТы выполнил {temp[msg.chat.id]["attack_count"]}/10 проверок силы")
    time.sleep(1)
    start_exam(msg)


def attack(msg: telebot.types.Message):
    # Создаём список сторон и перемешиваем его
    sides = ["Слева", "Справа", "Сверху", "Снизу"]

    # Создаём клавиатуру
    kb = telebot.types.ReplyKeyboardMarkup(True, False)
    kb.row(sides[0], sides[3])
    kb.row(sides[1], sides[2])

    bot.send_message(msg.chat.id, "Куда атаковать мастера?", reply_markup=kb)
    bot.register_next_step_handler(msg, attack_handler)


def attack_handler(msg: telebot.types.Message):
    sides = ["Слева", "Справа", "Сверху", "Снизу"]
    master = random.choice(sides)
    if master == msg.text:
        bot.send_message(msg.chat.id, "Твоя атака слишком медлительна! Ты не готов!")
        time.sleep(1)
        menu(msg)
        return
    temp[msg.chat.id]["attack_count"] += 1
    if temp[msg.chat.id]["attack_count"] == 10:
        player = users.read("userid", msg.chat.id)
        if player[4] > 40:
            player[7] = True
            users.write(player)
            bot.send_message(msg.chat.id, "Ты готов к защите города, поздравляю!")
        else:
            bot.send_message(msg.chat.id, "Ты прошел тренировку! Но твой уровень урона недостаточен!")
        time.sleep(1)
        menu(msg)
        return
    bot.send_message(msg.chat.id, f"Ты справился, продолжаем!"
                                  f"\nТы выполнил {temp[msg.chat.id]["attack_count"]}/10 проверок силы")
    time.sleep(1)
    start_exam(msg)


bot.infinity_polling()

# ДЗ
# Самостоятельно напиши функцию attack, которая будет давать возможность игроку выбрать одну из 4-х сторон для атаки.
# После атаки тренер должен случайным образом выбрать сторону защиты.
# Если атака игрока прошла успешно, счётчик драки (временная переменная) увеличивается на 1.

# Если счётчик драки достигает 10 и урон игрока > 40,
# то тренировка пройдена и игрок получает возможность защищать город.
# Возможно, придётся добавить столбец в базу данных для хранения информации.
