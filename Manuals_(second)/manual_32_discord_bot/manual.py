import discord
from dotenv import load_dotenv
import os
from discord.ui import Button, View


class MyView(View):
    def __init__(self):
        super().__init__()
        a = Button(label=" Я готов!", style=discord.ButtonStyle.green, emoji="👍")
        self.add_item(a)
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
        print(calc)
        if calc == "1479":
            await interaction.response.send_message(content="Успешно! 💎💎💎", view=None)
        elif len(calc) >= 4:
            print(calc)
            await interaction.response.edit_message(content="Ошибка ❌", view=None)
        else:
            await interaction.response.send_message(content="Введите следующую цифру", view=None, delete_after=1)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=discord.Intents.all())

calc = ""


@bot.slash_command()
async def test(ctx):
    link = Button(label="PyCord Docs", url="https://guide.pycord.dev/interactions/ui-components/buttons", emoji='🐍')
    btn = Button(label="Like", style=discord.ButtonStyle.blurple, emoji="❤️")
    view = View()
    view.add_item(link)
    view.add_item(btn)
    my_view = MyView()
    await ctx.respond("Hi", view=my_view)
    await ctx.respond("Hi", view=view)

    async def s_callback(interaction: discord.Interaction):
        # await interaction.response.send_message(content="Ночь, что за странная свобода: от заката до восхода")
        await interaction.response.edit_message(content="Ваше мнение учтено!", view=None)

    btn.callback = s_callback


bot.run(TOKEN)
