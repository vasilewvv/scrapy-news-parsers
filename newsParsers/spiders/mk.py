import scrapy


class MkSpider(scrapy.Spider):
    name = 'mk'
    allowed_domains = ['mk.ru']
    start_urls = ['https://www.mk.ru/news/']

    def parse(self, response):
        for news in response.css('li.news-listing__item'):
            try:
                yield {
                    'title': news.css('h3::text').get().strip(),
                    'date': news.css('span.news-listing__item-time::text').get().strip(),
                    'link': news.css('a::attr(href)').get()
                }
            except:
                pass

        next_page = response.css('li.news-listing__pagination-item.news-listing__pagination-item_active + li a::attr(href)').get()
        if next_page is not None:
            yield response.follow(f"https://www.mk.ru{next_page}", callback=self.parse)
