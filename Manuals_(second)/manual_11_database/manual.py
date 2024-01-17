import s_taper
from s_taper.consts import *
import random


scheme = {
    'user_id': INT + KEY,
    'name': TEXT,
    'age': INT,
    'first': BLN
}
scheme_2 = {
    'user_id': INT + KEY,
    'name': TEXT,
    'order_id': INT,
    'n': INT,
    'art': INT,
    'sum': INT
}
uni = {
   'name': TEXT + KEY,
   'song': TEXT
}

users = s_taper.Taper('users', 'data.db').create_table(scheme)
orders = s_taper.Taper("orders", "data.db").create_table(scheme_2)

# users.write([3121, "Александр", 32, True])

# for i in range(3000):
#     users.write([i, f"Имя {i}", random.randint(22, 78), random.choice((True, False))])

# orders.create_table(scheme_2, "new")

# for i in range(3000):
#     orders.create_table(uni, f"ID_{i}")

user = random.randint(0, 3000)
print(user)
users.write([f"ID_{user}", "Кара-кум — Круг"], f"ID_{user}")

# С помощью множественного выделения удали из студии все номерные таблицы
