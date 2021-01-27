import scrapy


class MkSpider(scrapy.Spider):
    name = 'mk'
    allowed_domains = ['mk.ru']
    start_urls = ['http://mk.ru/']

    def parse(self, response):
        pass
