import turtle


t = turtle.Pen()
screen = turtle.Screen()

screen.setup(1000, 800)
screen.bgcolor("black")
screen.title('Вирус')

t.up()
t.goto(0, 200)
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
