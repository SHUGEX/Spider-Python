# Scrapy settings for Douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Douban'

SPIDER_MODULES = ['Douban.spiders']
NEWSPIDER_MODULE = 'Douban.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 全局的用户代理(默认是被注释了，不生效的)
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

# Obey robots.txt rules
# robots协议 默认是遵守，使用的时候需要给它修改成False
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 控制速率，以秒为单位
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)

# 跟cookie相关的设置，默认是被注释的
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 全局默认 请求头
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
   'Cookie':'bid=3S5DolklESI; ll="118267"; _vwo_uuid_v2=D3EBE0F7503441D3959402C3D71EEFF0B|4519ecc1b3f605c6b3697a14afd4a59b; _ga=GA1.1.313176198.1627969259; _ga_RXNMP372GL=GS1.1.1635228400.1.1.1635228631.0; __gads=ID=b23142b8741ad35a-22d7870793ce0040:T=1628045181:RT=1636031363:S=ALNI_MYF8fqJxRCbH34B9ikAlBqa1r92rw; __yadk_uid=Rpl8jS0e38SKlLZxhLmR9Y05XHiVBxDg; douban-fav-remind=1; push_doumail_num=0; push_noty_num=0; gr_user_id=3fdfb9be-b87a-4cc3-912f-8f8b07904bd0; __utmv=30149280.23039; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; __gpi=UID=0000054e17920d2a:T=1652440669:RT=1656067139:S=ALNI_MacE_FArVxgYZLUPPx0fB49PDm03Q; dbcl2="235544536:kMI3acMtBFM"; ck=TzZ9; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1656074316%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_id.100001.4cf6=831bebd601806517.1627969259.184.1656074316.1656067175.; _pk_ses.100001.4cf6=*; __utma=30149280.313176198.1627969259.1656067139.1656074316.193; __utmb=30149280.0.10.1656074316; __utmz=30149280.1656074316.193.106.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.400287297.1627969259.1656067139.1656074316.181; __utmb=223695111.0.10.1656074316; __utmz=223695111.1656074316.181.96.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 开启爬虫中间件的地方，默认是注释的，是对request对象进行装饰(修饰)，添加UA cookie 代理
# SPIDER_MIDDLEWARES = {
#     # 路径                                    : 权重(优先级),权重数据越小，那么它的优先级就越高
#    'Douban.middlewares.DoubanSpiderMiddleware': 543,
#    'Douban.middlewares.sisiSpiderMiddleware': 546,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

# 下载器中间件
# DOWNLOADER_MIDDLEWARES = {
#    # 'Douban.middlewares.DoubanDownloaderMiddleware': 543,
#    'Douban.middlewares.DoubanDownloaderMiddleware': 543,
#    'Douban.middlewares.UserAgentDownloaderMiddleware': 544,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 开启管道
ITEM_PIPELINES = {
   'Douban.pipelines.DoubanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 手动指定编码
FEED_EXPORT_ENCODING = 'UTF-8'
