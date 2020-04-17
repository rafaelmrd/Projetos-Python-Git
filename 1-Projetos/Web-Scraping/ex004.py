
# Imprimindo informações de alguma página no terminal.

from urllib.request import urlopen

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import re


url = 'https://www.google.com.br/'
# xpath: //*[@id="row10640"]/td[4]/div

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lista = soup.find_all('title')
# lista = soup.find_all('title', class_='text-align')
print(lista)






