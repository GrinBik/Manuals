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
        if line == 'roulette':
            root.bind_all("<1>", record_start_point)
            root.bind_all("<B3-Motion>", draw_line)
            root.bind_all("<3>", None)
        else:
            root.bind_all('<1>', paint)
            root.bind_all("<3>", erase)
            root.bind_all("<B3-Motion>", erase)


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
        canvas.create_rectangle(event.x - brush, event.y - brush,
                                event.x + brush, event.y + brush,
                                fill=color, outline=color)
    elif state == "line1":
        canvas.create_line(event.x - brush, event.y - brush,
                           event.x + brush, event.y + brush, fill=color, width=brush)
    elif state == "line2":
        canvas.create_line(event.x + brush, event.y - brush,
                           event.x - brush, event.y + brush, fill=color, width=brush)


def erase(event):
    canvas.create_oval(event.x - brush * 2, event.y - brush * 2,
                       event.x + brush * 2, event.y + brush * 2,
                       fill="white", outline="white")


def ask_color(event):
    global color
    color_code = askcolor(title="Выбери цвет")
    color = color_code[1]
    size.configure(fg=color)


def record_start_point(event):
    global start_point, previous_line
    start_point = (event.x, event.y)
    previous_line = None  # Очищаем предыдущую линию при новом клике


def draw_line(event):
    global start_point, previous_line
    if start_point:
        if previous_line:
            canvas.delete(previous_line)  # Удаляем предыдущую линию
        line_id = canvas.create_line(start_point[0], start_point[1], event.x, event.y, width=brush)
        previous_line = line_id


root = tkinter.Tk()
root.geometry("600x520")
root.title("Рисовалка")
root["bg"] = 'gray75'
canvas = tkinter.Canvas(root, width=540, height=450, bg="white")
canvas.pack(side=tkinter.LEFT, fill=tkinter.Y)

state = "circle"

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
minus_btn.pack(side=tkinter.TOP, fill=tkinter.X)

brush = 10
color = "black"

start_point = None
previous_line = None

size = tkinter.Label(root, text=brush, fg=color, font=(None, 32))
size.pack(side=tkinter.TOP, fill=tkinter.X)

roulette_btn = tkinter.Button(root, text="рулетка", font=(None, 8), command=lambda: choose("roulette"))
roulette_btn.pack(side=tkinter.TOP)

canvas.bind_all("<w>", ask_color)
root.bind_all("<B1-Motion>", paint)

root.mainloop()
