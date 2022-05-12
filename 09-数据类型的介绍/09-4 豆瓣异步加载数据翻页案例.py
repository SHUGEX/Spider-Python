"""
演示翻页
"""
import time

"""
翻页的url的规律
第一页：https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
第二页：https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20
第三页：https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=40&limit=20
经过发现：url start参数是以20的等差数列进行翻页
"""

import requests

if __name__ == '__main__':
    pages_ = int(input('请输入你想抓以的页数:'))
    for i in range(pages_):  # 3 0 1 2
        # 1.确认目标的url
        url_ = f"https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={i*20}&limit=20"

        # 构造用户代理
        headers_ = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }

        # 2.发送网络请求，获取响应对象
        response_ = requests.get(url_, headers=headers_)
        str_data = response_.text

        # 4.保存
        with open(f'douban_{i+1}.json', 'w', encoding="utf-8") as f:
            f.write(str_data)

        time.sleep(1.5)   # 每爬取完一页就等待1.5秒，符合正常人的操作 降低请求频率