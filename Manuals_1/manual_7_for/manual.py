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
