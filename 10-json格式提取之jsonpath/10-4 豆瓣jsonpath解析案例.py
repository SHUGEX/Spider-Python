"""
演示豆瓣电影异步加载数据的抓取 动态数据
"""

import requests
import jsonpath
if __name__ == '__main__':
    # 1.确认目标的url
    url_ = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"

    # 构造用户代理
    headers_ = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }

    # 2.发送网络请求，获取响应对象
    response_ = requests.get(url_,headers=headers_)

    # 利用json方法转成python格式的数据
    py_data = response_.json()

    # 解析出电影名称跟评分 >> jsonpath
    title_list = jsonpath.jsonpath(py_data,"$..title")
    score_list = jsonpath.jsonpath(py_data,"$..score")
    # print(title_list)
    # print(score_list)

    # 转成键值对对应的字典
    movie_dict = {}
    for i in range(len(title_list)):
        movie_dict[title_list[i]] = score_list[i]
    print(movie_dict)
    # zip_obj = zip(title_list,score_list)
    # for i in zip_obj:
    #     print(i)




