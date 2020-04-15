from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

# Pegando cookie de uma página web.

# Livro Web Scraping com Python: Coletando mais dados da web moderna
# Titulo -  Submetendo um formulário básico
# https://books.google.com.br/books?id=95qODwAAQBAJ&pg=PT216&lpg=PT216&dq=submiss%C3%A3o+de+dados+post+python&source=bl&ots=FV6DwvqkTX&sig=ACfU3U0lsc_l5YYor1XiIWAFhqWX5OWQBQ&hl=pt-BR&sa=X&ved=2ahUKEwjVk6O9ueboAhUvIbkGHWTGDGAQ6AEwBnoECAcQMQ#v=onepage&q=submiss%C3%A3o%20de%20dados%20post%20python&f=false

# -------------------------------
# params = {'email': '', 'senha': ''}
# r = requests.post('https://sistema.justwebtelecom.com.br/login.php', params)
# time.sleep(3)
# print('Cookie is set to:')
# print(r.cookies.get_dict())
# print('Going to profile page...')
# r = requests.get('https://sistema.justwebtelecom.com.br/adm.php', cookies=r.cookies)
# print(r.text)
# -------------------------------

# session = requests.Session()
# params = {'email': '', 'senha': ''}
# s = session.post('https://sistema.justwebtelecom.com.br/login.php', params)
# time.sleep(3)
# print('Cookie is set to:')
# print(s.cookies.get_dict())
# print('Going to profile page...')
# s = session.get('https://sistema.justwebtelecom.com.br/adm.php')
# print(s.text)
# -------------------------------

from requests.auth import AuthBase
# from requests.auth import HTTPBasicAuth
#
# auth = HTTPBasicAuth('', '')
# r = requests.post(url='https://sistema.justwebtelecom.com.br/login.php', auth=auth)
# print(r.text)
# -------------------------------
