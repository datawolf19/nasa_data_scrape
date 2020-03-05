# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



class DeepspacePipeline(object):
    def process_item(self, item, spider):
        print('\n'*5, 'PIPELINE BABY', '\n'*5)
      
        with open(item['file_urls'].split('/')[-1], 'wb') as f:
            f.write(item['files'])
        return item
