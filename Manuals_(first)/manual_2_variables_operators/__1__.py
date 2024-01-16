apple = 4

a = 10
sasha = 12
doggy = 14
kilos = 7

gravity = 9.8
pi = 3.14
apple = 0.5
android = 13.4

name = "Саша"
color = "Красный"

name = 'Katya'
second = 'Ivanova'
data = 'Сегодня 31 декабря! С наступающим!'

a = True
a = False

print(type(name))

name = input()
print(name)

a = 5
print(a + 3)
a = 10 / 2
print(a)

print(5 / 2)
print(5 // 2)

print(5 / 2)
print(5 % 2)

apple = 5
apple += 3
print(apple)

sklad = 0
for_day = 15000 - 13500
sklad += for_day + for_day + for_day + for_day + for_day + for_day + for_day
print(sklad)

sklad = 0
for_day = 15000 - 13500
sklad += for_day * 7
print(sklad)

stroka = '34'
print(type(int(stroka)))

age = input()
age = int(age)
print(2023 - age)

num = 'Четыре'
apples = 'яблока'
print(num + apples)

# ДЗ
# 1. С помощью переменных вычислить количество секунд в одном году и вывести результат на консоль
# с помощью функции print().
# 2. Создать 3 переменные для Имени, Фамилии и Отчества.
# Пусть данные вводятся в них через консоль.
# После сложить эти переменные так, чтобы получилось полное ФИО и вывести результат на экран.

seconds = 0
seconds += 60 * 60 * 24 * 365
print(seconds)

name = input('Какое ваше имя? ')
surname = input('Какая ваша фамилия? ')
lastname = input('Какое ваше отчество? ')
print(name + " " + surname + " " + lastname)
