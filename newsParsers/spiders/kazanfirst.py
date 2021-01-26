import scrapy


class KazanfirstSpider(scrapy.Spider):
    name = 'kazanfirst'
    start_urls = ['https://kazanfirst.ru/news']

    def parse(self, response):
        for news in response.css('a.post-item.column-list__item.js-column-item'):
            try:
                yield {
                    'title': news.css('h3.post__title::text').get().strip(),
                    'date': news.css('span.post-info__time::text').get(),
                    'desc': news.css('span.post__description::text').get().strip(),
                    'category': news.css('span.post-info__article::text').get().strip(),
                    'link': news.css('div a::attr(href)').get()
                }
            except:
                pass

        # next_page = response.css('ul.pagination a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
