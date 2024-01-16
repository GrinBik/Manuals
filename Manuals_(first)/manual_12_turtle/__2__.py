import turtle


t = turtle.Pen()

t.fillcolor('yellow')
t.begin_fill()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.end_fill()

t.up()
t.goto(-100, -150)
t.down()

t.speed(150)

t.circle(100)

turtle.mainloop()
