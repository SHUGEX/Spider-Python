# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline   # 图片管道

class PicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    image_urls = scrapy.Field()  # 默认字段名称不可修改
    name = scrapy.Field()   # 图片名称字段
    pass
