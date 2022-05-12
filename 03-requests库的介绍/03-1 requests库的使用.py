"""
演示requests库的使用
"""

"""
第三方模块  pip install requests -i https://pypi.doubanio.com/simple

爬虫：模拟客户端，发送网络请求，获取响应

在python当中 我们就使用第三方库requests去发送网络请求
"""

# 导入发送网络请求的requests库
# import requests
# # 介绍程序入口的文章：https://www.cnblogs.com/liruilong/p/12867590.html
# # 程序入口(可写可不写,忘记了作用的,可以回顾基本班的内容(模块和包的部分))
# if __name__ == '__main__':
#     # 1.确认目标的url，注意点，url从network里面寻找，因为网页是由network里面所有数据包构成的
#     url_ = "https://www.baidu.com/"   # 以字符串的方式进行呈现
#
#     # 2.发送网络请求，得到响应对象
#     response_ = requests.get(url_)   # 目标的url,利用requests库发送网络请求，最终得到一个响应对象response
#     print(response_)                 # 对象的形式
#     # 3.解析数据
#     # 仅仅拿到响应对象没有用，我们要的是里面数据
#     # print(response_.text)    # 得到该url对应的响应代码(数据)
#     # print(type(response_.text))   # 响应response的text属性 得到的是string字符串类型的数据
#
#     print(response_.content)   # 得到该url对应的响应代码(数据)
#     print(type(response_.content))  # 响应response的content属性 得到的是bytes字节类型的数据
#     # 4.保存









# import requests
# # 介绍程序入口的文章：https://www.cnblogs.com/liruilong/p/12867590.html
# # 程序入口(可写可不写,忘记了作用的,可以回顾基本班的内容(模块和包的部分))
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "https://www.baidu.com/"
#
#     # 2.利用requests库发送网络请求
#     response_ = requests.get(url_)
#     print(response_.encoding)    # 打印出text自动检测到的编解码格式
#     # 4.保存 由于text得到的str类型，因此用w写入
#     # with open('baidu_01.html','w',encoding="utf-8") as f:
#     #     f.write(response_.text)
#
#     with open('baidu_02.html','wb') as f:  # 注意点：wb二进制方式写入的话，是不需要加上encoding="utf-8"这个参数
#         f.write(response_.content)






# 以后写入文件，但凡是碰到UnicodeEncodeError
# 保存的数据，出现了乱码

"""
出现问题的原因：
从网络上拿下来的数据，都是字节类型的
我们使用text直接拿到的是字符串类型，没有进行解码操作
使用text会自动进行解码操作
编解码格式的问题，text会自动识别编解码格式，然后进行解码，不一开准确
由于text自作多情 检测错了编解码的格式，导致我们拿到的就是乱码数据

解决办法....直接使用content得到字节类型的数据
"""


import requests
# 介绍程序入口的文章：https://www.cnblogs.com/liruilong/p/12867590.html
# 程序入口(可写可不写,忘记了作用的,可以回顾基本班的内容(模块和包的部分))
if __name__ == '__main__':
    # 1.确认目标的url
    url_ = "https://www.baidu.com/"

    # 2.利用requests库发送网络请求
    response_ = requests.get(url_)
    print(response_.encoding)    # 打印出text自动检测到的编解码格式
    bytes_data = response_.content   # 得到字节类型的数据

    # 拿到了字节类型的数据，直接进行解码，默认使用的是utf-8的格式
    str_data = bytes_data.decode('utf-8')  # decode解码 字节 > str字符串类型
    print(type(str_data))
    print(str_data)
    # print(response_.text)
    # data_ = response_.text        # ISO-8859-1
    # # print(type(data_))
    #
    # bytes_data = data_.encode('ISO-8859-1 ')   # 使用它检测到的格式变成字节类型
    #
    # # 拿到了字节类型的数据，使用utf-8进行解码，是不是就成了我们看得懂的字符串
    # str_data = bytes_data.decode('utf-8')
    # print(str_data)
    # print(type(str_data))
    # 4.保存 由于text得到的str类型，因此用w写入
    # with open('baidu_01.html','w',encoding="utf-8") as f:
    #     f.write(response_.text)

    # with open('baidu_02.html','wb') as f:  # 注意点：wb二进制方式写入的话，是不需要加上encoding="utf-8"这个参数
    #     f.write(response_.content)


# 想要在pycharm终端中打开某个文件，就必须先cd进入到该文件所在的目录才行，必须要dir能够看到该文件
# pycharm直接打开的本地html文件，自动渲染一下，会自动请求某些需要的部分(图片的请求)
# 使用终端start打开的话，是什么就打开什么，没有的就没有














"""
目的：是使用python代码去完成一个爬虫
爬虫：就是模拟客户端去发送网络请求，得到响应数据

目标数据：百度首页的response代码(数据)  html格式的数据
目标url: https://www.baidu.com/
"""

# 导入一个发送网络请求的第三方库
import requests

if __name__ == '__main__':
    # 1.确认需要的数据的url,目标url,需要是一个字符串
    url_ = "https://www.baidu.com/"

    # 2.发送网络请求，获取响应对象
    response_ = requests.get(url_)

    # 2.1 取到里面的数据
    bytes_data = response_.content   # bytes_data存入的就是响应的字节数据

    # 2.2 解码 把字节数据解码成字符串类型的数据
    str_data = bytes_data.decode()

    print(str_data)

    # 解析，提取部分数据
