# Abrindo janela do google chrome, pesquisando algo automaticamente.

import webbrowser
import pyautogui
import time

webbrowser.open('https://www.google.com/')

# a=pyautogui.position() - encontrar posição
# print(a)

time.sleep(1)

pyautogui.moveTo(2909, 142, duration=1)
pyautogui.click(2909, 142, button='left', duration=0.25)
time.sleep(1)
pyautogui.typewrite('Carro')
time.sleep(1)
pyautogui.hotkey('enter')
