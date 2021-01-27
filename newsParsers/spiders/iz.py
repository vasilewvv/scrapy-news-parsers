import scrapy


class IzSpider(scrapy.Spider):
    name = 'iz'
    allowed_domains = ['iz.ru']
    start_urls = ['https://iz.ru/feed/']

    def parse(self, response):
        for news in response.css('a.lenta_news__day__list__item'):
            try:
                yield {
                    'title': news.css('div.lenta_news__day__list__item__title::text').get().strip(),
                    'date': news.css('time::text').get().strip(),
                    'link': f"https://iz.ru{news.css('a.lenta_news__day__list__item::attr(href)').get()}"
                }
            except:
                pass

        next_page = response.css('a.button::attr(href)').get()
        if next_page is not None:
            yield response.follow(f"https://iz.ru{next_page}", callback=self.parse)
