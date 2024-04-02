# ДЗ
# Написать команду таймер, которая будет отсчитывать указанное в неё не целое количество секунд.
import discord
from dotenv import load_dotenv
import os
import time


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())


@bot.slash_command(description="Таймер")
async def timer(ctx: discord.commands.context.ApplicationContext, seconds: int):
    long = 0
    for i in range(seconds):
        time.sleep(1)
        long += 1
        await ctx.respond(f"Прошла 1 секунда, а всего {long}.")
    await ctx.respond(f"Дзынь-Дзынь")


bot.run(TOKEN)
