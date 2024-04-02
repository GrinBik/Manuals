import telebot
from telebot.types import InlineQuery
from telebot.types import InputTextMessageContent as ITC
from telebot.types import InlineQueryResultArticle as ILQRA
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("TELEGRAM_INLINE_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.inline_handler(func=lambda query: len(query.query) > 1)
def inline(query: InlineQuery):
    print(query.query)
    nums = query.query.split(" ")
    print(nums)
    nums = tuple(map(float, nums))
    print(nums)

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

    # Считаем частное
    quo = nums[0]
    for el in nums[1:]:
        quo /= el

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

    ans_4 = ILQRA(
        '4',
        "Деление",
        description=f"Результат: {quo}",
        input_message_content=ITC(f"{nums[0]} {''.join([f' / {i}' for i in nums[1:]])} = {quo}"))

    bot.answer_inline_query(query.id, [ans_1, ans_2, ans_3, ans_4])


bot.infinity_polling()
