# ДЗ
# Разобраться с аннотациями и классами.
# Используя подсказки, посмотреть что есть внутри класса Message и его внутренних классов.
# Пусть бот пишет администратору в ЛС, если кто-то из пользователей пишет в чате что-нибудь со словом «помощь».
# Сообщение администратору должно выглядеть так: Пользователь {юзернейм} просит помощи на сервере {имя сервера}!
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
    print(message.channel)
    print(message.author)
    guild = message.guild
    if "помощь" in message.content:
        for admin in guild.members:
            if admin.guild_permissions.administrator and admin.name == 'grinbik':
                await admin.send(f'Пользователь {message.author} просит помощи на сервере {guild}!')



bot.run(TOKEN)
