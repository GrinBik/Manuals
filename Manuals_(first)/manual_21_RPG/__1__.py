from random import randint, choice
import time


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.xp = 0
        self.lvl = 1
        self.heals = 0

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"Ты нанёс врагу {self.damage} урона. Теперь у него {victim.hp} здоровья.")
        if victim.hp <= 0:
            print(f"{victim.name} повержен!")
            self.xp += victim.xp
            print(f"Ты получил {victim.xp} опыта! Теперь у тебя {self.lvl} LVL и {self.xp} XP.")
            while self.xp >= 100:
                self.lvl += 1
                print(f"ПОЗДРАВЛЯЮ! Уровень повышен: {self.lvl}")
                self.xp -= 100
                self.damage *= 1.5
                print(f"Ты стал сильнее! ⚔️: {self.damage}")
            luck = randint(0, 1)
            if luck == 1:
                self.heals += 1
                print(f"Ты получил Лечебный отвар🧋! Теперь у тебя их {self.heals} ед.")
            return False
        else:
            return True


class Enemy:
    races = {
        "Слизняк": (10, 10),
        "Волк": (25, 20),
        "Орк": (50, 45),
        "Группа гоблинов": (120, 25),
        "Оборотень": (150, 50)}

    def __init__(self):
        self.name = choice(list(self.races.keys()))
        self.hp = self.races[self.name][0]
        self.damage = self.races[self.name][1]
        self.xp = self.hp * 1.5

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"{self.name} нанёс тебе {self.damage} урона. Теперь у тебя {victim.hp} здоровья.")
        if victim.hp <= 0:
            exit(print("ПОТРАЧЕНО!"))


def create_hero(name, race, prof):
    hp = 100
    dmg = 25
    hp *= races[race][0]
    hp *= profs[prof][0]
    dmg *= races[race][1]
    dmg *= profs[prof][1]
    hero = Player(name, hp, dmg)
    return hero


def start(heal=None):
    if heal is None:
        enemy = Enemy()
    else:
        enemy = heal
    print(f"Тебе встретился {enemy.name}. ❤️: {enemy.hp}, ⚔️: {enemy.damage}")
    print("Нападать?")
    answer = input("Да/Нет/Лечиться: ").lower()
    if answer == 'лечиться':
        if hero.heals > 0:
            hero.hp += 50
            hero.heals -= 1
            print(f"Ты выпил Лечебный отвар🧋. ❤️: {hero.hp}")
        else:
            print("У тебя нет больше отвара.")
        start(enemy)
    elif answer == "да":
        fight(enemy)
    else:
        luck = randint(0, 100)
        if luck in range(40):
            print("Ты смог незаметно ускользнуть и пойти дальше!")
            time.sleep(2)
            start()
        else:
            print("Ты НЕ смог незаметно ускользнуть!")
            time.sleep(2)
            enemy.attack(hero)
            fight(enemy)


def fight(victim):
    result = hero.attack(victim)
    time.sleep(1)
    if result:
        victim.attack(hero)
        time.sleep(1)
        if hero.hp <= 0:
            exit()
        fight(victim)
    else:
        start()


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

time.sleep(1)
start()
