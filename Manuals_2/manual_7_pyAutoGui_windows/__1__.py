import pyautogui as gui
from time import sleep
from random import randint
from playsound import playsound


def website():
    gui.alert(text="Добро пожаловать на наш сайт/приложение", title="Welcome", button="Спасибо")
    while True:
        choice = gui.confirm(text=f"Вы уже зарегистрированы?", title="", buttons=["Да", "Нет", "Выход"])
        if choice == "Нет":
            gui.alert(text="Тогда вам нужно зарегистрироваться!", title="", button="Хорошо")
            new_login = gui.prompt(text="Введите логин", title="Регистрация", default="")
            new_password = gui.password(text="Придумайте пароль", title="Регистрация", default="", mask='*')
            login_password[new_login] = new_password
            gui.alert(text="Вы успешно зарегистрированы", title="", button="Спасибо")
        elif choice == "Да":
            login = gui.prompt(text="Введите    логин", title="Авторизация", default="")
            password = gui.password(text="Введите пароль", title="Регистрация", default="", mask="*")
            if login in login_password:
                if password == login_password[login]:
                    gui.alert(text="Вы успешно вошли на сайт/приложение", title="", button="Спасибо")
                else:
                    gui.alert(text="Неверный пароль", title="", button="Вернуться")
            else:
                gui.alert(text="Такого пользователя не существует", title="", button="Вернуться")
        elif choice == "Выход":
            gui.alert(text="Удачного дня", title="End", button="Спасибо")
            break


def get_pos():
    first_pos = 1
    second_pos = 2
    while first_pos != second_pos:
        first_pos = gui.position()
        sleep(0.5)
        second_pos = gui.position()
        if first_pos == second_pos:
            playsound('pong.mp3')
            return first_pos
        else:
            continue


def search_img():
    img = gui.locateOnScreen("screenshot.png")
    imf_x, img_y = gui.center(img)
    gui.doubleClick(x=imf_x, y=img_y)


# gui.alert(text="Critical Error ", title="Оповещение", button='OK')
#
# gui.confirm(text="Тебе нравятся эти окна?", title="Опрос", buttons= ['Очень', 'Нет'])
#
# gui.prompt(text="Введите свой логин", title="Регистрация", default='')
#
# gui.password(text="Введите пароль", title="Регистрация", default="", mask='*')
#
# rub = 1000
# while True:
#     if rub >= 100:
#         v = randint(1, 15)
#         sleep(0.5)
#         rub = rub - 100
#         gui.alert(text=f"У вас осталось {rub} рублей", title="Бюджет", button="ОК")
#         if v == 8:
#             gui.alert(text="Вы выиграли 1000 рублей!", title="Поздравляем!", button="Ура")
#             rub = rub + 1000
#             result = gui.confirm(text=f"Хотите продолжить?", title="Оповещение", buttons=["Играть", "Закончить"])
#             if result == "Закончить":
#                 print(f"ВЫ закончили с суммой {rub}")
#                 gui.alert(text=f"ВЫ закончили с суммой {rub}", title="Итоги", button="ОК")
#                 break
#         else:
#                 gui.alert(text="Не повезло, с вас спишется 100 рублей", title="Проигрыш", button="ОК")
#     else:
#         gui.alert(text="Вы банкрот", title="Проигрыш", button="ОК")
#         break
#
# login_password = {}
# website()

sleep(4)
f = get_pos()
s = get_pos()
width, height = s[0] - f[0], s[1] - f[1]
# Может возникнуть ошибка, необходимо будет установить дополнительный модуль: pip install Pillow
gui.screenshot("screenshot.png", region=(f[0], f[1], width, height))
search_img()

# ДЗ
# Используя окна оповещений, сделать форму для обратной связи на любую тему и записать введенные ответы.
# С помощью команды locateOnScreen написать программу код, которая сама запустит какую-либо программу.
