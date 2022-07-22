import scrapy   # 没有被直接作用到
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class CrawlMovieSpider(CrawlSpider):
    name = 'crawl_movie'    # 爬虫任务的名称
    allowed_domains = ['douban.com']   # 范围域
    start_urls = ['https://movie.douban.com/top250'] # 起始的url

    rules = ( # 创建了一个Rule对象(创建了一个LinkExtractor对象)，每一个对象都是详情页的请求对象的构造
        # 提取详情页的url,匹配到的详情页url自动发送请求
        Rule(LinkExtractor(allow=r'^https://movie.douban.com/subject/\d+/$'), callback='parse_item', follow=False),
        # 提取下一页的url
        Rule(LinkExtractor(restrict_xpaths=r'//a[text()="后页>"]'), follow=True),

    )

    def parse_item(self, response):  # 解析详情页的方法
        item = {}
        # 电影名称
        title_ = response.xpath('//h1/span[1]/text()').get()
        # 评分
        score_ = response.xpath('//strong/text()').get()
        # 导演
        man_ = response.xpath('//div[@id="info"]/span[1]/span/a/text()').get()

        # 尝试不使用item构造的字段
        item['ziyi'] = title_
        item['maiya'] = score_
        item['susu'] = man_

        return item


# import scrapy   # 没有被直接作用到
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
#
#
# class CrawlMovieSpider(CrawlSpider):
#     name = 'crawl_movie'    # 爬虫任务的名称
#     allowed_domains = ['douban.com']   # 范围域
#     start_urls = ['https://movie.douban.com/top250'] # 起始的url
#
#     rules = ( # 创建了一个Rule对象(创建了一个LinkExtractor对象)，每一个对象都是详情页的请求对象的构造
#         # 提取详情页的url,匹配到的详情页url自动发送请求
#         Rule(LinkExtractor(allow=r'^https://movie.douban.com/subject/\d+/$'), callback='parse_item', follow=False),
#         # 提取下一页的url
#         Rule(LinkExtractor(restrict_xpaths=r'//a[text()="后页>"]'), follow=True),
#
#     )
#
#     # 按照我们之前的理解
#     # def parse(self, response):  # 主页的response
#     #     """
#     #     url_list = response.xpath('xxxxxx')   # 得到一个详情页的url列表
#     #     # for循环迭代url列表
#     #
#     #     # 拿着每一个单独的url去构造request对象，yield出去
#     #     """
#
#     def parse_item(self, response):  # 解析详情页的方法
#         item = {}
#         #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
#         #item['name'] = response.xpath('//div[@id="name"]').get()
#         #item['description'] = response.xpath('//div[@id="description"]').get()
#         # 电影名称
#         title_ = response.xpath('//h1/span[1]/text()').get()
#         # 评分
#         score_ = response.xpath('//strong/text()').get()
#         # 导演
#         man_ = response.xpath('//div[@id="info"]/span[1]/span/a/text()').get()
#
#         # 尝试不使用item构造的字段
#         item['ziyi'] = title_
#         item['maiya'] = score_
#         item['susu'] = man_
#
#         return item
