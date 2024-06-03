import datetime
import random
import time


class Alien:
    races = {
        'Alien': (100, 100),
        'Martian': (100, 100),
        'Covenant': (100, 100),
        'Grox': (100, 100),
        'Klisany': (100, 100),
        'Vortigaunt': (100, 100),
        'Strict': (100, 100),
        'Sectoid': (100, 100),
        'Cephas': (100, 100),
        'Necromorph': (100, 100),
        'Zerg': (100, 100),
        'Azari': (100, 100)
    }

    def __init__(self):
        self.name = random.choice(tuple(self.races.keys()))
        self.hp = self.races[self.name][0]
        self.dmg = self.races[self.name][1]

    def attack(self):
        side = ("Справа", "Слева", "Сверху", "Снизу")
        words = ("Абракадабра", "Параллельные", "Катманду", "Йошкар-Ола", "Параллелепипед")
        action = random.choice(random.choice((side, words)))
        return action


def timestamp():
    now = datetime.datetime.now().timestamp()
    return now


score = 0
print("Игра началась!")
time.sleep(1)
while True:
    alien = Alien()
    print(f"Ты встретил пришельца расы {alien.name}!\nЕго здоровье — {alien.hp}\nЕго урон — {alien.dmg}")
    time.sleep(2)
    action = alien.attack()
    print(f"Он наносит тебе удар {action}!")
    time1 = timestamp()
    answer = input()
    time2 = timestamp()
    if answer.lower() != action.lower():
        print("Ты промахнулся!")
        time.sleep(2)
        break
    if time2 - time1 >= 5:
        print("Ты неуспел!")
        time.sleep(2)
        break
    print("Ты парировал удар и пришелец убежал!")
    time.sleep(2)
    score += 1
    print(f"Твой счёт — {score}")
    time.sleep(2)

print("Игра окончена (")
