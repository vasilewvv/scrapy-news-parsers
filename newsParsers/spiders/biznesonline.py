import scrapy


class BiznesonlineSpider(scrapy.Spider):
    name = 'biznesonline'
    allowed_domains = ['business-gazeta.ru']
    start_urls = ['https://www.business-gazeta.ru/category/6']

    def parse(self, response):
        for news in response.css('article'):
            try:
                yield {
                    'title': news.css('a.article-news__title::text').get().strip(),
                    'comments': news.css('span.comments-num::text').get().strip(),
                    'link': f"https://www.business-gazeta.ru{news.css('a.article-news__title::attr(href)').get()}"
                }
            except:
                pass

        next_page = f"https://www.business-gazeta.ru{response.css('a.person-page__more.js-pager__more::attr(href)').get()}"
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
