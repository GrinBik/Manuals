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

users = s_taper.Taper('users', 'data.db').create_table(scheme)
orders = s_taper.Taper("orders", "data.db").create_table(scheme_2)

user = users.read("user_id", 121)
print(user)

print(users.read("age", 70))

key = random.randint(0, 3000)
user = users.read("user_id", key)
print(f"ID: {key}")
print("Данные:")
for cell in user:
    print(cell)

data = users.read_all()
print(data)

data = users.read_all()
n = 0
for user in data:
    if user[2] >= 70:
        n += 1
        print(user)
print(f"Всего {n} клиентов старше 70")
print(f"Это {n * 100 / len(data)}% от всех клиентов")

data = users.read_obj("user_id", 322)
print(data)
print(data.__dict__)
print(f"Это {data.name} и ему {data.age} лет")

n = 0
for key in range(0, 3000):
    data = users.read_obj("user_id", key)
    if data.first:
        n += 1
print(f"Всего {n} новых клиентов")
print(f"Это {n * 100 / 3000}% от всех клиентов")

orders.delete_row(all_rows=True)
print(orders.read_all())

# users.delete_row("first", 1)
# users.drop_table()
# users.drop_table("Имя таблицы")
