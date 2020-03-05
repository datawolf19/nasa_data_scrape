import scrapy
import re

class NasaSpider(scrapy.Spider):
    # This is the name that should be used to call the spider in the
    # terminal: 
    # $: scrapy crawl nasaspider
    name = 'spacespider'
    start_urls = [
                  'https://hls.gsfc.nasa.gov/data/v1.4/L30/'
                  #,'https://hls.gsfc.nasa.gov/data/v1.4/S30/'
                 ]

    
    def parse(self, response):
        for text in response.xpath('*//a/@href').re('\d{4}'):
            try:
                if int(text) >= 2017:
                    yield {'year':text}
            except:
                pass


    