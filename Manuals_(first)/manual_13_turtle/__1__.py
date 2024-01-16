import turtle


t = turtle.Pen()
screen = turtle.Screen()

screen.setup(600, 400)

screen.bgcolor("cyan")

screen.title("Привет, ребята!")

for x in range(300, 400, 8):
    t.forward(x / 5)
    t.left(x / 10)
    t.backward(29)

screen.clear()

turtle.mainloop()
