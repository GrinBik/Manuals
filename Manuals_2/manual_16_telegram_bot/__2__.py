# ДЗ
# Придумать текст для будущих локаций: площади тренировок и палаточного лагеря.
# Переместить все текстовые переменные в модуль text.py и импортировать его в главный файл.
import telebot
from dotenv import load_dotenv
import os
from text import reg, tren_square, camp


load_dotenv()
TOKEN = os.getenv('TELEGRAM_RPG_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, reg % msg.from_user.first_name)


print(reg)
print(tren_square)
print(camp)

bot.infinity_polling()
