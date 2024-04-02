import discord
from discord.ext import commands
import asyncio
import datetime


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.alarm_time = None

    @discord.slash_command()
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye!')

    @discord.user_command()
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hello to {member.mention}!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('Welcome to the server!')

    @commands.slash_command()
    async def set_timer(self, ctx, seconds: int):
        await ctx.respond(f"Таймер установлен на {seconds} секунд.")
        await asyncio.sleep(seconds)
        await ctx.send(f"{ctx.author.mention}, время вышло! Таймер завершен.")

    @commands.slash_command()
    async def alarm(self, ctx, hours: int, minutes: int):
        self.alarm_time = datetime.datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)
        await ctx.send(f"Будильник установлен на {self.alarm_time.strftime('%H:%M')}!")
        seconds_until_alarm = (self.alarm_time - datetime.datetime.now()).total_seconds()
        await asyncio.sleep(seconds_until_alarm)
        await ctx.send("Время проснуться!")


def setup(bot):
    bot.add_cog(Test(bot))
