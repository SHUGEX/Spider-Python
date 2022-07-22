from scrapy_redis.dupefilter import RFPDupeFilter
from scrapy_redis.scheduler import Scheduler
"""
# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 过滤                 指定路径做过滤操作的类模板
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器       指定替换原来的调度器的类模板
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#         持久化     指定断点续爬
SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# 指定替换掉原来的管道，使用redis去进行替换
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.

# 下载延迟
DOWNLOAD_DELAY = 1

"""



from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'myspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }

"""
需要一个redis_key 目前作用未知
注释掉start_urls  因为每一台服务器如果都是从同一个url开始运行，那么执行流程基本一样，就失去了分布式的意义 

需要修改的地方
1.继承的改变
2.start_url的注释
3.redis_key的增加
"""



"""
假设现在是四台服务器
一起开启爬虫任务
四台服务器同时卡住   
 listening on 127.0.0.1:6023  监听redis数据库
 
 往redis数据库里面以列表的形式放入start_urls
 随机指定一个服务器拿到了start_urls  进行解析 response里面100url
 100个url构造100个request请求对象  给redis进行任务的分发
 分给了各个服务器，解开堵塞状态 ，请求数据提取完 > redis 
"""