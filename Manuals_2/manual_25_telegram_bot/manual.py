import telebot
from telebot.types import InlineQuery
from telebot.types import InputTextMessageContent as ITMC
from telebot.types import InlineQueryResultArticle as ILQRA
from telebot.types import InlineQueryResultPhoto as ILQRP
from telebot.types import InlineQueryResultVideo as ILQRV
from dotenv import load_dotenv
import os
import math


load_dotenv()
TOKEN = os.getenv("TELEGRAM_INLINE_TOKEN")
bot = telebot.TeleBot(TOKEN)

plus_icon = "https://pp.vk.me/c627626/v627626512/2a627/7dlh4RRhd24.jpg"
minus_icon = "https://pp.vk.me/c627626/v627626512/2a635/ILYe7N2n8Zo.jpg"
divide_icon = "https://pp.vk.me/c627626/v627626512/2a620/oAvUk7Awps0.jpg"
multiply_icon = "https://pp.vk.me/c627626/v627626512/2a62e/xqnPMigaP5c.jpg"

# Хранение локальной информации
temp = {}


@bot.message_handler(["start"])
def start(msg):
    bot.send_message(msg.chat.id, f"Да-да, я слушаю")


@bot.inline_handler(func=lambda query: len(query.query) > 1)
def inline(query: InlineQuery):
    nums = query.query.split(" ")
    # Решение уравнения
    if "x" in nums:
        if nums[1] == "+":
            e = nums[4] + " - " + nums[2]
        e = eval(e)
        urav = ILQRA(
            '4',
            "Уравнение",
            description=f"Результат: {e}",
            input_message_content=ITMC(f"x = {e}"))
        bot.answer_inline_query(query.id, [urav])
        return
    elif "Кот" in nums:
        r = ILQRP(
            '7',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
            input_message_content=ITMC('https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg'))
        bot.answer_inline_query(query.id, [r])
    elif 'Видео' in nums:
        r = ILQRV('8',
                  'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
                  'video/mp4',
                  'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                  'Title')
        bot.answer_inline_query(query.id, [r])
    elif 'Умножение' in nums:
        r = ILQRP(
            '9',
            'https://xn--80afebc2bl4aj7g.xn--p1ai/upload/iblock/3eb/3ebc0dfa867e344cf30d81409cfd7558.jpg',
            'https://xn--80afebc2bl4aj7g.xn--p1ai/upload/iblock/3eb/3ebc0dfa867e344cf30d81409cfd7558.jpg',
            input_message_content=ITMC('https://xn--80afebc2bl4aj7g.xn--p1ai/upload/iblock/3eb/3ebc0dfa867e344cf30d81409cfd7558.jpg'))
        bot.answer_inline_query(query.id, [r])
    elif "Квадратные уравнения" in query.query:
        video_url = 'https://www.youtube.com/watch?v=9NiVFyhY-f0'
        r = ILQRV(
            '10',
            video_url=video_url,
            mime_type='video/mp4',
            thumbnail_url=video_url,
            title='Видео с YouTube')
        bot.answer_inline_query(query.id, [r])
    else:
        nums = tuple(map(float, nums))
        flag = False
        if 0 in nums:
            flag = True

        # Считаем сумму
        summ = sum(nums)

        # Считаем разницу
        diff = nums[0]
        for el in nums[1:]:
            diff -= el

        # Считаем произведение
        mult = nums[0]
        for el in nums[1:]:
            mult *= el

        if not flag:
            # Считаем частное
            quo = nums[0]
            for el in nums[1:]:
                quo /= el

        # Возведение в степень
        multi = nums[0]
        for el in nums[1:]:
            multi **= el

        # Квадратный корень
        sqrt = math.sqrt(nums[0])

        ans_1 = ILQRA(
            '1',
            "Сумма",
            description=f"Результат: {summ}",
            input_message_content=ITMC(f"{nums[0]} {''.join([f' + {i}' for i in nums[1:]])} = {summ}"),
            thumbnail_url=plus_icon)

        ans_2 = ILQRA(
            '2',
            "Разность",
            description=f"Результат: {diff}",
            input_message_content=ITMC(f"{nums[0]} {''.join([f' - {i}' for i in nums[1:]])} = {diff}"),
            thumbnail_url=minus_icon)

        ans_3 = ILQRA(
            '3',
            "Произведение",
            description=f"Результат: {mult}",
            input_message_content=ITMC(f"{nums[0]} {''.join([f' * {i}' for i in nums[1:]])} = {mult}"),
            thumbnail_url=multiply_icon)

        if not flag:
            ans_4 = ILQRA(
                '4',
                "Деление",
                description=f"Результат: {quo}",
                input_message_content=ITMC(f"{nums[0]} {''.join([f' / {i}' for i in nums[1:]])} = {quo}"),
                thumbnail_url=divide_icon)

        ans_5 = ILQRA(
            '5',
            "Возведение в степень",
            description=f"Результат: {multi}",
            input_message_content=ITMC(f"{nums[0]} {''.join([f' ** {i}' for i in nums[1:]])} = {multi}"))

        ans_6 = ILQRA(
            '6',
            "Корень",
            description=f"Результат: {sqrt}",
            input_message_content=ITMC(f"{nums[0]} {''.join([f' ** {i}' for i in nums[1:]])} = {sqrt}"))

        if not flag:
            bot.answer_inline_query(query.id, [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6])
        else:
            bot.answer_inline_query(query.id, [ans_1, ans_2, ans_3, ans_5, ans_6])


@bot.message_handler(content_types=['text'])
def math(msg, repeat=False):
    global temp
    if msg.text.lower().startswith("математик"):
        temp["математик"] = msg.from_user.id
        bot.send_message(msg.chat.id, "Чем помочь?")
        bot.register_next_step_handler(msg, math_handler)
    else:
        bot.send_message(msg.chat.id, f"Пользователь {msg.from_user.id} написал в {msg.chat.id}")
    if repeat:
        bot.register_next_step_handler(msg, math_handler)


def math_handler(msg):
    if temp["математик"] != msg.from_user.id:
        math(msg, True)
        return
    bot.send_message(msg.chat.id, f"{eval(msg.text)}")


bot.infinity_polling()
