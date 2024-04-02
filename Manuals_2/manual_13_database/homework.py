# ДЗ
# Создать модель таблицы игроков, где столбец инвентаря будет содержать словарь.
# Пусть ключами будут названия предметов, а значениями — количество предметов.
# Также создать функции добавления предметов и просмотра инвентаря для любого игрока.
import pickle
import s_taper
from s_taper.consts import *


def read_inventory(player_id):
    data = players.read_obj('id', player_id)
    for invent in data.inventory:
        print(f'{invent}: {data.inventory[invent]}')


def add_inventory(player_id, item):
    data = players.read('id', player_id)
    flag = True
    for cur in data[2]:
        if cur == item:
            data[2][cur] += 1
            flag = False
    if flag:
        data[2][item] = 1
    players.write(data)


scheme = {
    'id': INT + KEY,
    'name': TEXT,
    'inventory': TEXT
}

players = s_taper.Taper('players', 'data.db').create_table(scheme)

players.write([1, 'Гриша', {'аптечка': 2, 'бургер': 2}])
read_inventory(1)

add_inventory(1, 'бургер')
read_inventory(1)
