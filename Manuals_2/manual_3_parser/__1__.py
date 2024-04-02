import requests
from bs4 import BeautifulSoup


class Weather:
    def __init__(self, link):
        self.link = link
        r = requests.get(self.link).text
        self.soup = BeautifulSoup(r, "html.parser")

    def get_cities(self):
        data = self.soup.find_all('a')
        cities = {}
        for line in data:
            city = line.__str__()
            if 'href="/prognoz' in city:
                name = line.get_text()
                city_link = city[city.find('"') + 1 : city.rfind('"')]
                cities[name] = "https://pogoda.mail.ru" + city_link
        return cities


weather_data = Weather("https://pogoda.mail.ru/country/russia/")
towns = weather_data.get_cities()
print(towns)

# ДЗ
# Измени код класса так, чтобы ссылку можно было указывать извне.
