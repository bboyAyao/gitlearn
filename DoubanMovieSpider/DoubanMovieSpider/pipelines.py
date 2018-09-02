# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs

class DoubanmoviespiderPipeline(object):

    def __init__(self):
        self.file = codecs.open('Movie.csv', 'w', 'utf-8')
        self.wr = csv.writer(self.file, dialect="excel")
        self.wr.writerow(['name', 'rank', 'nation', 'score', 'brief_intro'])

    def process_item(self, item, spider):
        self.wr.writerow([item['name'], item['rank'], item['nation'], item['score'], item['brief_intro']])
        return item

    def close_spider(self, spider):
        self.file.close()
