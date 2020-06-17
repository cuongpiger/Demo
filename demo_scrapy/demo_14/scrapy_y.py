import scrapy
import json

def readJson(filename):
    with open('data.json') as json_file:
        data = json.load(json_file)

    return data


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = []

    def __init__(self):
        self.start_urls = readJson('data.json')

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            self.log(f'Next page is ========================== {next_page}')
            yield response.follow(next_page, self.parse)

# scrapy runspider scrapy_y.py
# scrapy runspider scrapy_y.py -o quotes.json