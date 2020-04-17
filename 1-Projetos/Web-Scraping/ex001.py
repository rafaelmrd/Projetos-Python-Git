
# Pesquisa no google de maneira automática

from selenium import webdriver
import time


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com'
        self.search_bar = 'q'  # name - barra de pesquisa
        self.btn_search = 'btnK'  # name - botão de pesquisa

    def navigate(self):
        self.driver.get(self.url)

    def search(self, palavra="None"):
        self.driver.find_element_by_name(self.search_bar).send_keys(palavra)
        pesquisar = self.driver.find_element_by_name('q')
        pesquisar.submit()  # - da um submit na barra de pesquisa.


ff = webdriver.Firefox()  # instanciando a classe webdriver, metodo Firefox() para ff
g = Google(ff)  # Classe Google leva o parametro ff
time.sleep(1)  # é importante não sobrecarregar o servidor

g.navigate()  # chamando o método navigate
g.search('Python')
