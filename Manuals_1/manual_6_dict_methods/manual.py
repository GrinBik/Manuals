slovar = {
    "ключ": "значение",
    123: 1234,
    "список": ["1", 2, "3"]
}
print(dict["список"])

# print(slovar[0])

print(dict["ключ"])

slovar[2023] = "Год Кролика"
print(slovar)

slovar[2023] = "Год Водяного Кролика"
print(slovar)

del slovar["ключ"]
print(slovar)

slovar.pop(2023)
print(slovar)

slovar = {2023: 'Год Водяного Кролика'}
rez = slovar.pop(2023)
print(rez)

# slovar = {"ключ": "значение"}
slovar[2023] = "Год Кролика"
slovar["Макароны"] = "спагетти"
print(slovar)
rez = slovar.popitem()
print(slovar)
print(rez)

print(slovar)
slovar.clear()
print(slovar)

example = {'персона': 'человек',
           'марафон': 'гонка бегунов длиной около 26 миль',
           'противостоять': 'оставаться сильным, несмотря на давление',
           'бежать': 'двигаться со скоростью'}
print(list(example.keys()))

print(list(example.values()))

phone_book = {
    'Белозеров': '+7 120 959 45 19',
    'Владимиров': '+7 (342) 787-1717',
    'Симонов': '+7 550 642 49 52',
    'Герасимова': '+7 056 273 2478'
}
last_name = input("Введите фамилию -> ")
print(f"Найден номер телефона: {phone_book[last_name]}")

phone_book["Владимиров"] = '+79175694884'
last_name = input("Введите фамилию -> ")
print(f"Найден номер телефона: {phone_book[last_name]}")

phone_book.pop("Герасимова")
