
# Pegando um dado de um site e salvando em um aquivo texts.json.

import scrapy


class Teste(scrapy.Spider):
    name = 'tt'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        self.log('Eu estou aqui {}' .format(response.url))
        texts = response.xpath('//span[@class="text"]/text()').extract()

        for text in texts:
            yield {
                'text': text
            }

# Ir no diretorio do arquivo, abrir o Git Bash Here, digitar os comandos abaixo.
# scrapy runspider ex006.py
# scrapy runspider ex006.py -o texts.json - criando o arquivo json

# https://www.youtube.com/watch?v=xlN8ChkF_Yw

# https://www.youtube.com/watch?v=rj8Sqsgh5TM
