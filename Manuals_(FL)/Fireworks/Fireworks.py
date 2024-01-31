import time
import turtle
import random


# Отрисовка звезды
def create_star():
    # Скорость возникновения звезды должна быть максимальной
    t.speed(150)
    # Выбор случайного цвета звезды
    choice = random.choice(colors)
    t.color(choice)
    # Отрисовка звезды
    t.begin_fill()
    for x in range(17):
        t.forward(STAR_SIZE)
        t.right(190)
    t.end_fill()


# Запуск партии фейерверков
def start_firework(reply_number):
    # Запуск фейерверков reply_number раз
    for i in range(reply_number):
        # Перенос ручки на случайное место нижней грани экрана
        t.penup()
        t.goto(random.randint(LEFT_LIMIT, RIGHT_LIMIT), BOTTOM_LIMIT)
        t.pendown()
        # Ручка должна смотреть ровно вверх
        t.setheading(90)
        # При запуске цвет должен быть черным, а скорость должна быть заметной
        t.pencolor('black')
        t.speed(4)
        # Отрисовка пунктира (запуск фейерверка)
        for j in range(12):
            t.forward(20)
            t.penup()
            t.forward(20)
            t.pendown()
        # Отрисовка звезды
        create_star()
        # Фиксация результата
        time.sleep(3)
        # Очистка холста
        t.clear()


# Создание ручки
t = turtle.Pen()
t.shape('arrow')
t.speed(150)

# Настройка экрана
screen = turtle.Screen()
WIDTH = 800
HEIGHT = 600
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('dark blue')

# Константы для хранения пределов возникновения фейерверка, цвета и размера звезды
colors = ['Yellow', 'Aqua', 'Red', 'Gold', 'Orange', 'Green', 'Lime', 'Cyan', 'Blue',
          'Brown', 'Grey', 'Purple', 'Violet', 'Pink']
STAR_SIZE = 70
LEFT_LIMIT = int(-WIDTH / 2 + STAR_SIZE)
RIGHT_LIMIT = int(WIDTH / 2 - STAR_SIZE)
BOTTOM_LIMIT = int(-HEIGHT / 2)

# Запуск нужного кол-ва фейерверков
while True:
    firework_number = turtle.textinput('Количество фейерверков в партии', "Введите сколько будет залпов?")
    try:
        firework_number = int(firework_number)
    except ValueError:
        continue
    else:
        if firework_number != 0:
            start_firework(firework_number)
        else:
            break

# Автоматическое закрытие окна при завершении запуска фейерверков
turtle.bye()
