import discord
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())

reps = {}


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    global reps
    if message.author not in reps:
        reps[message.author] = 0

    if message.reference:
        ref_author = bot.get_message(message.reference.message_id).author
        if message.content == "+++":
            reps[ref_author] += 1
            await message.channel.send(f'{message.author.name} поднял репутацию '
                                       f'{ref_author.name}!\n'
                                       f'Теперь у него {reps[ref_author]} баллов.')
        if reps[message.author] > 2:
            Moder = discord.utils.get(message.author.guild.roles, name="Модер")
            await ref_author.add_roles(Moder)


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
