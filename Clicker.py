import time
import pyautogui
from time import sleep
import keyboard

CLICKER_SPEED = 0.05
CLICK = False
while True:  # making a loop
    if keyboard.is_pressed('v'):
        CLICK = True

    elif CLICK == True:
        pyautogui.click()
        sleep(CLICKER_SPEED)

    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print(f'You Pressed A Key! {time.thread_time()}')
        CLICK = False
