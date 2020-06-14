import scrapy


class MySpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://quotes.toscrape.com/page/3/',
    ]

    def parse(self, response):
        for text in response.xpath('//text').getall():
            yield {"text": text}