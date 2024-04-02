def function():
    print("Функция работает!")


def search():
    num = words.count("клубника")
    if num != 0:
        print("Клубника найдена")
    else:
        print("В списке нет никаких клубник")


def math(number):
    answer = number * 10
    return f"Ответ: {answer}"


def square(a, b):
    value = a * b
    return value


def cube(num):
    result = square(num, num) * 6
    return result


function()

words = ['Идет', 'бычок,', 'качается, вздыхает', 'на',
         'ходу', 'ох,', 'доска', 'кончается', 'сейчас', 'я', 'упаду']

while True:
    new = input("Введи новое слово -> ")
    words.append(new)
    search()
    if new == 'stop':
        break

x = int(input('Введите число -> '))
math(x)
ans = math(x)
print(ans)

print(cube(3))
