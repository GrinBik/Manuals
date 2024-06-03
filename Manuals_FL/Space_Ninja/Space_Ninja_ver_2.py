import random
import time
import os
from threading import Timer


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


def stop(arg):
    print("\n\nТы неуспел...\n")
    time.sleep(2)
    print(f"\nИгра окончена (\n\nТы смог отразить {score} атак!")
    os._exit(arg)


timeout = 5
score = 0
print("Игра началась!\n")
time.sleep(1)
while True:
    t = Timer(timeout, stop, [1])
    alien = Alien()
    print(f"Ты встретил пришельца расы {alien.name}!\nЕго здоровье — {alien.hp}\nЕго урон — {alien.dmg}\n")
    time.sleep(2)
    action = alien.attack()
    print(f"Он наносит тебе удар {action}!\n")
    t.start()
    try:
        answer = input("У вас есть %d секунд чтобы ввести ответ...:" % timeout)
    finally:
        t.cancel()
    if answer.lower() != action.lower():
        print("\nТы промахнулся!")
        time.sleep(2)
        break
    print("\nТы парировал удар и пришелец убежал!\n")
    time.sleep(2)
    score += 1
    print(f"Твой счёт — {score}\n")
    time.sleep(2)

print(f"\nИгра окончена (\n\nТы смог отразить {score} атак!")
