# ДЗ
# Создать холст черного цвета с параметрами (1000, 800) и с названием "Ракушка”.
# Белой ручкой, используя цикл for, нарисовать на чёрном холсте морскую ракушку.
import turtle


t = turtle.Pen()
screen = turtle.Screen()

screen.setup(1000, 800)
screen.bgcolor("black")
screen.title('Ракушка')

t.color('white')
t.speed(150)
t.hideturtle()

for i in range(81):
    t.circle(i * 2.7)
    t.left(4)

turtle.mainloop()
