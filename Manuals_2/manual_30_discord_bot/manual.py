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
    if "зебра" in message.content:
        await message.delete(delay=2)


@bot.event
async def on_member_join(member: discord.Member):
    channels = member.guild.channels
    for ch in channels:
        if ch.name == "основной":
            await ch.send(f"Привет, @{member.name}")


@bot.event
async def on_member_remove(member: discord.Member):
    channels = member.guild.channels
    for ch in channels:
        if ch.name == "основной":
            await ch.send(f"{member.name.title()} вышел с сервера...")


@bot.event
async def on_member_update(old: discord.Member, gold: discord.Member):
    channel = None
    channels = gold.guild.channels
    for ch in channels:
        if ch.name == "основной":
            channel = ch
    if old.nick != gold.nick:
        await channel.send(f"{old.name if not old.nick else old.nick} теперь "
                           f"{'без ника' if not gold.nick else gold.nick}")
    if old.roles != gold.roles:
        await channel.send(f"У {old.name} изменилась роль!")


@bot.event
async def on_user_update(old: discord.User, gold: discord.User):
    channel = None
    members = bot.get_all_members()
    for mem in members:
        if mem.name == gold.name:
            channels = mem.guild.channels
    for ch in channels:
        if ch.name == "основной":
            channel = ch

    if old.avatar != gold.avatar:
        await channel.send(f"У {gold.name} новая ава!")
        await channel.send(gold.avatar.url)
        await channel.send("👍👍👍")


@bot.slash_command(description="Удаление")
async def clear(ctx, num: int = 100):
    await ctx.channel.purge(limit=num)
    await ctx.respond("Готово 👍")
    await ctx.delete(delay=2)


bot.run(TOKEN)
