a = 0
while a < 10:
    print("Печеньки шоколадные, ", a)
    a += 1
print("Цикл окончен")

a = 0
while a < 10:
    print("Печеньки шоколадные, ", a)
    if a == 5:
        break
    a += 1
print("Цикл окончен")

a = 0
while a < 10:
    a += 1
    if a == 5:
        continue
    print("Печеньки злаковые, ", a)
print("Цикл окончен")

km = int(input("Сколько километров будем ехать? -> "))
long = 0
while long != km:
    if long % 5 == 0:
        print(f"Мы проехали {long} км. Нам осталось {km - long} км.")
    long += 1
print("Ура! Мы доехали до города Б! Всего пройдено %s километров." % long)

numbers = []
while 5 > 1:
    num = int(input("Введите число -> "))
    if num == 0:
        break
    numbers.append(num)
print(f"Минимальное число в списке: {min(numbers)}")