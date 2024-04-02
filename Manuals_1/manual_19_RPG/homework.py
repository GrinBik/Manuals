# ДЗ
# Запрограммируй функцию create_enemy().
#
# Она должна случайным образом выбирать
# имя врага и его характеристики: hp и dmg.
#
# В качестве примера,
# возьми функцию create_hero().
from random import randint, choice


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


def create_enemy():
    name = choice(enemy_names)
    hp = randint(50, 100)
    dmg = randint(50, 100)
    enemy = Enemy(name, hp, dmg)
    return enemy


enemy_names = ['Танос', 'Локи', 'Орк', 'Зомби', 'Невидимка']
