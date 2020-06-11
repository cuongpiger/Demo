import scrapy
import os

class ThreadsSpider(scrapy.Spider):
    name = "threads"
    folder_path = "save_file"
    def start_requests(self):
        os.mkdir(self.folder_path)
        urls = []
        for i in range(1,500):
            url = 'http://f319.com/forums/thi-truong-chung-khoan.3/page-%s'% i
            urls.append(url)
            
        for url in urls:        
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("-")
        if len(page) < 2: 
            page = 1
        else:
            page = page[-1]
        filename = 'page-%s.html' % page
        
        
        with open(self.folder_path+"/"+filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)