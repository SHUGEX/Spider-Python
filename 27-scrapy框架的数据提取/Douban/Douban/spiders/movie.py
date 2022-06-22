import scrapy
from ..items import *

class MovieSpider(scrapy.Spider): # 自动继承自Spider类
    name = 'movie'     # 爬虫任务名称
    allowed_domains = ['douban.com']  # 允许爬取的范围
    start_urls = ['https://movie.douban.com/top250'] # 起始url

    def parse(self, response):  # 解析,方法名称固定，不要自行修改
        """response接受的就是起始url发送了请求之后的响应response"""
        # 电影名称，xpath直接定位
        # title_ = response.xpath('//a/span[@class="title"][1]/text()')
        # print(title_)

        # 数据的提取
        # title_ = response.xpath('//a/span[@class="title"][1]/text()').extract()
        # title_ = response.xpath('//a/span[@class="title"][1]/text()').extract_first()
        # title_ = response.xpath('//a/span[@class="title"][1]/text()').get()
        # title_ = response.xpath('//a/span[@class="title"][1]/text()').getall()
        # print(title_)

        # 解析数据，得到了电影名称的列表
        title_ = response.xpath('//a/span[@class="title"][1]/text()').getall()

        # 保存
        # 1.把items里面的东西导入过来
        for title in title_:
            # 保存数据需要依靠items里面的模板
            items_ = DoubanItem()   # 字典对象 > 键值对 A:B  字典名[键名] = 值
            items_['name'] = title  # 构造键值对，保存到items对象里
            # 数据已经上车item,准备进入管道保存，此时此刻，name：'肖申克的救赎
            yield items_  # 相当于把数据给了管道进行保存

        # 电影评分，xpath直接定位


        pass
