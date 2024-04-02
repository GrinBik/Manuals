# IT-корпорации требуется программа проверки умных светильников.
# Напиши программу, эмулирующую работу двух умных лампочек с использованием модуля tkinter.
# Создай родительский класс и два класса: Lamp и Sconce.
# Lamp будет описывать умные лампочки, вкручиваемые в потолочные светильники или люстры,
# а Sconce — настенные бра-светильники.
# Лампы должны иметь имя, цвет свечения и яркость, а также методы изменения этих параметров.
import tkinter


class Home:
    def __init__(self):
        self.name = None
        self.color = "white"
        self.brightness = 100
        self.id = canvas.create_oval(40, 40, 190, 190, width=2, fill=self.color)

    def set_color(self, color):
        self.color = color
        canvas.itemconfigure(self.id, fill=self.color)

    def set_brightness(self, bright):
        self.brightness = bright


class Lamp(Home):
    def __init__(self, name):
        super().__init__()
        self.name = name.lower()
        self.text = canvas.create_text(115, 115, text=self.name.title(), font=(None, 18))


class Sconce(Home):
    def __init__(self, name):
        super().__init__()
        self.name = name.lower()
        canvas.move(self.id, 200, 0)
        self.text = canvas.create_text(315, 115, text=self.name.title(), font=(None, 18))


root = tkinter.Tk()
root.geometry('800x600')
root.resizable(0, 0)
root.title('Умный дом')
canvas = tkinter.Canvas(root, width=800, height=600, bg='aqua')
canvas.pack()

l = Lamp("Лампа")
s = Sconce("Бра")

l.set_color("blue")
s.set_color("lime")

root.mainloop()
