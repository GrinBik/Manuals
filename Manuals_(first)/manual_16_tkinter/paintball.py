import tkinter
import time
import random


def draw():
    global h_x, h_y
    for bull in bullets:
        bullet = bull[0]
        h_x = bull[1]
        h_y = bull[2]
        x, y, x1, y1 = canvas.coords(bullet)
        canvas.move(bullet, h_x, h_y)
        if x1 >= 800:
            canvas.delete(bullet)
            bullets.remove(bull)


def shot():
    global bullets
    bullet = canvas.create_oval(5, 205, 45, 245, fill='red')
    b = (bullet, 10, random.random())
    bullets.append(b)
    root.after(50, shot)


root = tkinter.Tk()
root.geometry("800x600")
root.title("Анимация")
root["bg"] = 'white'

canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

canvas.create_rectangle(0, 180, 40, 200, fill="black")
canvas.create_rectangle(0, 250, 40, 270, fill="black")

hero = canvas.create_oval(5, 205, 45, 245, fill="red")

h_x = 4
h_y = 0

bullets = []

shot()
while True:
    root.update()
    root.update_idletasks()
    draw()
    time.sleep(0.01)
