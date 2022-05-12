"""
单页贴吧案例
"""
"""
为什么看不到大部分的数据
核心数据被注释了，所以呈现不出来
也相当于一个反爬
"""


# from urllib.parse import unquote
# # %E7%BE%8E%E9%A3%9F
#
# print(unquote('%E7%BE%8E%E9%A3%9F'))


"""
单页贴吧数据
"""
# import requests
#
# if __name__ == '__main__':
#     data_ = input('请输入你想抓取的贴吧:')
#     # 1.确认目标的url
#     url_ = "https://tieba.baidu.com/f"
#
#
#     # 设置用户代理
#     headers_ = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#
#     params_ = {
#         "kw":data_
#     }
#
#     # 发送请求，得到响应对象
#     response_ = requests.get(url_,headers=headers_,params=params_)
#     str_data = response_.content.decode()
#
#     # 4.保存
#     with open(f'{data_}.html','w',encoding="utf-8") as f:
#         f.write(str_data)
#





"""
贴吧多页爬虫
1个url  >> 一个资源
多个url >> 多个资源

简单: >> url有规律可循

第1页的url:https://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&pn=0        0*50
第2页的url:https://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&pn=50       1*50
第3页的url:https://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&pn=100      2*50
第4页的url:https://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&pn=150      3*50

想法:使用for循环就可以使得url参数产生有规律地变化，实现翻页
"""
import requests

if __name__ == '__main__':
    data_ = input('请输入你要搜索的贴吧:')
    pages_ = int(input("请输入你要爬取的页数:"))

    for i in range(pages_):  # range(0,10) 0 1 2 3 4 5 6 7 8 9
        # 1.确认目标的url
        url_ = "https://tieba.baidu.com/f"


        # 设置用户代理
        headers_ = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }

        params_ = {
            "kw":data_,
            "pn":i*50
        }

        # 发送请求，得到响应对象
        response_ = requests.get(url_,headers=headers_,params=params_)
        str_data = response_.content.decode()

        # 4.保存
        with open(f'{data_}_第{i+1}页.html','w',encoding="utf-8") as f:
            f.write(str_data)


