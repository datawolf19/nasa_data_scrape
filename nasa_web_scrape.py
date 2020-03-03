import scrapy

class NasaSpider(scrapy.Spider):
    name = 'nasaspider'
    start_urls = [
                  'https://hls.gsfc.nasa.gov/data/v1.4/L30/',
                  'https://hls.gsfc.nasa.gov/data/v1.4/S30/'
                 ]

    