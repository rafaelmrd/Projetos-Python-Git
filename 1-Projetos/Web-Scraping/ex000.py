# Abrindo o google.com

from selenium import webdriver


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com'

    def navigate(self):
        self.driver.get(self.url)


ff = webdriver.Firefox()
g = Google(ff)
