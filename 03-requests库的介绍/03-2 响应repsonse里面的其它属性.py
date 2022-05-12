"""
演示响应response里面的其它属性
"""

"""
response.text 响应体 str类型
respones.content 响应体 bytes类型
response.status_code 响应状态码
response.request.headers 响应对应的请求头
response.headers 响应头
response.request.cookies 响应对应请求的cookie
response.cookies 响应的cookie（经过了set-cookie动作）
"""


import requests

if __name__ == '__main__':
    # 1.确认需要的数据的url,目标url,需要是一个字符串
    url_ = "https://www.baidu.com/"

    # 2.发送网络请求，获取响应对象
    response_ = requests.get(url_)

    # response.status_code 响应状态码,200(请求成功)  301(跳转) 404页面找不到  500服务器出现了错误
    # print(response_.status_code)

    # response.request.headers 响应对应的请求头(重点)
    # print(response_.request.headers)  # 响应对象里面还包含了我们的请求信息(已经被服务端解析过了一次的请求信息)

    # 代表百度的服务器已经知道了我们是一个python爬虫的身份，已经被识别到到了是一个爬虫程序
    # 'User-Agent': 'python-requests/2.24.0'(重点)

    # 正常的使用浏览器访问，用户代理(代理请求者的身份)
    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36


    # response.headers 响应头
    # print(response_.headers)

    # response.request._cookies 响应对应请求的cookie
    # print(response_.request._cookies)   # 这是一个CookieJar对象(了解)

    # response.cookies 响应的cookie（经过了set-cookie动作）
    print(response_.cookies)