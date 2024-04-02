import telebot
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('TELEGRAM_RPG_TOKEN')
bot = telebot.TeleBot(TOKEN)

reg = "Привет, %s. В этой игре ты отринешь свою сущность и станешь настоящим магом 🧙‍♂️. Мир на пороге уничтожения: " \
      "народ огня 🔥 развязал войну и теперь все пытаются помешать им. Именно ты станешь тем, " \
      "кто спасёт человечество ⚔️!\n" \
      "Я верю в тебя!\n\nКак твоё имя, ученик?"


@bot.message_handler(['start'])  # Обработчик команды /start
def start(msg: telebot.types.Message):
    print(f"Юзер {msg.chat.id} вызвал команду "
          f"{msg.text}")
    bot.send_message(msg.chat.id, reg % msg.from_user.first_name)


@bot.message_handler(['help'])  # Обработчик команды /help
def start(msg: telebot.types.Message):
    print(f"Юзер {msg.chat.id} вызвал команду {msg.text}")
    bot.send_message(msg.chat.id, f"Юзер {msg.chat.id} вызвал команду {msg.text}")
    bot.send_message(msg.chat.id, f"Тебе нужна помощь?", reply_to_message_id=2046)


@bot.message_handler(content_types=["audio"])
def start(msg: telebot.types.Message):
    aud = msg.audio
    print(f"Бот получил аудио.\n"
          f"Продолжительность: {aud.duration / 60} мин.\n"
          f"Исполнитель: {aud.performer}\n"
          f"Название: {aud.title}\n"
          f"Размер файла: {aud.file_size / 1024000} МБайт")


@bot.message_handler(content_types=["photo"])
def start(msg: telebot.types.Message):
    photo_list = msg.photo
    print(photo_list)
    print(len(photo_list))
    for photo in photo_list:
        print(photo.__dict__)


@bot.message_handler(content_types=['text'])  # Ловец сообщения
def start(msg: telebot.types.Message):
    if msg.from_user.is_bot:
        return
    bot.send_message(msg.chat.id, f"Юзер 12345678 написал сообщение {msg.message_id}")


bot.infinity_polling()
