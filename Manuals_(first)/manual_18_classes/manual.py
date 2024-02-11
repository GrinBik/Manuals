class Automatic:
    def __init__(self):
        print('Началась инициализация!')
        self.time = 30
        self.name = 'Будильник'


class Parrot:
    def __init__(self, color, size):
        # 12
        self.color = color
        self.size = size

    def chirik(self):
        print(f"«Чирик, Чирик!» - сказал {self.size} {self.color} попугай.")


class Bus:
    def __init__(self, trip):
        self.trip = trip

    def navigator(self, stop):
        line = trip[self.trip]
        print(f"Автобус {self.trip} прибыл на остановку {line[stop]}")


duzz = Automatic()

kesha = Parrot('зеленый', 'маленький')

kesha.chirik()

trip = {
    13: ("Гостиный двор", "ГДК", "Магазин Гипер", "Галерея"),
    25: ("Парк Победы", "Улица Ленина", "Главная площадь", "Речное депо")
}

go = Bus(13)
for num in range(4):
    go.navigator(num)

speedy = Bus(25)
for num in range(4):
    speedy.navigator(num)
