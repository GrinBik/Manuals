import telebot
from telebot.types import InlineQuery
from telebot.types import InputTextMessageContent as ITC
from telebot.types import InlineQueryResultArticle as ILQRA
from telebot.types import InlineQueryResultPhoto as ILQRP
from telebot.types import InlineQueryResultVideo as ILQRV
from dotenv import load_dotenv
import os, math


load_dotenv()
TOKEN = os.getenv("TELEGRAM_INLINE_TOKEN")
bot = telebot.TeleBot(TOKEN)

plus_icon = "https://pp.vk.me/c627626/v627626512/2a627/7dlh4RRhd24.jpg"
minus_icon = "https://pp.vk.me/c627626/v627626512/2a635/ILYe7N2n8Zo.jpg"
divide_icon = "https://pp.vk.me/c627626/v627626512/2a620/oAvUk7Awps0.jpg"
multiply_icon = "https://pp.vk.me/c627626/v627626512/2a62e/xqnPMigaP5c.jpg"


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
            input_message_content=ITC(f"x = {e}"))
        bot.answer_inline_query(query.id, [urav])
        return
    elif query.query == "Кот":
        r = ILQRP(
            '7',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
            input_message_content=ITC('https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg'))
        bot.answer_inline_query(query.id, [r])
    elif query.query == 'Видео':
        r = ILQRV('8',
                  'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
                  'video/mp4',
                  'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                  'Title')
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
            input_message_content=ITC(f"{nums[0]} {''.join([f' + {i}' for i in nums[1:]])} = {summ}"),
            thumbnail_url=plus_icon)

        ans_2 = ILQRA(
            '2',
            "Разность",
            description=f"Результат: {diff}",
            input_message_content=ITC(f"{nums[0]} {''.join([f' - {i}' for i in nums[1:]])} = {diff}"),
            thumbnail_url=minus_icon)

        ans_3 = ILQRA(
            '3',
            "Произведение",
            description=f"Результат: {mult}",
            input_message_content=ITC(f"{nums[0]} {''.join([f' * {i}' for i in nums[1:]])} = {mult}"),
            thumbnail_url=multiply_icon)

        if not flag:
            ans_4 = ILQRA(
                '4',
                "Деление",
                description=f"Результат: {quo}",
                input_message_content=ITC(f"{nums[0]} {''.join([f' / {i}' for i in nums[1:]])} = {quo}"),
                thumbnail_url=divide_icon)

        ans_5 = ILQRA(
            '5',
            "Возведение в степень",
            description=f"Результат: {multi}",
            input_message_content=ITC(f"{nums[0]} {''.join([f' ** {i}' for i in nums[1:]])} = {multi}"))

        ans_6 = ILQRA(
            '6',
            "Корень",
            description=f"Результат: {sqrt}",
            input_message_content=ITC(f"{nums[0]} {''.join([f' ** {i}' for i in nums[1:]])} = {sqrt}"))

        if not flag:
            bot.answer_inline_query(query.id, [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6])
        else:
            bot.answer_inline_query(query.id, [ans_1, ans_2, ans_3, ans_5, ans_6])


bot.infinity_polling()
