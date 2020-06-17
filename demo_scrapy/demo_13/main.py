# from scrapy.crawler import CrawlerProcess
# from demo_13.spiders.spider import MySpider
import json
import os
# from scrapy.py import MySpider

""" def readInputData():
    data = []

    with open('input/data.json', 'r') as json_file:
        data = json.load(json_file)

    return data """

""" process = CrawlerProcess()
process.crawl(MySpider, url_list=readInputData())
process.start() """

os.system('scrapy runspider scrapy.py')
