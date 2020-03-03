import scrapy
import re

class NasaSpider(scrapy.Spider):
    name = 'nasaspider'
    start_urls = [
                  'https://hls.gsfc.nasa.gov/data/v1.4/L30/',
                  'https://hls.gsfc.nasa.gov/data/v1.4/S30/'
                 ]
    re_digits = '\d+'

    def parse(self, response):
        for text in response.selector.xpath('//table/tr/td/a/@href').getall():
            try:
                if int(re.match(re_digits, text).group()) >= 2017:
                    response.urljoin(text)
            except:
                pass


    