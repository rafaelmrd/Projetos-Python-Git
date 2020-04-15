
# Fazendo login em um site de forma automática.

from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://sistema.justwebtelecom.com.br/login.php")
time.sleep(2)
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("senha")

username.send_keys("MEU-USUARIO")
password.send_keys("MINHA-SENHA")

time.sleep(2)
login_attempt = browser.find_element_by_id('entrar').click()
time.sleep(5)

# a = pyautogui.position()
# print(a)

# pesquisar meu nome na para de pesquisa usando pyautogui.
# pyautogui.moveTo(523, 101, duration=1)
# pyautogui.click(523, 101, button='left', duration=0.25)
# time.sleep(1)
# pyautogui.typewrite('rafael garcia')
# time.sleep(3)
# pyautogui.hotkey('enter')
# time.sleep(3)

# Abre uma nova guia no navegador:
browser.execute_script("window.open('https://sistema.justwebtelecom.com.br/adm.php')")

time.sleep(2)

# mostra todas as minhas informaçoes - GET - controller.php?id=24328
# https://sistema.justwebtelecom.com.br/dashboard/controller.php?id=24328
