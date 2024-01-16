class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


def create_hero(name, race, prof):
    hp = 100
    dmg = 25
    hp *= races[race][0]
    hp *= profs[prof][0]
    dmg *= races[race][1]
    dmg *= profs[prof][1]
    hero = Player(name, hp, dmg)
    return hero


name = input("Введи своё имя: ")

races = {
    "эльф": (1.5, 1),
    "гном": (0.8, 1.2),
    "человек": (1, 1)
}

profs = {
    "лучник": (0.9, 2),
    "щитоносец": (2, 0.6),
    "рыцарь": (1.2, 1.2)
}

race = ""
prof = ""

while race not in tuple(races.keys()):
    print(f"Bыбеpи расу: {tuple(races.keys())}")
    race = input("->").lower()

while prof not in tuple(profs.keys()):
    print(f"Bыбеpи профессию: {tuple(profs.keys())}")
    prof = input("->").lower()

hero = create_hero(name, race, prof)

print(f"Здравствуй, герой с именем {hero.name}!\n"
      f"Твоё здоровье равно {hero.hp} XП. \n"
      f"Твой урон равен {hero.damage} единицам.\n"
      f"Желаю удачи в приключениях, странник! ^_+")
