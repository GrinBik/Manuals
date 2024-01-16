import pickle
import s_taper
from s_taper.consts import *


data = {}
for x in range(25):
    data[f'{x}'] = x * 2

print(data)

bytes = pickle.dumps(data)
print(bytes)

data = pickle.loads(bytes)
print(data)

scheme = {
    'id': INT + KEY,
    'data': TEXT
}
users = s_taper.Taper('users', 'data.db').create_table(scheme)
hard = (["я", "список", "внутри", "кортежа"], {"я": "словарь", "внутри": "кортежа"})
# users.write([1, hard])
print(users.read_all())
print(users.read("ID", 1))
print(users.read_obj("ID", 1).__dict__)
