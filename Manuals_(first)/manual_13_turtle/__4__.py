import turtle


t = turtle.Pen()
screen = turtle.Screen()

screen.setup(1000, 800)
screen.bgcolor("black")
screen.title('Прыжок в прошлое')

colors = ["red", "green", "orange", "blue"]

name = turtle.textinput('Введите свое имя', 'Как тебя зовут?')

t.speed(150)
t.hideturtle()

for x in range(80):
    t.pencolor(colors[x % 4])
    t.write(name, font=('Arial', int((x + 4) / 4)))
    t.up()
    t.forward(x * 4)
    t.down()
    t.left(91)

turtle.mainloop()
