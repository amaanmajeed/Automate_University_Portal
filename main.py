import pyautogui
from time import sleep

# from bs4 import BeautifulSoup
# import requests


# Documentation https://pyautogui.readthedocs.io/en/latest/
# open portal

pyautogui.FAILSAFE = True
x = 1102
y = 657
wait_time = 10


def wait_open(image):
    loc = 'None'
    i = 0
    while True:
        loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=.92)
        if str(type(loc)) == "<class 'pyscreeze.Box'>" or i == (wait_time * 2):
            print('Portal Identified')
            break
        else:
            i += 1
        sleep(0.5)


pyautogui.hotkey('win', '1')
sleep(1.5)

wait_open('OpenEdge.jpg')

pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://online.umt.edu.pk/', interval=0.02)
pyautogui.press('enter')
sleep(0.5)

wait_open('Participate.jpg')
sleep(1)

pyautogui.moveTo(x, y)
pyautogui.doubleClick()
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# click an Image
# cords = pyautogui.locateCenterOnScreen(image)
# pyautogui.click(cords)
