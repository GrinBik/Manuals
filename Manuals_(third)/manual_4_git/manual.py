import random

points = {
    "comp": 0,
    "player": 0
}


def is_odd(number: int):
    if number % 2 == 0:
        return False
    else:
        return True


while True:
    a = random.randint(10, 110)
    while not is_odd(a):
        a = random.randint(10, 110)
    b = random.randint(10, 120)
    while not is_odd(b):
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
