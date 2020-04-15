# Imprimindo informações de alguma página no terminal.

from selenium import webdriver
import time
import re


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.ixcsoft.com.br/'

    def navigate(self):
        self.driver.get(self.url)

    def getDados(self):
        element = self.driver.find_element_by_tag_name('title')
        html_content = element.get_attribute('outerHTML')
        # tira as tag do conteudo
        html_content2 = re.sub('<[^>]+?>', '', html_content)
        print(html_content2)


ff = webdriver.Firefox()  # instanciando a classe webdriver, metodo Firefox() para ff
g = Google(ff)  # Classe Google leva o parametro ff
time.sleep(1)  # é importante não sobrecarregar o servidor

g.navigate()  # chamando o método navigate
g.getDados()  # chamando o método getDados

# A função re.sub() recebe como primeiro parâmetro uma expressão regular e buscará no conteúdo,
# definido pelo terceiro parâmetro, trechos que combinam com a expressão, substituindo-os pelo
# conteúdo definido no segundo parâmetro.
