import scrapy


class TopwarSpider(scrapy.Spider):
    name = 'topwar'
    allowed_domains = ['topwar.ru']
    start_urls = ['https://topwar.ru/news/']

    def parse(self, response):
        for news in response.css('article.post.item'):
            try:
                yield {
                    'title': news.css('h2 a::text').get().strip(),
                    'desc': news.css('div.post-text::text').get().strip(),
                    'date': news.css('time::attr(datetime)').get().strip(),
                    'views': news.css('div.meta__views::text').get().strip(),
                    'comments': news.css('div.meta__coms::text').get().strip(),
                    'link': news.css('h2 a::attr(href)').get()
                }
            except:
                pass

        next_page = response.css('nav.pages-list a::attr(href)')[1].get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
