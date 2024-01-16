# IT-корпорации требуется программа проверки умных светильников.
# Напиши программу, эмулирующую работу двух умных лампочек с использованием модуля tkinter.
# Создай родительский класс и два класса: Lamp и Sconce.
# Lamp будет описывать умные лампочки, вкручиваемые в потолочные светильники или люстры,
# а Sconce — настенные бра-светильники.
# Лампы должны иметь имя, цвет свечения и яркость, а также методы изменения этих параметров.

# Лампы должны управляться через поле ввода и реагировать на команды по типу:
# «Лампа 1 цвет red» и «Лампа 2 яркость 10». Цвет и яркость ламп меняется плавно!
# Экземпляры Lamp должны иметь функцию ночника (мягкий теплый свет и плавное затухание),
# а экземпляры Sconce режим тревоги (красный).
# Tkinter должен рисовать в середине экрана каждую лампу с её именем внутри.
import tkinter
import time


class Home:
    def __init__(self):
        self.name = None
        self.color = (255, 255, 255)
        self.brightness = 100
        self.id = canvas.create_oval(40, 40, 190, 190, width=2, fill=to_hex(self.color))

    def get_color(self):
        color = canvas.itemcget(self.id, "fill")
        return to_rgb(color)

    def set_color(self, color):
        self.color = to_rgb(to_hex(color))

    def on(self):
        if self.get_color() == self.color:
            return
        nr, ng, nb = to_rgb(to_hex(self.color))
        lr, lg, lb = self.get_color()

        if nr > lr:
            lr += 3
        elif nr < lr:
            lr -= 3
        else:
            pass
        if ng > lg:
            lg += 3
        elif ng < lg:
            lg -= 3
        else:
            pass

        if nb > lb:
            lb += 3
        elif nb < lb:
            lb -= 3
        else:
            pass

        canvas.itemconfigure(self.id, fill=to_hex((lr, lg, lb)))

    def set_brightness(self, bright):
        if bright == 100:
            return
        lr, lg, lb = self.color
        rgb = lr * bright / 100, lg * bright / 100, lb * bright / 100
        self.color = tuple(map(int, rgb))

    def set_brightness(self, bright):
        if bright == 100:
            return
        lr, lg, lb = self.color
        rgb = lr * bright / 100, lg * bright / 100, lb * bright / 100
        self.color = tuple(map(int, rgb))


class Lamp(Home):
    def __init__(self, name:str):
        super().__init__()
        self.name = name.lower()
        self.text = canvas.create_text(115, 115, text=self.name.title(), font=(None, 18))

    def sleep(self):
        self.set_color("yellow")
        self.set_brightness(50)


class Sconce(Home):
    def __init__(self, name):
        super().__init__()
        self.name = name.lower()
        canvas.move(self.id, 200, 0)
        self.text = canvas.create_text(315, 115, text=self.name.title(), font=(None, 18))

    def alarm(self):
        self.set_color("red")


def inp():
    data = entry.get().lower()
    commands = data.split(" ")
    if len(commands) < 3:
        return
    name, task, value = list(map(str.lower, commands))
    if name not in lamps:
        return
    aim = lamps[name]
    if task == "цвет":
        aim.set_color(value)
    elif task == "яркость":
        aim.set_brightness(int(value))
    else:
        return


def to_hex(rgb):
    if type(rgb) is str:
        color = list(root.winfo_rgb(rgb))
        for n, c in enumerate(color):
            color[n] = c // 257
        r, g, b = color
    else:
        r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def to_rgb(hexa):
    hexa = hexa[1:]
    return tuple(int(hexa[i:i + 2], 16) for i in (0, 2, 4))


root = tkinter.Tk()
root.geometry('800x600')
root.resizable(0, 0)
root.title('Умный дом')

entry = tkinter.Entry(root, width=50, font=(None, 16), justify="right")
entry.grid(row=0, column=0, sticky="E")

btn = tkinter.Button(root, text="Ввод", command=inp)
btn.grid(row=0, column=1, sticky="W")

canvas = tkinter.Canvas(width=700, height=600)
canvas.grid(row=1, columnspan=2)

l = Lamp("Лампа")
s = Sconce("Бра")
lamps = {}
for lamp in (l, s):
    lamps[lamp.name] = lamp

while True:
    root.update()
    root.update_idletasks()
    l.on()
    s.on()
    time.sleep(0.01)
