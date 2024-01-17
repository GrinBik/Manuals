import s_taper
from s_taper.consts import *


scheme = {
    'user_id': INT + KEY,
    'name': TEXT,
    'age': INT,
    'first': BLN
}

users = s_taper.Taper('users', 'data.db').create_table(scheme)

# Ссылка на SQLite Studio: https://sqlitestudio.pl/

scheme_2 = {
    'user_id': INT + KEY,
    'name': TEXT,
    'order_id': INT,
    'n': INT,
    'art': INT,
    'sum': INT
}

orders = s_taper.Taper("orders", "data.db").create_table(scheme_2)

# Заполни обе таблицы различной информацией.
