import s_taper
from s_taper.consts import *


scheme = {
    'user_id': INT + KEY,
    'name': TEXT,
    'rating': INT
}

users = s_taper.Taper('users', 'data.db').create_table(scheme)

user = users.read('user_id', 0)
