"""
演示python交互xpath语法
"""
"""
python想要执行xpath语法，需要一个第三方库 lxml 
"""



# 导入发送网络请求的requests库
import requests
# 导入处理xpath的第三方库
from lxml import etree  # etree下面报红色波浪线，并不是代码错误，而是编辑器的导包路径问题，并不会影响代码的正常运行
import json
if __name__ == '__main__':
    # 确认目标的url
    url_ = "https://movie.douban.com/top250"

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

    dict_ = {}
    for i in range(len(title_list)):
        dict_[title_list[i]] = url_list[i]
    print(dict_)

    # 4.保存到本地
    file_obj = open('douban250_.json','w')

    # 少了一个s，就是直接跟json文件打交道
    json.dump(dict_,file_obj,ensure_ascii=False)


"""
作业：
做一个翻页案例，xpath提取豆瓣数据翻页
2天内写完，写完直接把代码以邮件的形式发给我的QQ邮箱，1919270709@qq.com
"""