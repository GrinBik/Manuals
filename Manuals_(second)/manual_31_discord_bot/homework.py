# ДЗ
# Дописать функционал убавления репутации за счёт ответа «---» (три минуса).
# Если репутация упадёт ниже 995, отнимать роль Модератора. Это можно сделать по такому же принципу,
# но метод будет называться remove_roles().
# Перенести систему рейтинга в базу данных SQLite.
import discord
from dotenv import load_dotenv
import os
import s_taper
from s_taper.consts import *


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())

scheme = {
    'user_id': INT + KEY,
    'name': TEXT,
    'rating': INT
}

users = s_taper.Taper('users', 'data.db').create_table(scheme)


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    try:
        user = users.read('user_id', message.author.id)
    except IndexError:
        user = [message.author.id, message.author.name, 0]
        users.write(user)

    if message.reference:
        ref_author = bot.get_message(message.reference.message_id).author
        if message.content == "+++":
            user[2] += 1
            users.write(user)
            await message.channel.send(f'{user[1]} поднял репутацию '
                                       f'{ref_author.name}!\n'
                                       f'Теперь у него {user[2]} баллов.')
        elif message.content == "---":
            user[2] -= 1
            users.write(user)
            await message.channel.send(f'{user[1]} понизил репутацию '
                                       f'{ref_author.name}!\n'
                                       f'Теперь у него {user[2]} баллов.')
        if user[2] > 2:
            Moder = discord.utils.get(message.author.guild.roles, name="Модер")
            await ref_author.add_roles(Moder)
        elif user[2] < 2:
            Moder = discord.utils.get(message.author.guild.roles, name="Модер")
            await ref_author.remove_roles(Moder)


@bot.event
async def on_member_update(old: discord.Member, gold: discord.Member):
    channel = None
    channels = gold.guild.channels
    for ch in channels:
        if ch.name == "основной":
            channel = ch
    if old.roles != gold.roles:
        await channel.send(f"У {gold.name} изменилась роль!")

bot.run(TOKEN)
