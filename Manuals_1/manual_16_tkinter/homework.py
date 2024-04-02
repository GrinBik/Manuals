# ДЗ
# Добавить кнопку «Огонь» справа от дула, которая будет стрелять очередями по 5 патрон.
# Сделать выбор цвета пуль с помощью модуля tkinter.colorchooser.

import tkinter
import time
import random
from tkinter.colorchooser import askcolor


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
    for i in range(5):
        bullet = canvas.create_oval(5, 205, 45, 245, fill=color)
        b = (bullet, 10, random.random())
        bullets.append(b)


def ask_color(event):
    global color, hero
    color = askcolor(title="Выбери цвет")[1]
    canvas.delete(hero)
    hero = canvas.create_oval(5, 205, 45, 245, fill=color)


root = tkinter.Tk()
root.geometry("800x600")
root.title("Анимация")
root["bg"] = 'white'

canvas = tkinter.Canvas(root, width=650, height=600, bg="white")
canvas.pack(side=tkinter.LEFT, fill=tkinter.Y)

canvas.create_rectangle(0, 180, 40, 200, fill="black")
canvas.create_rectangle(0, 250, 40, 270, fill="black")

fire_btn = tkinter.Button(root, text='Огонь', font=('Arial', 25), command=shot)
fire_btn.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# canvas.create_window(20, 300, window=fire_btn)
color = 'red'

hero = canvas.create_oval(5, 205, 45, 245, fill=color)

h_x = 4
h_y = 0

bullets = []

root.bind_all('<w>', ask_color)

while True:
    root.update()
    root.update_idletasks()
    draw()
    time.sleep(0.01)
