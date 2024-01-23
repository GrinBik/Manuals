# ДЗ
# Разобраться с аннотациями и классами.
# Используя подсказки, посмотреть что есть внутри класса Message и его внутренних классов.
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    print(message)
    await message.channel.send("Hello!")
    print(message.channel)
    print(message.author)


bot.run(TOKEN)
