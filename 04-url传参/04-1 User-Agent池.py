"""
演示User-Agent池  用户代理池
"""
"""
需要短时间内连续访问同一个网站很多次这样一个需求
headers_ = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
在服务端会有记录
同一个User-Agent 3s  上百次   非正常用户行为  以此来判断你是一个爬虫程序

解决办法：
使用User-Agent池
可以理解成是一个列表  很多的Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36
100次请求 
每一次请求，都从User-Agent池里面随机拿一个身份  张三  李四 王五
"""

# import requests
# # 简单演示如何使用
# import random
# # 1.使用列表，里面存放很多的User-Agent值
# user_agent_list = [
#     'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#     'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.51 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#     'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.52 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#     'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.53 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#     'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.54 (KHTML, like Gecko) Version/5.1 Safari/534.50',
# ]
#
# # 获取一个随机整数，作为列表的索引值
# num = random.randint(0,4)   # 前后都包，0和4都有可能取到
#
# # 打印获取到的索引
# print(num)
#
# # 打印随机选取的user-agent
# print(user_agent_list[num])
#
# if __name__ == '__main__':
#     url_ = "https://www.baidu.com/"
#
#     headers_ = {
#         'User-Agent':user_agent_list[num]
#     }
#
#     # 每次请求，都携带上随机的user-agent
#     response_ = requests.get(url_,headers=headers_)
#
#     # 打印百度服务器检测到的用户代理身份
#     print(response_.request.headers)





# 2.一个第三方库可以提供  fake-useragent     pip install fake-useragent  -i https://pypi.doubanio.com/simple
# 一般导入使用的是下划线，下载的时候是中橫线
from fake_useragent import FakeUserAgent
import requests
user_agent_demo = FakeUserAgent().random    # 这个random不需要导入

print(user_agent_demo)

if __name__ == '__main__':
    url_ = "https://www.baidu.com/"

    headers_ = {
        'User-Agent':user_agent_demo
    }

    # 每次请求，都携带上随机的user-agent
    response_ = requests.get(url_,headers=headers_)

    # 打印百度服务器检测到的用户代理身份
    print(response_.request.headers)


"""
终极方法：
ctrl点击FakeUserAgent进入源码>ctrl点击settings进入源码>第16行CACHE_SERVER这里有一个https，把s去掉 > 如果有弹窗，点击OK > 再把s去掉 > 多运行几遍 
"""