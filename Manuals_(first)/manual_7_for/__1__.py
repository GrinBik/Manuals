print(list(range(30)))

print(list(range(15, 30)))

print(list(range(15)))
print(list(range(0, 25, 7)))

for x in range(10):
    print(x)

to_buy = ["Сыр", "Колбаса", "Хлебушек", "Листья салата", "Соус"]
for x in to_buy:
    print(x)

for x in range(10, 0, -1):
    print(x)
print("Поехали!")

numbers = [35, 35, 46, 464, 5, 234, 645, 64, 56, 343]
maximal = numbers[0]
for num in numbers:
    if num > maximal:
        maximal = num
print(maximal)

# ДЗ
# 1. Создать список из случайных цифр. С помощью цикла найти самое маленькое число из этого списка.
# 2. Создать список из случайных слов. С помощью цикла найти самое короткое слово из этого списка.
# Чтобы найти длину слова, использовать функцию len(). Пример использования функции: name = "Саша", print(len(name))

numbers = [1, 3, 6, 34, 2, 43, 45, 234, 56, 23, 65, 23, 65, 20, 29, 28, 72, 93, 85]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(minimum)

words = ['пельмени', 'картошка', 'свинина', 'доширак', 'пицца', 'спагетти', 'рис', 'поп-корн']
short = words[0]
for word in words:
    if len(short) > len(word):
        short = word
print(short)
