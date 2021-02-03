import scrapy


class CnewsSpider(scrapy.Spider):
    name = 'cnews'
    allowed_domains = ['cnews.ru']
    start_urls = ['https://www.cnews.ru/archive/']

    def parse(self, response):
        for news in response.css('div.allnews_item'):
            try:
                ctime = news.css('div.ani-date time::text').get()
                date = ctime[0].strip()
                time = ctime[1].strip()
                yield {
                    'title': news.css('a::text').get().strip(),
                    'link': news.css('a::attr(href)').get()
                }
            except:
                pass
        page = 2
        while page < 50:
            next_page = f"https://www.cnews.ru/archive/type_top_lenta_articles/page_{page}"
            page += 1
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
