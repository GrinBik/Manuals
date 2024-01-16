import random


dictionary = {
    "Слива": "12 ккал",
    "Банан": "120 ккал",
    "Яблоко": "54 ккал",
    "Snickers": "132 ккал"
}

keys = list(dictionary.keys())
rnd = random.choice(keys)
print("%s: %s" % (rnd, dictionary[rnd]))
