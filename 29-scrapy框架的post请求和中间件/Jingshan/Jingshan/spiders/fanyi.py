import scrapy
import jsonpath

class FanyiSpider(scrapy.Spider):
    name = 'fanyi'      # 爬虫任务名称
    allowed_domains = ['iciba.com']   # 允许的范围域
    # start_urls = ['http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=0d2d6b4f80839676'] # 起始url

    # 重写构造起始url的方法
    def start_requests (self):
        # 目标url
        url_ = "http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=0d2d6b4f80839676"

        # 构造form表单数据
        form_data = {
            "from": "zh",
            "to": "en",
            "q": "你好"
        }

        # 2.构造请求对象
        yield scrapy.FormRequest(url_,formdata=form_data,callback=self.parse)

    def parse(self, response):
        py_data = response.json()
        res_ = jsonpath.jsonpath(py_data,'$..out')[0]
        print(f'翻译结果为:',res_)
