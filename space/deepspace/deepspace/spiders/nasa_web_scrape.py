import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from deepspace.items import DeepspaceItem
#from deepspace.pipelines import DeepspacePipeline

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

    def parse_folder(self, response):
        # file_page = response.xpath('//a/@href').re('^[^?/].*hdr')
        # if file_page:
        #     print('\n\n\nGOING TO PARSE_ITEM\n\n\n')
        #     print(response.url)
        #     print('\n\n\nGOING TO PARSE_ITEM\n\n\n')
        #     yield scrapy.Request(response.url, callback=self.parse_hdf)
            
        next_page = response.xpath('*//a/@href').re('^[^?/].*')
        if next_page:
            for page in next_page:
                if page.split('.')[-1] in ('hdr'):
                    print('\n'*5, 'GOING TO PARSER', '\n'*5)
                    yield scrapy.Request(response.urljoin(page), callback=self.parse_item)
                else:
                    print('\n'*5, 'FOLDER DIVING', '\n'*5)
                    yield scrapy.Request(response.urljoin(page), callback=self.parse_folder)


    def parse(self, response):
        """Selects the years from the webpage."""
        next_page = response.xpath('*//a/@href').re('^[^?/].*\d?')
        print(type(next_page))
        if next_page:
            for page in [next_page[0]]:
                print(page)
                yield scrapy.Request(response.urljoin(page), callback=self.parse_folder)
                

    
            
    def parse_item(self, response):
        print('\n'*5, 'PARSER', '\n'*5)
        item = DeepspaceItem()
        item['file_urls'] = response.url
        item['files'] = response.body
        return item
        



        

            


    