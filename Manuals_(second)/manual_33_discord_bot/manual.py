import discord
from dotenv import load_dotenv
import os
from discord.ext import tasks


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())

bot.load_extension('cogs.test')


@bot.event
async def on_ready():
    ping.start()


@tasks.loop(seconds=5)
async def ping():
    print(bot.latency)


bot.run(TOKEN)
