# ДЗ
# Создать модуль, заполнить его функциями сложения и вычитания.
# Импортировать этот модуль в другую программу. Написать с помощью условных конструкций и этих функций
# программу калькулятора - запрашивать два числа и оператор у пользователя и выводить ответ в консоль.
import __7__


number1 = int(input("Введите первое число: "))
operator = input("Введите оператор: ")
number2 = int(input("Введите первое число: "))
if operator == "+":
    print(__7__.plus(number1, number2))
elif operator == '-':
    print(__7__.minus(number1, number2))
else:
    print('Оператор не распознан')
