import discord
from dotenv import load_dotenv
import os
import random
import asyncio


# Проверка ответа пользователя на верность
def check_word(answer):
    if WORDS[bot_word] == answer:
        return True
    return False


# Переворот слова задом наперед
def reverse_word(letter):
    return letter[::-1]


# Загрузка токена и установка боту прав
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())

# Все слова хранятся в словаре, ключ которого перевернутое слово, а значение правильно написанное слово
WORDS = {}
# Читаем слова из файла (каждое слово на новой строке)
file = open('words.txt', 'r', encoding='UTF-8')
for line in file.readlines():
    # Срезаем последний символ "\n"
    word = line[:-1]
    # Добавляем слово и его перевернутую версию в словарь
    WORDS[reverse_word(word)] = word


# Кортеж из перевернутых слов
right_words = tuple(WORDS.keys())
# Отправленное ботом перевернутое слово
bot_word = ''


# Пользователь решил сыграть в игру "Задом наперед"
@bot.slash_command(description='Игра "Задом наперед"')
async def reverse(ctx: discord.commands.context.ApplicationContext):
    global bot_word
    # Выбор ботом случайного перевернутого слова
    bot_word = random.choice(right_words)
    # Отправка сообщения пользователю
    await ctx.respond(f'Угадай, что за слово: {bot_word}\nУ тебя 10 секунд!')
    # Ждем от пользователя ответа 10 секунд
    try:
        # Если получаем ответ, то двигаемся дальше
        user_answer = await bot.wait_for('message', timeout=10)
    except asyncio.TimeoutError:
        # Если ответ не получаем, то проигрыш
        await ctx.respond("Время вышло! Попробуйте еще раз.")
        return
    # Проверка введенного пользователем слова
    result = check_word(user_answer.content.lower())
    if result:
        # При совпадении поздравляем
        await ctx.respond(f'Верно! Так держать')
    else:
        # При проигрыше поддерживаем
        await ctx.respond(f'Неверно...\nНичего страшного, попробуйте еще раз!')


# Запуск бота
bot.run(TOKEN)
