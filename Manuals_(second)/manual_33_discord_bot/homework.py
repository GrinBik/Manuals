# ДЗ
# Используя все полученные навыки работы с командами, добавить боту возможности секундомера, таймера и будильника.
# Должен быть секундомер, который начнёт засекать время по команде и остановится по команде.
# Он должен выдать общее время в понятном формате.
# Должен быть таймер, который будет принимать количество секунд и «звенеть» через указанное время.
# Должен быть будильник, который будет писать в чат в указанное время.
import discord
from dotenv import load_dotenv
import os
from discord.ext import tasks


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())

bot.load_extension('cogs.test')

seconds = 0


@bot.event
async def on_ready():
    ping.start()


@tasks.loop(seconds=5)
async def ping():
    print(bot.latency)


@tasks.loop(seconds=1)
async def sec(ctx):
    global seconds
    seconds += 1
    await ctx.send(f'время на секундомере: {seconds // 60}м : {seconds % 60}с')


@bot.slash_command(name="start", description="Запускает секундомер")
async def start(ctx):
    global seconds
    seconds = 0
    await ctx.respond(f'Секундомер запущен!')
    sec.start(ctx)


@bot.slash_command(name="stop", description="Останавливает секундомер")
async def stop(ctx):
    sec.stop()
    await ctx.respond(f'Секундомер остановлен: {seconds // 60}м : {seconds % 60}с')


bot.run(TOKEN)
