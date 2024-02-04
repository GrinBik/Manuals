# ДЗ
# Создать функцию, которая будет проверять сообщение игрока на слово «ящерица». Пусть все его сообщения удалятся,
# если участник использует это слово.
import discord
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if 'ящерица' in message.content:
        await message.channel.purge(limit=None, check=lambda mes: mes.author == message.author)
        await message.channel.send(f'{message.author.name} использовал запрещенное слово, все его сообщения удалены!')

bot.run(TOKEN)
