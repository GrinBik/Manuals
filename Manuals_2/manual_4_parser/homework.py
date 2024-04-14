import requests
from bs4 import BeautifulSoup
import tkinter


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


class Window:
    def __init__(self, cities):
        # Стартовое окно
        self.root = tkinter.Tk()
        self.root.geometry('800x700')
        self.root.title('Прогноз погоды')
        # Список с будущими названиями городов
        self.check = []

        # Заголовок
        self.text = tkinter.Label(self.root, text="В каком городе вы хотели бы посмотреть прогноз погоды?",
                                  font=('Arial', 15))
        self.text.pack(side=tkinter.TOP)

        # Перечень доступных городов
        self.cities_list = tkinter.Label(self.root, wraplength=800, font=("Arial", 11))
        self.cities_list.pack(side=tkinter.TOP)
        # Заполняем перечень городов
        self.set_text(cities)

        # Поле ввода
        self.entry = tkinter.Entry(self.root, width=50)
        self.entry.pack(side=tkinter.LEFT)

        # Кнопка запуска загрузки прогноза
        self.btn = tkinter.Button(self.root, text="Ввод", command=lambda x=cities: self.check_input(cities))
        self.btn.pack(side=tkinter.LEFT)

    # Заполнение перечня городов
    def set_text(self, cities):
        text = ""
        for city in cities:
            self.check.append(city)
            text += city + ', '
        text = text[:-2]
        self.cities_list.configure(text=text)

    # Проверка введенного названия города
    def check_input(self, cities):
        choice = self.entry.get()
        if choice not in self.check:
            return
        self.text.configure(text=f'Прогноз погоды в городе {choice}')
        self.show_weather(cities[choice])

    # Загрузка прогноза в выбранном городе
    def show_weather(self, city_link):
        # Получаем код страницы
        site_data = Weather(city_link)
        # Берем только нужную информацию
        data = site_data.soup.find('div', {'class': 'information__content'})
        # Получаем текст тегов
        data = data.get_text()
        # Меняем все переносы на новую строку на пробел
        data = data.replace("\n", " ")
        # Разбиваем получившуюся строку на элементы (список) и соединяем их через пробел
        # Таким образом избавляемся от лишних пробелов
        data = ' '.join(data.split())
        # Добавляем эмодзи в зависимости от температуры
        if data[0] == '+':
            data = data
        else:
            data = data
        # Выводим на экран
        self.cities_list.configure(text=data)
        print(data[0])


weather_data = Weather("https://pogoda.mail.ru/country/russia/")
towns = weather_data.get_cities()

window = Window(towns)
window.root.mainloop()

# ДЗ
# Добавь в проект украшения.
# Пусть в зависимости от температуры на экране появляются большие эмодзи солнца ☀️и снежинки ❄️.
