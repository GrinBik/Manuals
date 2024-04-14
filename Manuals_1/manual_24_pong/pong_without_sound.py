import tkinter
import time
import random


# Родительский класс игроков
class Player:
    def __init__(self):
        # сам объект
        self.id = None
        # перемещение по оси y
        self.y = None
        # перемещение по оси x
        self.x = 0
        # скорость перемещения
        self.speed = 3

    # отрисовка перемещения
    def paint(self):
        # перемещение
        canvas.move(self.id, self.x, self.y)
        # координаты объекта
        pos1 = canvas.coords(self.id)
        # при выходе ракетки за пределы экрана останавливаем
        if pos1[1] <= 0 or pos1[3] >= 600:
            self.y = -self.y


# Класс первой ракетки
class Player1(Player):
    def __init__(self):
        super().__init__()
        # ракетка
        self.id = canvas.create_rectangle(10, 10, 30, 100, fill="black")
        # скорость по оси y
        self.y = 0

    # Управление ракеткой
    def goto(self, event):
        if event.keysym == 'w':
            self.y = -self.speed
        elif event.keysym == 's':
            self.y = self.speed

    # Остановка ракетки
    def stop(self, event):
        if event.keysym in "ws":
            self.y = 0


# Класс второй ракетки
class Player2(Player):
    def __init__(self):
        super().__init__()
        # ракетка
        self.id = canvas.create_rectangle(10, 10, 30, 100, fill="black")
        # переносим в нужное место
        canvas.move(self.id, 760, 500)
        # скорость по оси y
        self.y = 0

    # Управление ракеткой
    def goto(self, event):
        if event.keysym == 'Up':
            self.y = -self.speed
        elif event.keysym == 'Down':
            self.y = self.speed

    # Остановка ракетки
    def stop(self, event):
        if event.keysym in ("Up", "Down"):
            self.y = 0


# Класс мяча
class Ball:
    def __init__(self):
        # мяч
        self.id = canvas.create_oval(0, 0, 50, 50, fill="red")
        # ставим в нужное место
        canvas.move(self.id, 375, 275)
        # случайное движение по оси X
        self.y = random.choice([-1, 1])
        # случайное движение по оси Y
        self.x = random.choice([-1, 1])
        # скорость
        self.speed = 2

    # отрисовка перемещения мяча
    def paint(self):
        # счет обоих игроков
        global score1, score2
        # координаты мяча
        x1, y1, x2, y2 = canvas.coords(self.id)
        # координаты первой ракетки
        rx1, ry1, rx2, ry2 = canvas.coords(player1.id)
        # координаты второй ракетки
        rx3, ry3, rx4, ry4 = canvas.coords(player2.id)
        # отскок мяча от верхней и нижней грани
        if y1 <= 0:
            self.y = self.speed
        if y2 >= 600:
            self.y = -self.speed
        # отскок мяча от первой ракетки
        if y1 >= ry1 and y2 <= ry2 and x1 <= rx2:
            # отскок мяча
            canvas.move(self.id, 50, 0)
            # увеличиваем счет
            score1 += 1
            # меняем надпись
            canvas.itemconfig(score_gui, text=f"Счёт {score1}:{score2}")
            # увеличиваем скорость мяча и обеих ракеток
            self.speed += 0.25
            player1.speed += 0.25
            player2.speed += 0.25
            # изменяем направление движения мяча
            self.x = self.speed
        if y1 > ry3 and y2 < ry4 and x2 >= rx3:
            # отскок мяча
            canvas.move(self.id, -50, 0)
            # увеличиваем счет
            score2 += 1
            # меняем надпись
            canvas.itemconfig(score_gui, text=f"Счёт {score1}:{score2}")
            # увеличиваем скорость мяча и обеих ракеток
            self.speed += 0.25
            player1.speed += 0.25
            player2.speed += 0.25
            # изменяем направление движения мяча
            self.x = -self.speed
        # перемещение мяча
        canvas.move(self.id, self.x, self.y)
        if x2 <= 0 or x1 >= 800:
            return True


# окно
root = tkinter.Tk()
# размер
root.geometry("800x600")
# невозможность изменения размера окна
root.resizable(0, 0)
# название окна
root.title("Pong")

# холст
canvas = tkinter.Canvas(root, height=600, width=800, bg="green")
canvas.pack()

# 2 игрока (ракетки)
player1 = Player1()
player2 = Player2()

# мяч
ball = Ball()

# привязка клавиш к управлению объектами
root.bind_all("<KeyPress>", player1.goto)
root.bind_all("<KeyRelease>", player1.stop, add='+')
root.bind_all("<KeyPress>", player2.goto, add='+')
root.bind_all("<KeyRelease>", player2.stop, add='+')

# файл с рекордом
file = open("score.ini", "r+")
# читаем строку из файла
data = file.readline()

# если строка пуста, то РЕКОРД = 0
if data == "":
    record = 0
    file.write(f"{record}")
    file.close()
# если строка не пуста, то сохраняем существующий РЕКОРД
else:
    record = int(data)
    file.close()

# счет двух игроков
score1 = 0
score2 = 0

# надпись на экране счета и рекорда
score_gui = canvas.create_text(400, 20, text=f"Счёт {score1}:{score2}", font=("Arial",20), fill="black")
record_gui = canvas.create_text(400, 60, text=f"Рекорд {record}", font=("Arial", 20), fill="black")

# процесс игры
while True:

    # обновляем окно
    root.update()
    # обновляем процессы
    root.update_idletasks()

    # перемещение первой ракетки
    player1.paint()
    # перемещение второй ракетки
    player2.paint()

    # перемещение мяча
    result = ball.paint()
    # вылет мяча за пределы боковых граней экрана
    if result:

        # мяч вылетел - удаляем
        canvas.delete(ball.id)
        # новый мяч
        ball = Ball()
        # установка начальной скорости ракеток
        player1.speed = 3
        player2.speed = 3

        # проверяем наличие рекорда
        if record < max(score1, score2):
            # новый рекорд
            record = max(score1, score2)
            # открываем файл
            file = open("score.ini", "r+")
            # очищаем файл
            file.truncate(0)
            # переносим курсор в начало файла
            file.seek(0)
            # записываем новый рекорд
            file.write(f'{record}')
            # обновляем надпись на экране
            canvas.itemconfig(record_gui, text=f"Рекорд {record}")
            # закрываем файл
            file.close()

        # сброс очков
        score1 = 0
        score2 = 0
        canvas.itemconfig(score_gui, text=f"Счёт {score1}:{score2}")

    # FPS
    time.sleep(0.01)
