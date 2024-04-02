# ДЗ
# Протестировать отправку медиа с помощью send_message()
import discord
from dotenv import load_dotenv
import os
from discord.ui import Button, View


class MyView(View):
    def __init__(self):
        super().__init__()
        num = 0
        for row in range(3):
            for n in range(3):
                num += 1
                a = Button(label=f"{num}", row=row, custom_id=f"btn_{num}")
                a.callback = self.callback
                self.add_item(a)

    async def callback(self, interaction: discord.Interaction):
        global calc
        calc += interaction.custom_id[4:]
        if calc == "1479":
            await interaction.response.send_message(content="Успешно! 💎💎💎", view=None)
        elif len(calc) >= 4:
            print(calc)
            await interaction.response.edit_message(content="Ошибка ❌", view=None)
        else:
            await interaction.response.send_message(content="https://clipart-library.com/images/piod8EddT.gif", view=None, delete_after=2)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())

calc = ""

@bot.slash_command()
async def test(ctx):
    my_view = MyView()
    await ctx.respond("Hi", view=my_view)


bot.run(TOKEN)
