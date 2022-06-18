import scrapy


class WendaSpider(scrapy.Spider):
    name = 'wenda'                   # 爬虫任务名称
    allowed_domains = ['sisi.com']   # 爬取的范围，超出这个域名就不爬取
    start_urls = ['http://sisi.com/'] # 起始url

    def parse(self, response):   # 解析，自动接收了响应response
        pass
