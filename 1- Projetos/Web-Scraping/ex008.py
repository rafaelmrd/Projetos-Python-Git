import time
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# https://medium.com/horadecodar/como-fazer-webscraping-com-python-e-beautiful-soup-28a65eee2efd


# ---------------------------------------- Ex: 3 - selenium
# browser = webdriver.Firefox()
# browser.get("https://google.com")
# html = browser.page_source
# soup = BeautifulSoup(html, 'lxml')
# lista = soup.find_all('title')  # ou print(soup.title)
# print(lista)
# ---------------------------------------- Ex: 3 - selenium

# ---------------------------------------- Ex: 2 - BeautifulSoup
# url = 'https://google.com'
# time.sleep(3)
# html = urlopen(url) # lendo a URL com a urllopen
# soup = BeautifulSoup(html, 'lxml')
# lista = soup.find_all('title')
# print(lista)
# ---------------------------------------- Ex: 2 - BeautifulSoup

# ---------------------------------------- Ex: 1 - requests
# res = requests.get('https://google.com')
# res.raise_for_status() # ou res.text
# print(res.text)
# ---------------------------------------- Ex: 1 - requests

