import turtle


t = turtle.Pen()

t.hideturtle()

for x in range(300, 400, 8):
    t.forward(x / 5)
    t.left(x / 10)
    t.backward(29)

turtle.mainloop()
