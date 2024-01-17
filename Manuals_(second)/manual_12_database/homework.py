# ДЗ
# Удали таблицы users и orders
import s_taper
from s_taper.consts import *


scheme = {
    'user_id': INT + KEY,
    'name': TEXT,
    'age': INT,
    'first': BLN
}

users = s_taper.Taper('users', 'data.db').create_table(scheme)

users.drop_table("orders")
