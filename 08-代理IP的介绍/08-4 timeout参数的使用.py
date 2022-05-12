"""
timeout参数的使用
规定你的响应时间

每一个代理IP的响应时间不一样
1.剔除掉不能够使用的代理IP
2.有些响应时间过长，timeout参数用来剔除掉响应时间过长的代理
"""

import requests

from lxml import etree

if __name__ == '__main__':
    # 特殊测IP的url
    url_ = "https://tool.lu/ip/"

    # 用户代理 cookie
    headers_ = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }

    proxies_ = {"https": "http://1.1.1.1:8888"}  # 假的代理IP，无法使用的代理IP
    #
    #     # 使用代理IP
    response_ = requests.get(url_,headers=headers_,proxies=proxies_,timeout=3)  # 设置响应时间，秒为单位
    # response_ = requests.get(url_,headers=headers_)
    str_data = response_.content.decode()
    # print(str_data)

    # 目前不用了解，只是配合案例
    html_obj = etree.HTML(str_data)
    data_ = html_obj.xpath('//form[@id="main_form"]/p[1]/text()')[0]
    print(data_)