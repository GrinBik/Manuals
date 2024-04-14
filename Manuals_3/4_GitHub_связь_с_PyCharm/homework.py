# Превратить игру в сложение строк.
# Пусть слова выбираются случайно из большого списка.
# Требуется реализовать:
# создание списка слов, возможность добавления в него слов и удаления;
# перемешивание списка слов;
# На каждом этапе производить коммит изменения и писать соответствующий комментарий.
import random


# Создание начального списка
def create_words():
    global words
    words = ['привет', 'как', 'дела', 'у', 'меня', 'хорошо', 'нормально', 'скучно', 'солнечно', 'дождь']


# Добавление нового слова в список
def add_word(word):
    global words
    words.append(word)


# Удаление слова из списка
def remove_word(word):
    global words
    words.remove(word)


# Перемешивание списка слов
def change_words():
    global words
    random.shuffle(words)


def show_commands():
    print('- Добавить слово в список команда: "add <новое_слово>"\n'
          '- Удалить слово из списка команда: "remove <слово>"\n'
          '- Перемешать слова команда: "shuffle"\n'
          '- Для вывода возможных команд: "commands"\n'
          'Игра!')


def show_result():
    print(f'Счёт: {points["player"]}:{points["comp"]}')


points = {
    "comp": 0,
    "player": 0
}

words = []

show_result()

while True:
    create_words()
    a = random.choice(words)
    b = random.choice(words)
    user = input(f"Какие 2 слова спрятаны в: {a}{b} = ")
    if user == f'{a} {b}':
        print("Верно!")
        points["player"] += 1
        show_result()
    elif "add " in user:
        add_word(user.split(' ')[1])
    elif "remove " in user:
        remove_word(user.split(' ')[1])
    elif "shuffle" in user:
        change_words()
    elif "commands" in user:
        show_commands()
    else:
        print("Ты ошибся. Попробуй ещё разочек.")
        points["comp"] += 1
        show_result()
