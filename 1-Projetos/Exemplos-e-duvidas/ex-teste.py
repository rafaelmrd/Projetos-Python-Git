from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main(args):

    browser = webdriver.Firefox()
    browser.get('http://www.google.com')
    time.sleep(2)  # é importante não sobrecarregar o servidor

    elementoEntrada = browser.find_element_by_name("q")  # procura o campo de texto com nome "q"
    elementoEntrada.send_keys("amazonia")  # preenche com a palavra amazonia
    elementoEntrada.submit()  # realiza a pesquisa

    time.sleep(10)  # 30 segundos para fechar a conexão

    browser.close()
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))


# https://cadernodelaboratorio.com.br/2019/08/12/selenium-controlando-um-browser-programaticamente/