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
async def summ(ctx: discord.commands.context.ApplicationContext, first: int, second: int):
    summa = first + second
    await ctx.respond(f"Ответ: {summa}.")


@bot.message_command(name="Повысить репутацию")
async def plus_rep(ctx: discord.commands.context.ApplicationContext, message: discord.Message):
    await ctx.respond(f"+ Rep, {message.author.name}")


@bot.user_command(name="Дата регистрации")
async def account_creation_date(ctx, member: discord.Member):
    await ctx.respond(f"{member.name} создал аккаунт {member.created_at}")


bot.run(TOKEN)
