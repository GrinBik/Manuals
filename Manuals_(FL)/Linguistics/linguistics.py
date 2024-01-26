import discord
from dotenv import load_dotenv
import os
import random
import asyncio


def check_word(answer):
    if WORDS[bot_word] == answer:
        return True
    return False


def reverse_word(letter):
    return letter[::-1]


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())

WORDS = {}
file = open('words.txt', 'r', encoding='UTF-8')
for line in file.readlines():
    word = line[:-1]
    WORDS[reverse_word(word)] = word


right_words = tuple(WORDS.keys())
bot_word = ''
game = False


@bot.slash_command(description='Игра "Задом наперед"')
async def reverse(ctx: discord.commands.context.ApplicationContext):
    global bot_word
    bot_word = random.choice(right_words)
    await ctx.respond(f'Угадай, что за слово: {bot_word}\nУ тебя 10 секунд!')
    try:
        user_answer = await bot.wait_for('message', timeout=10)
    except asyncio.TimeoutError:
        await ctx.respond("Время вышло! Попробуйте еще раз.")
        return
    result = check_word(user_answer.content.lower())
    if result:
        await ctx.respond(f'Молодец! Верно!')
    else:
        await ctx.respond(f'Ничего страшного, попробуй еще раз!')


bot.run(TOKEN)
