import requests
from bs4 import BeautifulSoup
import tkinter


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


class Window:
    def __init__(self, cities):
        self.root = tkinter.Tk()
        self.root.geometry('800x700')
        self.root.title('Прогноз погоды')
        self.check = []

        self.label = tkinter.Label(self.root, wraplength=600, font=("Trebuchet MS", 11))
        self.label.pack(side=tkinter.TOP)
        self.set_text(cities)

        self.entry = tkinter.Entry(self.root, width=50)
        self.entry.pack(side=tkinter.LEFT)

        self.btn = tkinter.Button(self.root, text="Ввод", command=lambda x=cities: self.check_input(cities))
        self.btn.pack(side=tkinter.LEFT)

    def set_text(self, cities):
        text = ""
        for city in cities:
            self.check.append(city)
            text += city + ', '
        text = text[:-2]
        self.label.configure(text=text)

    def check_input(self, cities):
        choice = self.entry.get()
        if choice not in self.check:
            return
        self.show_weather(cities[choice])

    def show_weather(self, city_link):
        site_data = Weather(city_link)
        data = site_data.soup.find('div', {'class': 'information__content'})
        data = data.get_text()
        data = data.replace("\n", "").replace("\r", "")
        data = ' '.join(data.split())
        text = ''
        prev_char = ''
        n = 0
        for char in data:
            if char.isdigit() and prev_char.isalpha():
                text += ' ' + char
            else:
                text += char
            prev_char = char
        self.label.configure(text=text)


weather_data = Weather("https://pogoda.mail.ru/country/russia/")
towns = weather_data.get_cities()

window = Window(towns)
window.root.mainloop()

# ДЗ
# Добавь в проект украшения.
# Пусть в зависимости от температуры на экране появляются большие эмодзи солнца ☀️и снежинки ❄️.
