import time


maximum = int(input("Введи количество секунд: "))
timer = 0
while timer != maximum:
    print("Прошла 1 секунда. Осталось", maximum - timer, "секунд.")
    time.sleep(1)
    timer += 1
print("Дзынь-Дзынь")
