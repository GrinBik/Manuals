import pyautogui as gui
from time import sleep


def mouse_pos():
    while True:
        sleep(4)
        print(gui.position())


mouse_pos()

sleep(4)
gui.click(x=204, y=330, button='left')

sleep(4)
gui.click(x=204, y=330, button='right')

sleep(4)
gui.doubleClick(x=204, y=330, button='left')

sleep(4)
pos = [[55, 63], [31, 149], [47, 294], [247, 778], [257, 888], [353, 875], [1318, 761]]
for x, y in pos:
    sleep(4)
    gui.click(x=x, y=y, button='left')

sleep(4)
pos = [[757, 111], [1124, 147], [783, 348], [1140, 715], [995, 861]]
for coord in pos:
    sleep(2)
    index = pos.index(coord)
    if index == 2:
        gui.click(x=coord[0], y=coord[1])
        sleep(1)
        gui.dragTo(x=pos[index + 1][0], y=pos[index + 1][1])
        continue
    elif index == 3:
        gui.click(x=pos[index + 1][0], y=pos[index + 1][1])
        break
    else:
        gui.click(x=coord[0], y=coord[1])

# ДЗ
# Написать программу, которая будет рисовать круг в программе paint.
