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
        pesquisar = self.driver.find_element_by_name('q')  # - da um submit na barra de pesquisa.
        pesquisar.submit()


ff = webdriver.Firefox()  # instanciando a classe webdriver, metodo Firefox() para ff
g = Google(ff)  # Classe Google leva o parametro ff
time.sleep(1)  # é importante não sobrecarregar o servidor

g.navigate()

g.search('teste')

# pesquisar2 = self.driver.find_element_by_name('btnK') - da um submit no botão de pesquisa
# pesquisar2.submit()

# A submit()função existe para facilitar a vida. Você pode usá-lo
# em qualquer elemento dentro das tags de formulário para enviar esse formulário.

# browser = webdriver.Chrome(executable_path=
# r"C:\Users\garci\PycharmProjects\Projetos-Python\Projetos-Jupyter\chromedriver.exe").

# ff = webdriver.Firefox(executable_path=
# r"C:\Users\JustWeb-Rafael\AppData\Local\Programs\Python\Python36\geckodriver.exe").

# g.navigate() -  chamando um método que faz parte de uma classe.

# retorna um objeto do tipo selenium.
# ff.find_element_by_name('q') - terminal - barra de pesquisa. q - name

# escrevendo na barra de pesquisa.
# bar = ff.find_element_by_name('q')
# bar.send_keys('Teste')

# name da barra de pesquisa - btnK
