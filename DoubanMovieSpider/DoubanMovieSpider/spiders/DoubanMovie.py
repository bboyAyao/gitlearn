# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
from DoubanMovieSpider.items import DoubanmoviespiderItem

class DoubanmovieSpider(CrawlSpider):
    name = 'DoubanMovie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=0']

    content_link = LinkExtractor(allow=(r'/subject/\d+/'),restrict_xpaths=('//div[@class="hd"]'))
    page_link = LinkExtractor(allow=(r'\?start=\d+&filter='),restrict_xpaths=('//span[@class="next"]/a'))

    rules = [
        Rule(content_link,callback="parse_item"),
        Rule(page_link)
    ]

    def parse_item(self, response):
        results = response.xpath("//div[@id='content']")
        for each_movie in results:
            rank = each_movie.xpath(".//div[@class='top250']/span[@class='top250-no']/text()").extract()[0]
            name = each_movie.xpath(".//h1/span[1]/text()").extract()[0].replace(",","/")
            pattern = re.compile(r'<span class="pl">制片国家/地区:</span>(.*?)<br>')
            nation = pattern.search(each_movie.extract()).group(1)
            nation = "".join(nation.split())
            score = each_movie.xpath(".//div[@class='rating_self clearfix']/strong/text()").extract()[0]
            brief_intro = each_movie.xpath(".//span[@property='v:summary']/text()").extract()
            if len(brief_intro)>0:
                brief_intro = "".join(brief_intro[0].split())
            else:
                brief_intro = "无"

            item = DoubanmoviespiderItem()
            item['rank'] = rank
            item['name'] = name
            item['nation'] = nation
            item['score'] = score
            item['brief_intro'] = brief_intro

            print("电影名称：",name)
            print("排名：", rank)
            print("评分：", score)
            print("地区：", nation)
            print("简介：", brief_intro)

            yield item