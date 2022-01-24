import time
from time import sleep
import keyboard
import pyautogui

CLICKER_SPEED = 0.05
print(CLICKER_SPEED)
a = input()
CLICK = False
while True:
    # sleep используется для замедления цикла, чтобы не грузил ЦП
    if keyboard.is_pressed('v'):
        CLICK = True

    elif keyboard.is_pressed('q'):  # if key 'q' is pressed
        print(f'You Pressed A Key! {time.thread_time()}')
        CLICK = False
        sleep(0.5)

    elif not CLICK:
        sleep(0.5)

    elif CLICK:
        pyautogui.click()
        sleep(CLICKER_SPEED)
