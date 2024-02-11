import time
import pyautogui as gui


# Calculator 5 + 5 =
gui.click(x=576, y=1047)
time.sleep(1)
gui.write('Calc')
time.sleep(1)
gui.click(x=735, y=270)
time.sleep(1)

# 5
gui.click(x=659, y=677)
time.sleep(1)

# +
gui.click(x=862, y=744)
time.sleep(1)

# 5
gui.click(x=659, y=677)
time.sleep(1)

# =
gui.click(x=850, y=808)
