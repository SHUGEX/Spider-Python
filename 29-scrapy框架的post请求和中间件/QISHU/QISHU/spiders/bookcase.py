import scrapy


class BookcaseSpider(scrapy.Spider):
    name = 'bookcase'
    allowed_domains = ['qishu7.com']
    # start_urls = ['http://www.qishu7.com/modules/article/bookcase.php']

    def start_requests(self):
        url_ = "http://www.qishu7.com/modules/article/bookcase.php"
        cookie_ = 'UM_distinctid=17fdfc949e53ee-011b40f6521126-576153e-1fa400-17fdfc949e6589; CNZZDATA1254529914=2131565625-1648718962-https%253A%252F%252Fwww.baidu.com%252F%7C1651650450; PHPSESSID=qme0973nua4g01dkbogde5aqo5; jieqiUserInfo=jieqiUserId%3D1164%2CjieqiUserUname%3Dsixstar_dahai%2CjieqiUserName%3Dsixstar_dahai%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D%2CjieqiUserHonor%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserUname_un%3Dsixstar_dahai%2CjieqiUserName_un%3Dsixstar_dahai%2CjieqiUserHonor_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1656067210; jieqiVisitInfo=jieqiUserLogin%3D1656067210%2CjieqiUserId%3D1164'
        cookie_dict = {i.split('=')[0]:i.split('=')[1] for i in cookie_.split('; ')}
        yield scrapy.Request(url_,cookies=cookie_dict,callback=self.parse)

    def parse(self, response):
        print(response.body.decode('gbk'))
