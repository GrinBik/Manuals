import random
import time
import datetime
import my_modul


a = random.randint(0, 10)
print(a)

shop = ["молоко", "колбаса", "сыр"]
ch = random.choice(shop)
print(ch)

print(1)
time.sleep(2)
print(3)

print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

dictionary = {
    "Слива": "12 ккал",
    "Банан": "120 ккал",
    "Яблоко": "54 ккал",
    "Snickers": "132 ккал"
}
keys = list(dictionary.keys())
rnd = random.choice(keys)
print("%s: %s" % (rnd, dictionary[rnd]))

maximum = int(input("Введи количество секунд: "))
timer = 0
while timer != maximum:
    print("Прошла 1 секунда. Осталось", maximum - timer, "секунд.")
    time.sleep(1)
    timer += 1
print("Дзынь-Дзынь")

print(my_modul.test)
