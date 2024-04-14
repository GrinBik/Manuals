# Модернизировать программу таким образом, чтобы игра продолжалась только с нечётными числами.
# Написать функцию, которая будет отсеивать чётные числа из игры.
# Сделать коммит изменений и загрузить их в GitHub (сделать все через pyCharm).
import random

points = {
    "comp": 0,
    "player": 0
}


def is_even_number(number: int):
    if number % 2 == 0:
        return True
    else:
        return False


while True:
    a = random.randint(10, 110)
    while is_even_number(a):
        a = random.randint(10, 110)
    b = random.randint(10, 120)
    while is_even_number(b):
        b = random.randint(10, 110)
    op = random.choice(("+", "-"))
    if op == "+":
        ans = a + b
        user = input(f"{a} + {b} = ")
    else:
        ans = a - b
        user = input(f"{a} - {b} = ")
    if user == str(ans):
        print("Верно!")
        points["player"] += 1
    else:
        print("Ты ошибся. Попробуй ещё разочек.")
        points["comp"] += 1
    print(f'Счёт: {points["player"]}:{points["comp"]}')
