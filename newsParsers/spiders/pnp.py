import scrapy


class PnpSpider(scrapy.Spider):
    name = 'pnp'
    start_urls = ['https://www.pnp.ru/news/1/']

    def parse(self, response):
        for news in response.css('div.item.have_image'):
            yield {
                'title': news.css('div.title a::text').get(),
                'date': news.css('p span::text').get(),
                'author': news.css('p a::text').get(),
                'link': news.css('div.title a::attr(href)').get()
            }
        for num in range(2, 10):
            yield response.follow(f"https://www.pnp.ru/news/{num}/", callback=self.parse)
