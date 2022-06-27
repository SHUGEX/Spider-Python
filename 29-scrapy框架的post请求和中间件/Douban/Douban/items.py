# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影名称
    name = scrapy.Field()
    # 电影评分
    score = scrapy.Field()
    # 电影介绍
    text = scrapy.Field()
    pass
