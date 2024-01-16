import tkinter
import time
from playsound import playsound


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
        self.id = canvas.create_rectangle(30, 10, 40, 90, fill="white")
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
        self.id = canvas.create_rectangle(760, 10, 770, 90, fill="white")
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
        self.id = canvas.create_oval(100, 100, 120, 120, fill='white')
        self.x = 3
        self.y = 3

    def draw(self):
        global score
        canvas.move(self.id, self.x, self.y)
        x1, y1, x11, y11 = canvas.coords(player1.id)
        x2, y2, x22, y22 = canvas.coords(player2.id)
        bx, by, bx1, by1 = canvas.coords(self.id)
        if by <= 0 or by1 >= 600:
            self.y = -self.y
        # if by > y1 and by1 < y11 and bx <= x11:
        if by > y1 - 15 and by1 < y11 + 15 and bx <= x11:
            self.x -= 0.25
            self.x = -self.x
            player1.speed += 0.25
            score += 1
            canvas.itemconfig(score_gui, text=f"Счёт: {score}")
            playsound('pong.mp3', block=False)
        if by > y2 - 15 and by1 < y22 + 15 and bx1 >= x2:
            self.x += 0.25
            self.x = -self.x
            player2.speed += 0.25
            score += 1
            canvas.itemconfig(score_gui, text=f"Счёт: {score}")
            playsound('pong.mp3', block=False)
        if bx <= 0 or bx1 >= 800:
            return True


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

record_file = open("score.ini", "r+")
data = record_file.readline()
if data == "":
    record = 0
    record_file.write(f"{record}")
    record_file.close()
else:
    record = int(data)

score = 0
score_gui = canvas.create_text(390, 20, text=f"Счёт: {score}", fill="white", font=("Consolas", 20))
canvas.create_text(390, 40, text=f"Рекорд: {record}", fill="white", font=("Consolas", 20))

while True:
    root.update()
    root.update_idletasks()
    player1.draw()
    player2.draw()
    loser = ball.draw()
    if loser:
        break
    time.sleep(0.01)

record_file = open("score.ini", "r+")
a = record_file.readline()
if int(a) < score:
    record_file.truncate(0)
    record_file.seek(0)
    record_file.write(f"{score}")
    record_file.close()
else:
    record_file.close()
