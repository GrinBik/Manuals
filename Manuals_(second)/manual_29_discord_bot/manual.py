import discord
from dotenv import load_dotenv
import os
import datetime


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())


@bot.slash_command(description="Текущее время в МСК")
async def time(ctx: discord.commands.context.ApplicationContext):
    moscow = datetime.timezone(datetime.timedelta(hours=3))
    data = datetime.datetime.now(moscow)
    await ctx.respond(f"Текущее время в Москве: {data.hour}:{data.minute}")


@bot.slash_command(description="Сложение")
async def summ(ctx, first: int, second: int):
    summa = first + second
    await ctx.respond(f"Ответ: {summa}.")


bot.run(TOKEN)
