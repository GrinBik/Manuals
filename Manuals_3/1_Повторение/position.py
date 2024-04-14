import time
import pyautogui as gui


def position():
    while True:
        print(gui.position())
        time.sleep(1)


position()
