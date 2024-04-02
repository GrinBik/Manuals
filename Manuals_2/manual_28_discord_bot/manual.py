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
    await message.reply(message.content)
    await message.channel.send("Hello!")
    await message.author.send("Bonjour!")


bot.run(TOKEN)
