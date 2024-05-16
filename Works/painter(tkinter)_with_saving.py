import tkinter
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfile
from PIL import ImageGrab, Image
from tkinter.filedialog import asksaveasfile


# Сохранение в файл формата ".jpg"
def save_file():
    # Доступные форматы файлов
    files = [('Image Files', '*.jpg'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt'),
             ('All Files', '*.*')]
    # Диалоговое окно по выбору файла для сохранения
    file_name = asksaveasfile(filetypes=files, defaultextension='*.jpg').name
    # Левая верхняя координата по X и Y
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    # Правая нижняя координата по X и Y
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    # Сохранение
    ImageGrab.grab().crop((x, y, x1, y1)).save(file_name)


# Сохранение новой формы ручки
def change_form(new_form):
    global form, thickness
    # Если нажаты кнопки управления толщиной пера
    if new_form == 'plus' and thickness < 99:
        thickness += 1
        size.configure(text=thickness)
    elif new_form == 'minus' and thickness > 0:
        thickness -= 1
        size.configure(text=thickness)
    # Сохранение выбранной формы пера
    else:
        form = new_form


# Рисование
def draw(event):
    global thickness
    # Если рисование вне холста, то никакой реакции
    if event.widget.__class__ is not tkinter.Canvas:
        return
    # Рисование формой "круг"
    if form == "circle":
        canvas.create_oval(event.x - thickness,
                           event.y - thickness,
                           event.x + thickness,
                           event.y + thickness,
                           fill=color,
                           outline=color)
    # Рисование формой "квадрат"
    elif form == "square":
        canvas.create_rectangle(event.x - thickness,
                                event.y - thickness,
                                event.x + thickness,
                                event.y + thickness,
                                fill=color,
                                outline=color)
    # Рисование формой "линия 1"
    elif form == "line1":
        canvas.create_line(event.x - thickness,
                           event.y - thickness,
                           event.x + thickness,
                           event.y + thickness,
                           fill=color)
    # Рисование формой "линия 2"
    elif form == "line2":
        canvas.create_line(event.x + thickness,
                           event.y - thickness,
                           event.x - thickness,
                           event.y + thickness,
                           fill=color)


# "Ластик" формы "круг"
def erase(event):
    canvas.create_oval(event.x - thickness,
                       event.y - thickness,
                       event.x + thickness,
                       event.y + thickness,
                       fill="white",
                       outline="white")


# Палитра
def ask_color(event):
    global color
    color = askcolor(title="Выбери цвет")[1]
    size.configure(fg=color)


# Очистка всего холста
def canvas_clear(event):
    canvas.delete('all')


# Окно
root = tkinter.Tk()
root.geometry("800x600")
root.title("«Рисовалка»")
root["bg"] = 'gray'
root.resizable(0, 0)

# Холст
canvas = tkinter.Canvas(root, width=700, height=600, bg="white")
canvas.pack(side=tkinter.LEFT, fill=tkinter.Y)

# Кнопка "квадрат"
square_btn = tkinter.Button(root, text="🟥", font=(None, 20), command=lambda: change_form('square'))
square_btn.pack(side=tkinter.TOP, fill=tkinter.X)
# Кнопка "круг"
circle_btn = tkinter.Button(root, text="🔴", font=(None, 20), command=lambda: change_form("circle"))
circle_btn.pack(side=tkinter.TOP, fill=tkinter.X)
# Кнопка "линия 1"
line1_btn = tkinter.Button(root, text=" ↘ ", font=(None, 20), command=lambda: change_form("line1"))
line1_btn.pack(side=tkinter.TOP, fill=tkinter.X)
# Кнопка "линия 2"
line2_btn = tkinter.Button(root, text=" ↙ ", font=(None, 20), command=lambda: change_form("line2"))
line2_btn.pack(side=tkinter.TOP, fill=tkinter.X)
# Кнопка "плюс"
plus_btn = tkinter.Button(root, text="➕", font=(None, 20), command=lambda: change_form("plus"))
plus_btn.pack(side=tkinter.TOP, fill=tkinter.X)
# Кнопка "минус"
minus_btn = tkinter.Button(root, text="➖", font=(None, 20), command=lambda: change_form("minus"))
minus_btn.pack(side=tkinter.TOP, fill=tkinter.X)
# Кнопка очистки всего холста
clear_btn = tkinter.Button(root, text="C", font=(None, 20), command=lambda: canvas_clear("<BackSpace>"))
clear_btn.pack(side=tkinter.TOP, fill=tkinter.BOTH)

# Форма пера
form = "circle"
# Толщина пера
thickness = 10
# Цвет пера
color = 'black'

# Актуальная толщина пера и его цвет
size = tkinter.Label(root, text=thickness, fg=color, font=(None, 32))
size.pack(side=tkinter.TOP, fill=tkinter.X)

# Поле ввода названия файла для сохранения в него
filename = tkinter.Entry(root)
filename.pack(side=tkinter.TOP, fill=tkinter.X)

# Кнопка сохранения
save_btn = tkinter.Button(root, text="Save", font=(None, 20), command=save_file)
save_btn.pack(side=tkinter.TOP, fill=tkinter.BOTH)

# Левая кнопка мыши - рисование
root.bind_all('<1>', draw)
root.bind_all("<B1-Motion>", draw)
# Правая кнопка мыши - "ластик"
root.bind_all("<3>", erase)
root.bind_all("<B3-Motion>", erase)
# Кнопка "с" - палитра
canvas.bind_all("<c>", ask_color)
# Кнопка очистки всего холста
canvas.bind_all("<BackSpace>", canvas_clear)

root.mainloop()
