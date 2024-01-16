to_buy = ['Мука', 'Сахар', 'Яблоки']

to_buy = [435, "Сахар", True, 245.516]
cell = [349 * 45, 34 + 11]

print(to_buy[0])
print(to_buy[1: 3])

to_buy = [435, "Caxap", True, 245.516]
print(to_buy)
to_buy[1] = "Соль"
print(to_buy)

shop = ["Аты-баты", "Шли солдаты", "Аты-Баты"]
shop.append("Hа базар")
print(shop)

shop = ["Аты-Баты", "Шли солдаты"]
del shop[0]
print(shop)

to_buy = (435, "Сахар", True, 245.516)
print(to_buy)
# to_buy[1] = "Соль"
# print(to_buy)

to_buy = ["Мука", "Сахар", "Яблоки", "Какао", "Апельсины"]
print(to_buy[2:5])

to_buy = ("Мука", "Сахар", "Яблоки")
print(to_buy[0])
# to_buy[0] = "Maндарины"
# print(to_buy[0])

# ДЗ
# Составить список из 5 текстовых значений (тип данных string).
# Вывести на консоль каждую первую букву каждого элемента списка.
# Подсказка: нужно будет ставить две пары квадратных скобок (data[][]).

menu = ['Пельмени', 'Паста', 'Картошка', 'Мясо', 'Рыба']
print(menu[0][0])
print(menu[1][0])
print(menu[2][0])
print(menu[3][0])
print(menu[4][0])
