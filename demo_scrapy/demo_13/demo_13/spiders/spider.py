import scrapy
import json

def readInputData():
    data = []

    with open('input/data.json', 'r') as json_file:
        data = json.load(json_file)

    return data


class MySpider(scrapy.Spider):
    name = 'quotes'
    start_urls = []

    """ def __init__(self, *args, **kwargs):
        self.start_urls = kwargs.pop('url_list', [])
        super(MySpider, *args, **kwargs) """

    def __init__(self):
        self.start_urls = readInputData()

    def parse(self, response):
        for text in response.xpath('//text').getall():
            
            with open('results/fileout.txt', 'a') as f:
                json.dump(data, f)