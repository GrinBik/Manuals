# ДЗ
# Создай класс мячика со всеми
# необходимыми атрибутами.
# Он должен появиться на экране.
import tkinter
import time


class Player:
    def __init__(self):
        self.id = None
        self.y = None

    def draw(self):
        canvas.move(self.id, 0, self.y)
        _, y, _, y1 = canvas.coords(self.id)
        if y <= 0 or y1 >= 600:
            self.y = 0


class Player1(Player):
    def __init__(self):
        super().__init__()
        self.id = canvas.create_rectangle(10, 10, 20, 90, fill="white")
        self.y = 0
        self.speed = 3

    def move(self, event):
        # print(event.__dict__)
        if event.keysym == "w":
            self.y = -self.speed
        if event.keysym == "s":
            self.y = self.speed

    def stop(self, event):
        if event.keysym in "ws":
            self.y = 0


class Player2(Player):
    def __init__(self):
        super().__init__()
        self.id = canvas.create_rectangle(780, 10, 790, 90, fill="white")
        self.y = 0
        self.speed = 3

    def move(self, event):
        if event.keysym == "Up":
            self.y = -self.speed
        if event.keysym == "Down":
            self.y = self.speed

    def stop(self, event):
        if event.keysym in ("Up", "Down"):
            self.y = 0


class Ball:
    def __init__(self):
        self.id = canvas.create_oval(490, 490, 510, 510, fill='white')
        self.x = 3
        self.y = 3

    def draw(self):
        canvas.move(self.id, self.x, self.y)
        x, y, x1, y1 = canvas.coords(self.id)
        if y <= 0 or y1 >= 600:
            self.y = -self.y
        elif x <= 0 or x1 >= 800:
            self.x = -self.x


root = tkinter.Tk()
root.geometry("800x600")
root.title("Pong")

canvas = tkinter.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

player1 = Player1()
player2 = Player2()

ball = Ball()

root.bind_all("<KeyPress>", player1.move)
root.bind_all("<KeyRelease>", player1.stop, add="+")
root.bind_all("<KeyPress>", player2.move, add="+")
root.bind_all("<KeyRelease>", player2.stop, add="+")

while True:
    root.update()
    root.update_idletasks()
    player1.draw()
    player2.draw()
    ball.draw()
    time.sleep(0.01)