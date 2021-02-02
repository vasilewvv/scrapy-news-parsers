import scrapy


class A3dnewsSpider(scrapy.Spider):
    name = '3dnews'
    allowed_domains = ['3dnews.ru']
    start_urls = ['https://3dnews.ru/news/']

    def parse(self, response):
        for news in response.css('div.article-entry'):
            try:
                link = news.css('div.imgPrevWrapper a::attr(href)').get().strip()
                if link[0] == "h":
                    pass
                else:
                    link = f"https://3dnews.ru{link}"
                yield {
                    'title': news.css('h1::text').get().strip(),
                    'desc': news.css('p::text').get().strip(),
                    'date': news.css('span.entry-date::text').get().strip(),
                    'link': link
                }
            except:
                pass

        next_page = response.css('a.right::attr(href)').get()
        next_page = f"https://3dnews.ru{next_page}"
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
