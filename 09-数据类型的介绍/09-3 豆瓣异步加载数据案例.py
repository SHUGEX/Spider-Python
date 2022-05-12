"""
演示豆瓣电影异步加载数据的抓取 动态数据
"""

import requests

if __name__ == '__main__':
    # 1.确认目标的url
    url_ = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"

    # 构造用户代理
    headers_ = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }

    # 2.发送网络请求，获取响应对象
    response_ = requests.get(url_,headers=headers_)
    str_data = response_.text

    # 4.保存
    with open('douban_01.json','w',encoding="utf-8") as f:
        f.write(str_data)