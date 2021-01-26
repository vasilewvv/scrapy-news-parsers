import scrapy


class ChizExpressSpider(scrapy.Spider):
    name = 'chizexpress'
    start_urls = ['https://chelny-izvest.ru/news/widget/list/ekspress-novostinews-page/page/1']

    def parse(self, response):
        for news in response.css('div.widget-view-small'):
            try:
                yield {
                    'title': news.css('div a::text').get().strip(),
                    'date': news.css('div.widget-view-small__date::text').get().strip(),
                    'desc': news.css('div.widget-view-small__description::text').get().strip(),
                    'link': news.css('div a::attr(href)').get()
                }
            except:
                pass

        next_page = response.css('ul.pagination a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
