# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviespiderItem(scrapy.Item):
    # 爬取豆瓣电影排行榜，电影名称，电影评分，电影信息，电影简介
    name = scrapy.Field()
    score = scrapy.Field()
    nation = scrapy.Field()
    brief_intro = scrapy.Field()
    rank = scrapy.Field()

