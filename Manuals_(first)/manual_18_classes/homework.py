# ДЗ
# Создать класс главного героя будущей игры в жанре RPG. Назначить ему все необходимые атрибуты:
# здоровье, урон, имя и другие. Придумать боевой клич главного героя и создать метод, который будет выводить
# этот клич в консоль, будто бы герой кричит. Создать экземпляр получившегося класса и вывести в консоль
# все его атрибуты. Запустить метод боевого крика.
class Player:
    def __init__(self):
        self.hp = 100
        self.dmg = 10
        self.name = 'Игрок'

    def clich(self):
        print('Я есть Грут')


hero = Player()
print(f'Создан игрок под именем {hero.name}, у которого {hero.hp} здоровья и {hero.dmg} урона.')
hero.clich()