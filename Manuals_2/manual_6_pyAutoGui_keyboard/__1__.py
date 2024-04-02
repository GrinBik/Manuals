import pyautogui as gui
from time import sleep


sleep(4)
# Кликаем по поиску и пишем название запускаемой программы
gui.click(x=657, y=1043)
sleep(1)
gui.write('pain')
sleep(1)
gui.press('Enter')

# В играх можно применять зажатие клавиш
# Если есть игра, то можно опробовать зажатие 'w' на 7 секунд
sleep(4)
gui.keyDown('w')
sleep(7)
gui.keyUp('w')

# Если есть игра, то можно опробовать передвижение по квадратной траектории
sleep(4)
long = 2
for side in "WASD":
    gui.keyDown(side)
    sleep(long)
    gui.keyUp(side)

sleep(4)
gui.click(x=657, y=1043)
gui.press('f', presses=4)

sleep(4)
gui.click(x=657, y=1043)
with gui.hold('shift'):
    gui.press("p")

sleep(4)
gui.click(x=657, y=1043)
gui.hotkey('shift', 'p')

# ДЗ
# Написать программу, при запуске которой будет запускаться браузер.
# В адресной строке будет вводиться запрос и нажиматься enter.
# После чего мышка должна кликнуть по первому поисковому результату для загрузки страницы.
