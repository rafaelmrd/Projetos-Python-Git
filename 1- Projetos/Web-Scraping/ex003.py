# Imprimindo informações de alguma página no terminal.

from selenium import webdriver
import time
import re

from selenium.webdriver.common.keys import Keys


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.google.com/'

    def navigate(self):
        self.driver.get(self.url)

    def getDados(self):
        element = self.driver.find_element_by_tag_name('title')
        html_content = element.get_attribute('outerHTML')
        # tira as tag do conteudo
        html_content2 = re.sub('<[^>]+?>', '', html_content)
        return html_content2

    def condicao(self):
        # html_content2 = g.getDados() = conteudoPagina
        conteudoPagina = g.getDados()
        if 't' in conteudoPagina:
            print('true')
            print(conteudoPagina)
        else:
            print('false')
            print(conteudoPagina)


ff = webdriver.Firefox()  # instanciando a classe webdriver, metodo Firefox() para ff
g = Google(ff)  # Classe Google leva o parametro ff
time.sleep(1)  # é importante não sobrecarregar o servidor

g.navigate()  # chamando o método navigate
g.getDados()  # chamando o método getDados
g.condicao()  # chamando o método condicao

