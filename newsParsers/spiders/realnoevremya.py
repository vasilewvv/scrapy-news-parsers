import scrapy


class RealnoevremyaSpider(scrapy.Spider):
    name = 'realnoevremya'
    allowed_domains = ['realnoevremya.ru']
    start_urls = ['http://realnoevremya.ru/']

    def parse(self, response):
        pass
