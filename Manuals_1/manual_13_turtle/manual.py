import turtle


t = turtle.Pen()

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("cyan")
screen.title("Привет, ребята!")

for x in range(300, 400, 8):
    t.forward(x / 5)
    t.left(x / 10)
    t.backward(29)
screen.clear()

screen.bgcolor("cyan")
t.setheading(0)
t.up()
t.goto(0, 0)
t.down()
t.hideturtle()
for x in range(300, 400, 8):
    t.forward(x / 5)
    t.left(x / 10)
    t.backward(29)
screen.clear()

screen.bgcolor("cyan")
t.up()
t.goto(0, 0)
t.down()
colors = ["red", "green", "orange", "blue"]
t.speed(150)
for x in range(50):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(91)
screen.clear()

screen.bgcolor("cyan")
t.up()
t.goto(0, 0)
t.down()
name = turtle.textinput('Введите свое имя', 'Как тебя зовут?')
for x in range(80):
    t.pencolor(colors[x % 4])
    t.write(name, font=('Arial', int((x + 4) / 4)))
    t.up()
    t.forward(x * 4)
    t.down()
    t.left(91)
screen.clear()

screen.bgcolor("black")
t.up()
t.goto(-100, 150)
t.down()
t.color('green')
t.speed(150)
t.hideturtle()
b = 0
while b < 200:
    t.right(b)
    t.forward(b * 3)
    b += 1

turtle.mainloop()
