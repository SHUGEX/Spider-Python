# <<爬虫作业>>
# 1、-->爬取百度贴吧美食吧,爬取10页数据

import requests
from urllib.parse import quote
from fake_useragent import FakeUserAgent

if __name__ == "__main__":
    input_wd = input("请输入搜素关键字：")
    wd_ = quote(input_wd)
    url_ = "https://tieba.baidu.com/f?"
    page_ = 50
    for i in range(10):

        use_agent_demo = FakeUserAgent().random

        headers_ = {
            "User-Agent": use_agent_demo
        }
        params_ = {
            "kw": wd_,
            "pn": page_*i
        }
        response_ = requests.get(url_, headers=headers_, params=params_)
        bytes_date = response_.content
        str_date = bytes_date.decode()
        with open(f"test04_1_tieba_{input_wd}.html", "a+", encoding="utf-8") as f:
            f.write(str_date)
            print(f"<<贴吧-{input_wd}-第{i+1}页爬取成功！>>")

# 2、-->网易云一张图片的下载、一首非VIP歌曲的下载、一个MV的下载
import requests
from urllib.parse import quote
from fake_useragent import FakeUserAgent
from lxml import etree

if __name__=="__main__":
    url_ = "https://music.163.com/discover/playlist/?"
    input_cat = input("请输入图片的音乐风格(例:古风):")
    cat_ = quote(input_cat)
    use_agent_ = FakeUserAgent().random
    headers_ = {
        "User-Agent": use_agent_
    }
    params_ = {
        "cat": cat_
    }
    response_ = requests.get(url_,headers=headers_,params=params_)
    str_date = response_.content.decode()
    html_obj = etree.HTML(str_date)
    item_list = html_obj.xpath('.//li')    # 标签里面没有别的内容了
    for i in item_list:
        url = i.xpath('.//img[@class="j-flag"]/@src')
        name = i.xpath('.//a/@title')
        use_agent_ = FakeUserAgent().random
        headers_ = {
            "User-Agent": use_agent_
        }

        # 这里报错了
        response = requests.get(url[0], headers=headers_)  # IndexError: list index out of range

        with open(f"X:/jpg/{input_cat}_{name[0]}.jpg", "wb") as f:
            f.write(response.content)
        print(f"<<{name[0]}>>")

        x = ()

"""
音乐和MV的下载地址不知道怎么找...

"""
