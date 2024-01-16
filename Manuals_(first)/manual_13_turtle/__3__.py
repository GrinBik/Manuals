import turtle


t = turtle.Pen()
screen = turtle.Screen()

screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Спираль")

colors = ["red", "green", "orange", "blue"]

t.speed(150)
t.hideturtle()

for x in range(50):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(91)

turtle.mainloop()
