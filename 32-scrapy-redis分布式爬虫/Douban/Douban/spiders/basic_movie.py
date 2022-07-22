import scrapy


class BasicMovieSpider(scrapy.Spider):
    name = 'basic_movie'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
