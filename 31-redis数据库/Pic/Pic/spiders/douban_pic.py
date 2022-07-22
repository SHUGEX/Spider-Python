import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import *

class DoubanPicSpider(CrawlSpider):
    name = 'douban_pic'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'^https://movie.douban.com/subject/\d+/$'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # 构造保存图片url的item对象
        item_ = PicItem()

        # 得到图片的url
        url_ = response.xpath('//div[@id="mainpic"]/a/img/@src').get()  # 字符串的方式
        # 需要把图片的url发送到图片管道
        item_['image_urls'] = [url_]   # 以列表的方式 构造了以item对象为载体的数据

        # 获取图片名称
        name_ = response.xpath('//h1/span[1]/text()').get()
        item_['name'] = name_

        return item_
