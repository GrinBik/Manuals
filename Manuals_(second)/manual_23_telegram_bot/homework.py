# Добавить возможность возводить число в любую указанную степень и находить квадратный корень из одиночного числа.
# Если ты введешь 0 вторым числом, то возникнет ошибка и нужные кнопки не появятся. Сделай исключение ошибки.
import telebot
from telebot.types import InlineQuery
from telebot.types import InputTextMessageContent as ITC
from telebot.types import InlineQueryResultArticle as ILQRA
from dotenv import load_dotenv
import os, math


load_dotenv()
TOKEN = os.getenv("TELEGRAM_INLINE_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.inline_handler(func=lambda query: len(query.query) > 1)
def inline(query: InlineQuery):
    nums = query.query.split(" ")
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
        input_message_content=ITC(f"{nums[0]} {''.join([f' + {i}' for i in nums[1:]])} = {summ}"))

    ans_2 = ILQRA(
        '2',
        "Разность",
        description=f"Результат: {diff}",
        input_message_content=ITC(f"{nums[0]} {''.join([f' - {i}' for i in nums[1:]])} = {diff}"))

    ans_3 = ILQRA(
        '3',
        "Произведение",
        description=f"Результат: {mult}",
        input_message_content=ITC(f"{nums[0]} {''.join([f' * {i}' for i in nums[1:]])} = {mult}"))

    if not flag:
        ans_4 = ILQRA(
            '4',
            "Деление",
            description=f"Результат: {quo}",
            input_message_content=ITC(f"{nums[0]} {''.join([f' / {i}' for i in nums[1:]])} = {quo}"))

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
