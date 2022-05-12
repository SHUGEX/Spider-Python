"""
演示用户代理的使用 User-Agent(重点)
"""

# 使用爬虫去访问百度首页，其实已经是被检测到了是爬虫的身份
"""
百度首页已经知道了我们是爬虫程序的情况下，为啥还要给我们返回了数据....
1.拒绝我们的访问
2.数据不重要的话
3.返回给你假数据
"""


# import requests
#
# if __name__ == '__main__':
#     # 1.确认需要的数据的url,目标url,需要是一个字符串
#     url_ = "https://www.baidu.com/"
#
#     # 2.发送网络请求，获取响应对象
#     response_ = requests.get(url_)
#
#     # 2.1 取到里面的数据
#     bytes_data = response_.content   # bytes_data存入的就是响应的字节数据
#
#     # 2.2 解码 把字节数据解码成字符串类型的数据
#     str_data = bytes_data.decode()
#
#     with open('baidu_03.html','w',encoding="utf-8") as f:
#         f.write(str_data)
"""
经过对比发现数据少了

因为我们已经被识别成了一个爬虫程序

尽可能地模拟正常的用户，模拟客户端(浏览器)去发送请求
'User-Agent': 'python-requests/2.24.0'(重点)

解决办法，隐藏爬虫身份 'python-requests/2.24.0' 这个部分给隐藏

正常用户的脸(身份):   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36

"""


"""
User-Agent 用户代理的使用
"""
import requests

if __name__ == '__main__':
    # 1.确认需要的数据的url,目标url,需要是一个字符串
    url_ = "https://www.baidu.com/"

    # 2.1 实现User-Agent用户代理，隐藏爬虫身份，使用正常浏览器的身份
    # 键名:User-Agent    键值:正常浏览器的数据
    headers_ = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

    # 2.发送网络请求，获取响应对象,把用户代理User-Agent带上
    response_ = requests.get(url_,headers=headers_)

    # 2.1 取到里面的数据
    bytes_data = response_.content   # bytes_data存入的就是响应的字节数据

    # 2.2 解码 把字节数据解码成字符串类型的数据
    str_data = bytes_data.decode()

    with open('baidu_04.html','w',encoding="utf-8") as f:
        f.write(str_data)

"""
User-Agent 
1.对于服务端来说，反爬点
2.对于我们来说，它是模拟正常用户的一个部分

User-Agent用户代理只是其中一个

"""