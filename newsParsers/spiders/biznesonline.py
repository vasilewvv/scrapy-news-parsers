import scrapy


class BiznesonlineSpider(scrapy.Spider):
    name = 'biznesonline'
    allowed_domains = ['business-gazeta.ru']
    start_urls = ['http://business-gazeta.ru/']

    def parse(self, response):
        pass
