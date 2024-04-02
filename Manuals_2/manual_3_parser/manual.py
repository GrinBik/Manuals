import requests
from bs4 import BeautifulSoup


class Weather:
    def __init__(self, link):
        self.link = link
        r = requests.get(self.link).text
        self.soup = BeautifulSoup(r, "html.parser")

    def get_cities(self):
        # получаем все строки с тегом "a"
        all_cities = self.soup.find_all('a')
        # создаем словарь для дальнейшего хранения - {город: ссылка на город}
        cities = {}
        # перебираем все строки
        for city in all_cities:
            # city храниться в неизвестном формате - преобразуем в str
            town = city.__str__()
            # ищем все строки в которых содержится 'href="/prognoz'
            if 'href="/prognoz' in town:
                # сохраняем название города
                # способ №1
                town_name = town[town.find('>') + 1: town.rfind('<')]
                # способ №2
                town_name = city.get_text()
                # сохраняем ссылку на город
                href = town[town.find('"') + 1: town.rfind('"')]
                # сохраняем все в словарь
                cities[town_name] = "https://pogoda.mail.ru" + href
        return cities


weather = Weather("https://pogoda.mail.ru/country/russia/")
towns = weather.get_cities()
print(towns)

# ДЗ
# Измени код класса так, чтобы ссылку можно было указывать извне.
