"""
爬虫中间件
下载中间件
它们的位置 决定了它们的作用
"""

"""
爬虫中间件:
from_crawler   >>>>  在爬虫任务创建的时候会调用

process_spider_input >>>>  每一个响应对象经过的时候，被调用

process_spider_output  >>>> 输出的对象，要么是请求对象，要么是item对象 

process_spider_exception  >>>> 处理异常

process_start_requests >>>> 构造起始url有关

spider_opened >>>> 调试信息的输出
"""



"""
下载器中间件
from_crawler  >>>> 在爬虫任务创建的时候会调用

重点:
process_request  >>>> 处理即将发送给下载器(拿着请求对象发送网络请求)的请求对象
                        构造用户代理
                            代理IP
                            Cookie
                            Referer

process_response  >>>> 100个请求对象，100个响应response
                        有一个统一的功能需要添加


process_exception  >>>>  异常处理

spider_opened    >>>> 调试信息的输出
"""


"""
这两个DoubanSpiderMiddleware
    DoubanDownloaderMiddleware
    它只是scrapy提供给咱们的一个模板写法
    默认是没有生效的
"""