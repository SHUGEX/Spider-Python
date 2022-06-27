"""
crawlspider > 模板  用来创建爬虫任务的模板
basic       > 模板    默认的
使用crawlspider作为模板创建爬虫任务 > 方便我们提取url
"""

"""
老案例  新模板 
使用crawlspider作为模板创建爬虫任务
scrapy genspider -t crawl  爬虫任务名称  爬取的范围域  scrapy genspider -t crawl  crawl_movie  xxx.com
"""

"""

LinkExtractor(链接提取器):规范url的提取范围
CrawlSpider：是一个类模板，继承自Spider,功能更加的强大
Rule(规则):规范url构造请求对象的规则

不需要再手动构造item对象
"""


"""
allow=(),里面写正则表达式匹配提取哪些url
deny=(),与allow完全相反，不常用 

allow_domains=(),允许的范围域
deny_domains=(),与上面相反 

restrict_xpaths=(),使用xpath来规范一个范围，再使用allow正则匹配提取，常用 

tags=('a', 'area'), 指定标签 

attrs=('href',),指定属性
"""



"""
疑问：解析主页的parse方法没有了
Rule对象，接收的就是起始页url的response
主页的rseponse > 只需要从中提取到详情页的url
因此，使用Rule对象直接提取，省去了方法，更加的简洁
快速地提取url

简化部分：主页response唯一可提取数据，url
1.解析主页的parse方法没有了,好处是提取url更加的简单，坏处是不能够再从主页中提取到其它的文本数据，仅仅只能够提取url


2.详情页的请求对象的构造，也被自动化了，由Rule直接进行发送

https://movie.douban.com/subject/\d+/   详情页url的正则表达式
https://movie.douban.com/subject/1292052/
https://movie.douban.com/subject/1291546/
https://movie.douban.com/subject/1292720/
https://movie.douban.com/subject/1292722/
https://movie.douban.com/subject/1295644/
https://movie.douban.com/subject/1292063/
https://movie.douban.com/subject/1291561/
https://movie.douban.com/subject/1295124/
https://movie.douban.com/subject/3541415/
https://movie.douban.com/subject/1889243/
https://movie.douban.com/subject/3011091/
https://movie.douban.com/subject/1292064/
https://movie.douban.com/subject/1292001/
https://movie.douban.com/subject/3793023/
https://movie.douban.com/subject/2131459/
https://movie.douban.com/subject/1291549/
https://movie.douban.com/subject/1307914/
https://movie.douban.com/subject/25662329/
https://movie.douban.com/subject/1292213/
https://movie.douban.com/subject/5912992/
https://movie.douban.com/subject/1296141/
https://movie.douban.com/subject/1291841/
https://movie.douban.com/subject/1849031/
https://movie.douban.com/subject/6786002/
https://movie.douban.com/subject/3319755/
"""

"""
总结:
使用crawlspider模板：
目的：方便快速提取主页的url
Rule对象的创建，替代了解析主页的parse方法
不再依靠item作为数据的载体
"""