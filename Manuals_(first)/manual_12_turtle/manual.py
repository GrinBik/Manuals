import turtle


t = turtle.Pen()

t.fillcolor('yellow')
t.begin_fill()

t.forward(200)
t.backward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.end_fill()

t.shape('turtle')
# circle, square, triangle, arrow, turtle

t.color('green')
# red, green, blue, white, black, violet ...

t.pensize(4)

t.up()
t.goto(-100, -150)
t.down()

t.speed(150)

t.circle(100)

turtle.mainloop()
