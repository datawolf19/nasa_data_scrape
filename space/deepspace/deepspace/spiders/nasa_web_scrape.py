import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from deepspace.items import DeepspaceItem

class NasaSpider(scrapy.Spider):
    # This is the name that should be used to call the spider in the
    # terminal: 
    # $: scrapy crawl nasaspider
    name = 'spacespider'
    

    start_urls = [
                  'https://hls.gsfc.nasa.gov/data/v1.4/L30/'
                  #,'https://hls.gsfc.nasa.gov/data/v1.4/S30/'
                 ]

    files_urls = []

    def parse(self, response):
        # for text in response.xpath('*//a/@href').re('^[^?/].*'):
        #     # identifies the years
        #     url = response.urljoin(text)
        
            
        file = response.xpath('//a/@href').re('^[^?/].*hdr')
        if file:
            for f in file:
                file_url = response.urljoin(f)
                file_extension = file_url.split('.')[-1]
                if file_extension not in ('.hdr'):
                    return
                item = DeepspaceItem()
                item['file_urls'] = [file_url]
                yield item
 
        next_page = response.xpath('*//a/@href').re('^[^?/].*')
        if next_page:
            yield scrapy.Request(response.urljoin(next_page[0]), callback=self.parse)

        

    def parse_item(self, response):
        pass 
        

            


    