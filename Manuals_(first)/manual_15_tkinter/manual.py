import tkinter
from tkinter.colorchooser import askcolor


def choose(line):
    global state, brush
    if line == 'plus' and brush < 99:
        brush += 1
        size.configure(text=brush)
    elif line == 'minus' and brush > 0:
        brush -= 1
        size.configure(text=brush)
    else:
        state = line


def paint(event):
    global brush
    if event.widget.__class__ is not tkinter.Canvas:
        return
    if state == "circle":
        canvas.create_oval(event.x - brush,
                           event.y - brush,
                           event.x + brush,
                           event.y + brush,
                           fill=color,
                           outline=color)
    elif state == "square":
        canvas.create_rectangle(event.x - brush,
                                event.y - brush,
                                event.x + brush,
                                event.y + brush,
                                fill=color,
                                outline=color)
    elif state == "line1":
        canvas.create_line(event.x - brush,
                           event.y - brush,
                           event.x + brush,
                           event.y + brush,
                           fill=color)
    elif state == "line2":
        canvas.create_line(event.x + brush,
                           event.y - brush,
                           event.x - brush,
                           event.y + brush,
                           fill=color)


def erase(event):
    canvas.create_oval(event.x - brush,
                       event.y - brush,
                       event.x + brush,
                       event.y + brush,
                       fill="white",
                       outline="white")


def ask_color(event):
    global color
    color = askcolor(title="Выбери цвет")[1]
    size.configure(fg=color)


root = tkinter.Tk()

root.geometry("600x450")
root.title("«Рисовалка»")
root["bg"] = 'gray'

canvas = tkinter.Canvas(root, width=540, height=450, bg="white")
canvas.pack(side=tkinter.LEFT, fill=tkinter.Y)

square_btn = tkinter.Button(root, text="🟥", font=(None, 20), command=lambda: choose('square'))
square_btn.pack(side=tkinter.TOP)

circle_btn = tkinter.Button(root, text="🔴", font=(None, 20), command=lambda: choose("circle"))
circle_btn.pack(side=tkinter.TOP, )

line1_btn = tkinter.Button(root, text=" ↘ ", font=(None, 20), command=lambda: choose("line1"))
line1_btn.pack(side=tkinter.TOP, )

line2_btn = tkinter.Button(root, text=" ↙ ", font=(None, 20), command=lambda: choose("line2"))
line2_btn.pack(side=tkinter.TOP, )

plus_btn = tkinter.Button(root, text="➕", font=(None, 20), command=lambda: choose("plus"))
plus_btn.pack(side=tkinter.TOP, )

minus_btn = tkinter.Button(root, text="➖", font=(None, 20), command=lambda: choose("minus"))
minus_btn.pack(side=tkinter.TOP, )

state = "circle"
brush = 10
color = 'black'

size = tkinter.Label(root, text=brush, fg=color, font=(None, 32))
size.pack(side=tkinter.TOP, )

root.bind_all('<1>', paint)
root.bind_all("<B1-Motion>", paint)

root.bind_all("<3>", erase)
root.bind_all("<B3-Motion>", erase)

canvas.bind_all("<w>", ask_color)
# canvas.bind_all("<2>", ask_color) - у меня не работает средняя кнопка

root.mainloop()
