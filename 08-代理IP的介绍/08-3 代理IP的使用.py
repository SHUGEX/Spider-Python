"""
演示代理IP的使用
"""
"""
使用的是真实的IP
"""



# import requests
#
# if __name__ == '__main__':
#     url_ = 'https://www.baidu.com'
#
#     headers_ = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#
#     response_ = requests.get(url_,headers=headers_)
#
#     print(response_.text)

"""
使用代理IP
"""
# import requests
#
# if __name__ == '__main__':
#     url_ = 'https://www.baidu.com'
#
#     headers_ = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#
#
#     # 构造代理IP字典
#     # proxies_字典中的键名(协议头)-->需要跟请求的url协议头保持一致，键值-->协议://IP:端口号
#     proxies_ = {"https":"http://1.1.1.1:8888"}  #  假的代理IP，无法使用的代理IP
#
#     # 使用代理IP
#     response_ = requests.get(url_,headers=headers_,proxies=proxies_)
#
#     print(response_.text)


"""
花钱购买的代理IP,也并不是百分之百全部能够用的
1000个代理IP,800能够用，200不能够使用
"""


"""
requests库的升级：
requests库升级前：无法使用的代理IP，会直接报错
requests库升级后：如果代理IP无法使用，它就会使用你的真实IP
"""



"""
坏处就是：无法过滤掉不能够使用的代理IP
1000个 >> 800 
"""


"""
如何处理：https://tool.lu/ip/

"""

# import requests
#
# from lxml import etree
#
# if __name__ == '__main__':
#     # 特殊测IP的url
#     url_ = "https://tool.lu/ip/"
#
#     # 用户代理 cookie
#     headers_ = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#         }
#
#     response_ = requests.get(url_,headers=headers_)
#     str_data = response_.content.decode()
#     # print(str_data)
#
#     # 目前不用了解，只是配合案例
#     html_obj = etree.HTML(str_data)
#     data_ = html_obj.xpath('//form[@id="main_form"]/p[1]/text()')[0]
#     print(data_)









# import requests
#
# from lxml import etree
#
# if __name__ == '__main__':
#     # 特殊测IP的url
#     url_ = "https://tool.lu/ip/"
#
#     # 用户代理 cookie
#     headers_ = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#         }
#
#     proxies_ = {"https": "http://220.179.210.174:4231"}  # 真的代理IP
#     #
#     #     # 使用代理IP
#     response_ = requests.get(url_,headers=headers_,proxies=proxies_)
#     # response_ = requests.get(url_,headers=headers_)
#     str_data = response_.content.decode()
#     # print(str_data)
#
#     # 目前不用了解，只是配合案例 提取数据 以后再了解，看不懂也没关系
#     html_obj = etree.HTML(str_data)
#     data_ = html_obj.xpath('//form[@id="main_form"]/p[1]/text()')[0]
#     print(data_)


import requests

from lxml import etree

if __name__ == '__main__':
    # 特殊测IP的url
    url_ = "https://tool.lu/ip/"

    # 用户代理 cookie
    headers_ = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }

    proxies_ = {"https": "http://1.1.1.1:8888"}  # 假的代理IP，无法使用的代理IP
    #
    #     # 使用代理IP
    response_ = requests.get(url_,headers=headers_,proxies=proxies_)
    # response_ = requests.get(url_,headers=headers_)
    str_data = response_.content.decode()
    # print(str_data)

    # 目前不用了解，只是配合案例
    html_obj = etree.HTML(str_data)
    data_ = html_obj.xpath('//form[@id="main_form"]/p[1]/text()')[0]
    print(data_)

"""
一个代理IP池  1000个代理IP 
使用循环
每一个代理IP
如果报错，就把其移除出代理IP池
"""