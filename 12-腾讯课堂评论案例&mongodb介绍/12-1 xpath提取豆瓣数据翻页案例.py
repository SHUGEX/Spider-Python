"""
演示xpath解析豆瓣案例
"""
import time

"""
第一页：https://movie.douban.com/top250?start=0&filter=         0*25
第二页：https://movie.douban.com/top250?start=25&filter=        1*25
第三页：https://movie.douban.com/top250?start=50&filter=        2*25
一页有25部电影，控制翻页的关键参数是start参数，start参数是以25进行一个递增的等差数列，或者说25的倍数

翻页的注意点：
反爬点：
注意降低请求频率
"""

# 导入发送网络请求的requests库
import requests
# 导入处理xpath的第三方库
from lxml import etree  # etree下面报红色波浪线，并不是代码错误，而是编辑器的导包路径问题，并不会影响代码的正常运行
import json
if __name__ == '__main__':
    dict_ = {}
    for i in range(10):
        # 确认目标的url
        url_ = f"https://movie.douban.com/top250?start={i*25}&filter="

        headers_ = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }

        # 2.发送网络请求，获取响应对象
        response_ = requests.get(url_, headers=headers_)
        str_data = response_.text
        # print(str_data)

        # 3.提取数据
        # str类型无法直接被xpath语法处理，所以需要转化类型
        html_obj = etree.HTML(str_data)    # 得到一个html对象

        title_list = html_obj.xpath('//a/span[@class="title"][1]/text()')   # 得到的结果是一个列表
        url_list = html_obj.xpath('//div[@class="hd"]/a[@class=""]/@href')   # 得到的结果是一个列表

        # 因为我们把字典放到了循环内部，导致下一次循环字典又变成了空字典
        for i in range(len(title_list)):
            dict_[title_list[i]] = url_list[i]

        # 手动延迟，降低请求频率，避免被反爬
        time.sleep(1)

    print(len(dict_))
    print(dict_)