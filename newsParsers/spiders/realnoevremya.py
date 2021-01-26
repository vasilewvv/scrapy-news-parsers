import scrapy


class RealnoevremyaSpider(scrapy.Spider):
    name = 'realnoevremya'
    allowed_domains = ['realnoevremya.ru']
    start_urls = ['https://realnoevremya.ru/news']

    def parse(self, response):
        for news in response.css('li.card'):
            try:
                yield {
                    'title': news.css('strong::text').get().strip(),
                    'date': news.css('span.border.date::text').get().strip(),
                    'category': news.css('a.border.l-category::text').get().strip(),
                    'link': f"https://realnoevremya.ru{news.css('a::attr(href)').get()}",
                }
            except:
                pass

        next_page = response.css('div.pageNav li.current+li a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
