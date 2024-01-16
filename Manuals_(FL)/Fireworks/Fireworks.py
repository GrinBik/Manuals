import random
import turtle


def create_star():
    t.hideturtle()
    t.speed(100)
    t.fillcolor(choice)
    t.begin_fill()
    for x in range(20):
        t.forward(90)
        t.right(190)
    t.end_fill()
    t.shape('arrow')
    t.setheading(90)
    t.speed(50)


colors = ['Yellow', 'Aqua', 'Red', 'Gold', 'Orange', 'Green', 'Lime', 'Cyan', 'Blue',
          'Brown', 'Grey', 'Purple', 'Violet', 'Pink']
choice = ''
t = turtle.Pen()
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('firebrick4')
t.setheading(90)

for i in range(40):
    t.shape('arrow')
    choice = random.choice(colors)
    t.pencolor(choice)
    t.speed(100)
    t.hideturtle()
    t.penup()
    t.goto(random.randint(-290, 290), -290)
    t.pendown()
    t.speed(50)

    t.shape('arrow')
    for j in range(50):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()
    t.clear()

    create_star()

turtle.mainloop()
