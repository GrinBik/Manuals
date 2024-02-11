# ДЗ
# Создать четыре ручки-черепашки зеленого, желтого, синего и красного цвета.
# Зелёная черепашка должна рисовать квадрат в верхнем левом углу.
# Желтая черепашка — вывести на экран солнце, используя метод заливки, в верхнем правом углу.
# Синяя черепашка в нижнем левом углу должна закрутить большую спираль.
# А красной черепахе нужно, используя форму кругов, в нижнем правом углу зациклиться в большой круг.
import turtle


# Создание ручки
t = turtle.Pen()
t.speed(150)

# Квадрат в верхнем левом углу
t.up()
t.goto(-200, 150)
t.down()
t.pencolor("green")
t.pensize(4)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# Солнце в верхнем правом углу
t.up()
t.goto(200, 100)
t.down()
t.pencolor('yellow')
t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()

# Спираль в нижнем левом углу
t.up()
t.goto(-150, -150)
t.down()
t.pencolor('blue')

for i in range(100):
    t.forward(i)
    t.left(50)

# Зацикленные круги ("пончик") в нижнем правом углу
t.up()
t.goto(250, -150)
t.down()
t.pencolor('red')

for i in range(15):
    t.circle(70)
    t.left(48)

turtle.mainloop()
