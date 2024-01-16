# ДЗ
# Добавить кнопку «Огонь» справа от дула,
# которая будет стрелять очередями по 5 патрон.
# Сделай выбор цвета пуль
# с помощью модуля tkinter.colorchooser.
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
    global bullets, bull_num
    bullet = canvas.create_oval(5, 205, 45, 245, fill=main_color)
    b = (bullet, 10, random.random())
    bullets.append(b)
    if bull_num < 5:
        root.after(50, shot)
        bull_num += 1


def set_color(event):
    global main_color
    color_code = askcolor(title="Выбери цвет")
    main_color = color_code[1]
    canvas.itemconfig(hero, fill=main_color)


def fire():
    global bull_num
    bull_num = 0
    shot()


root = tkinter.Tk()
root.geometry("800x600")
root.title("Анимация")
root["bg"] = 'white'

canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
canvas.pack(side=tkinter.RIGHT, fill=tkinter.Y)

canvas.create_rectangle(0, 180, 40, 200, fill="black")
canvas.create_rectangle(0, 250, 40, 270, fill="black")

hero = canvas.create_oval(5, 205, 45, 245, fill="red")

h_x = 4
h_y = 0

bullets = []

bull_num = 5
main_color = 'red'

root.geometry('900x600')
fire_btn = tkinter.Button(root, text='Огонь', font=('Arial', 15), command=fire)
fire_btn.pack(side=tkinter.LEFT, fill=tkinter.Y)

canvas.bind_all("<w>", set_color)

shot()
while True:
    root.update()
    root.update_idletasks()
    draw()
    time.sleep(0.01)
