import scrapy
from ..items import *
from urllib.parse import urljoin  # 完成url拼接
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
        title_list = response.xpath('//a/span[@class="title"][1]/text()').getall()
        # 解析数据，得到评分列表
        score_list = response.xpath('//span[@class="rating_num"]/text()').getall()
        # 解析数据，得到详情页的url
        url_list = response.xpath('//div[@class="hd"]/a/@href').getall()

        # 保存
        # 1.把items里面的东西导入过来
        for title in enumerate(title_list):
            # 保存数据需要依靠items里面的模板
            items_ = DoubanItem()   # 字典对象 > 键值对 A:B  字典名[键名] = 值
            items_['name'] = title[1]  # 构造键值对，保存到items对象里
            # 数据已经上车item,准备进入管道保存，此时此刻，name：'肖申克的救赎
            for score in enumerate(score_list):
                # 需要一一匹配，判断，如果索引相同，那么就保存
                if score[0] == title[0]:
                    items_['score'] = score[1]
                    # 向对应详情页的url,构造请求对象
                    for url in enumerate(url_list):
                        if score[0] == url[0]:   # 回调函数，新的request对象得到的response由谁去进行解析
                            yield scrapy.Request(url[1],callback=self.parse_url,meta={'sisi':items_})  # meta参数传递items对象

                    # yield items_  # 相当于把数据给了管道进行保存  # 每一个item对象就保存了两个键值对 名称 和 评分

            # 解析下一页的url //a[text()="后页>"]/@href
            # 1.urllib.join
            # next_url = response.xpath('//a[text()="后页>"]/@href').get()
            # url_ = response.urljoin(next_url)
            # # 2.构造下一页的request对象
            # yield scrapy.Request(url_, callback=self.parse)  # meta参数传递items对象

            # 翻页的2种方法
            next_url = response.xpath('//a[text()="后页>"]/@href').get()
            yield response.follow(next_url,callback=self.parse)

    # 手动构造解析详情页的方法 > 接收详情页的response
    # 目的是添加一个键值对数据到items对象里面
    def parse_url(self,response):
        # 解析数据
        # //div[@class="indent"]/span[2]/text()
        # text_list = response.xpath('//div[@class="indent"]/span[2]/text()').getall()
        # for text in text_list:
        #     item_ = response.meta.get('sisi')
        #     item_['text'] = text
        #     yield item_



        text_list = response.xpath('//div[@class="indent"]/span[2]/text()').getall()
        # for循环，每一个部分都需要进行一个切割操作
        text = ''
        for text_ in text_list:
            text_ = text_.strip()
            text += text_ + ','  # 每次切割完空格，就把它添加进去

        # //div[@class="indent"]/span[1]/text()
        if text == "":
            text_list = response.xpath('//div[@class="indent"]/span[1]/text()').getall()
            text = ''
            for text_ in text_list:
                text_ = text_.strip()
                text += text_ + ','  # 每次切割完空格，就把它添加进去
        item_ = response.meta.get('sisi')
        item_['text'] = text
        yield item_


        # //div[@class="indent"]/span[1]/text()

