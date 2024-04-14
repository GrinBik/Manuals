# Написать программу, которая открывает программу "калькулятор", и вычисляет результат суммы 5+5.
# Подсказка: использовать модуль pyAutoGUI.
import time
import pyautogui as gui


# Пауза перед запуском программы
time.sleep(3)

# клик в поле поиска
gui.click(x=576, y=1047)
time.sleep(1)

# название искомой программы
gui.write('Calc')
time.sleep(1)

# запуск
gui.click(x=735, y=270)
time.sleep(1)

# набор текстом 5 + 5 и после Enter (пауза после каждого нажатия)
gui.press("5")
time.sleep(1)
gui.press("+")
time.sleep(1)
gui.press("5")
time.sleep(1)
gui.press("enter")
