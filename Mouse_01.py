# https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/
import pyautogui
import time


try:
    while True:
        print(pyautogui.size())
        pyautogui.moveTo(100, 100, duration=1)
        print(pyautogui.position())
        time.sleep(10)
        pyautogui.moveTo(800, 800, duration=1)
        time.sleep(10)
except KeyboardInterrupt:
    print('interrupted!')