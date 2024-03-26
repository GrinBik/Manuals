import s_taper
from s_taper.consts import *


def check(line):
    if line == 'INT':
        return INT
    elif line == 'FLT':
        return FLT
    elif line == 'TEXT':
        return TEXT
    elif line == 'BLN':
        return BLN


name = input('Введите название таблицы: ')
columns = input('Введите название каждого столбца и тип его данных через запятую: ').split(',')
n = len(columns)
scheme = {}
print(f'len = {n}')
for i in range(0, n, 2):
    # scheme[columns[i]] = check(columns[i+1])
    scheme[columns[i]] = columns[i + 1]
    # print(columns[_])
for j in list(scheme.values()):
    print(type(j))

tests = s_taper.Taper(name, 'data.db').create_table(scheme)

print(scheme)
