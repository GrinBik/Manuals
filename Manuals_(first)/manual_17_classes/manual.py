class Balloon:
    color = 'green'
    size = 0


class Sharik:
    color = 'pink'
    size = 'big'


red = Balloon()

s1 = Sharik()
s2 = Sharik()
s2.size = 'medium'
print(f'Шарик 1, цвет {s1.color}, размер {s1.size}')
print(f'Шарик 2, цвет {s2.color}, размер {s2.size}')
