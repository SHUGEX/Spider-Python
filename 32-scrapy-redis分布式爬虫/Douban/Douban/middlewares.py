# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 爬虫中间件
# class DoubanSpiderMiddleware:
#     """爬虫器中间件模板，默认是没有生效的，需要在配置文件settings中配置"""
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Request or item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# # 下载器中间件
# class DoubanDownloaderMiddleware:
#     """下载器中间件模板"""
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)




from fake_useragent import FakeUserAgent
# 自定义下载器中间件
class DoubanDownloaderMiddleware:
    def process_request (self, request, spider):
        """处理请求对象"""
        request.cookies = {'bid': '3S5DolklESI', 'll': '"118267"', '_vwo_uuid_v2': 'D3EBE0F7503441D3959402C3D71EEFF0B|4519ecc1b3f605c6b3697a14afd4a59b', '_ga': 'GA1.1.313176198.1627969259', '_ga_RXNMP372GL': 'GS1.1.1635228400.1.1.1635228631.0', '__gads': 'ID', '__yadk_uid': 'Rpl8jS0e38SKlLZxhLmR9Y05XHiVBxDg', 'douban-fav-remind': '1', 'push_doumail_num': '0', 'push_noty_num': '0', 'gr_user_id': '3fdfb9be-b87a-4cc3-912f-8f8b07904bd0', '__utmv': '30149280.23039', 'ap_v': '0,6.0', '__utmc': '223695111', '__gpi': 'UID', 'dbcl2': '"235544536:kMI3acMtBFM"', 'ck': 'TzZ9', '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1656074316%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D', '_pk_id.100001.4cf6': '831bebd601806517.1627969259.184.1656074316.1656067175.', '_pk_ses.100001.4cf6': '*', '__utma': '223695111.400287297.1627969259.1656067139.1656074316.181', '__utmb': '223695111.0.10.1656074316', '__utmz': '223695111.1656074316.181.96.utmcsr'}
        return None

# 构建一个添加用户代理的下载器中间件
class UserAgentDownloaderMiddleware:
    def process_request (self, request, spider):
        """处理请求对象"""
        user_agent = FakeUserAgent().random

        # 用户代理User-Agent的使用
        request.headers['User-Agent'] = user_agent

        # 代理IP的使用             协议    IP      端口  user:password
        request.meta['proxy'] = 'https://1.1.1.1:8888'

        # 跳转Referer的设置
        referer = request.url

        if referer:
            request.headers['referer'] = referer

        return None