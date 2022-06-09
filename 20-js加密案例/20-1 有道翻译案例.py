"""
演示有道翻译爬虫案例
"""
"""
目的：
用爬虫去请求得到翻译结果
"""
# 时间戳在线解析:https://tool.lu/timestamp/         有道翻译:https://fanyi.youdao.com/
"""
分析:
--1.找到数据包，请求POST,response的类型为json
    --构造表单数据
        i: 你好
        from: AUTO
        to: AUTO
        smartresult: dict
        client: fanyideskweb
        salt: 16540851477580
        sign: 22c0905db8b3e4df57bee4e54a1c8098
        lts: 1654085147758
        bv: 1744f6d1b31aab2b4895998c6078a934
        doctype: json
        version: 2.1
        keyfrom: fanyi.web
        action: FY_BY_CLICKBUTTION
--2.修改了要被翻译的数据之后，其它的表单数据是不是也会跟着产生变化
--3.form表单的不同之处
    --i     >> 要被翻译的文字
    --lts   >> 猜测，是格林尼治时间   证实 >> 以毫秒为单位的格林尼治时间  int(time.time()*1000)
    --salt  >> 根据lts进行的加盐操作  在末尾加上一个数字
    --sign  >> 未知  加密得来的  代码的运行 js代码   js文件当中
    
    
参数解密思路:
lts > ts > r > 以毫秒为单位的格林尼治时间戳 > int(time.time()*1000)
salt > i > r + 一个10以内的随机数字 > int(time.time()*1000) + random.randint(0,9)
sign > md5加密 > 参数为："fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5"
                        "fanyideskweb" + 要被翻译的内容 + salt + "Ygy_4c=r#e#4EX^NUGUc5"
"""

"""
i: 你好                                                   ⭐ i: 你好 
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16540851477580                                        ⭐ salt: 16540851477580  
sign: 22c0905db8b3e4df57bee4e54a1c8098                      ⭐ sign: 22c0905db8b3e4df57bee4e54a1c8098 
lts: 1654085147758                                           ⭐ lts: 1654085147758 
bv: 1744f6d1b31aab2b4895998c6078a934                         >> 以UA为参数进行md5加密之后的密文
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION

i: 阳光                                                   ⭐ i: 阳光  
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16540861776247                                         ⭐ salt: 16540861776247  
sign: 0d09f0fab511770790ef11d32c53ec15                        ⭐ sign: 0d09f0fab511770790ef11d32c53ec15
lts: 1654086177624                                            ⭐ lts: 1654086177624 
bv: 1744f6d1b31aab2b4895998c6078a934
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
"""


# import requests
# import jsonpath
# if __name__ == '__main__':
#     # 1.确认url
#     url_ = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#
#     # 请求头
#     headers_ = {
#         "Cookie": "OUTFOX_SEARCH_USER_ID=265786532@10.169.0.81; OUTFOX_SEARCH_USER_ID_NCOO=879005324.6578022; _ntes_nnid=6d3c8f32846ae1ebc9845de680fca423,1628772129772; ___rl__test__cookies=1654085147757",
#         "Referer": "https://fanyi.youdao.com/",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
#     }
#
#     # 构造form表单
#     form_data = {
#         "i": "阳光",
#         "from": "AUTO",
#         "to": "AUTO",
#         "smartresult": "dict",
#         "client": "fanyideskweb",
#         "salt": "16540851477580",
#         "sign": "22c0905db8b3e4df57bee4e54a1c8098",
#         "lts": "1654085147758",
#         "bv": "1744f6d1b31aab2b4895998c6078a934",
#         "doctype": "json",
#         "version": "2.1",
#         "keyfrom": "fanyi.web",
#         "action": "FY_BY_CLICKBUTTION"
#
#     }
#
#     # 发送请求，得到响应
#     response_ = requests.post(url_,headers=headers_,data=form_data)
#     py_data = response_.json()
#
#     # 解析数据 jsonpath  得到的结果为列表
#     # res_ = jsonpath.jsonpath(py_data,'$..tgt')[0]
#
#     # 输出打印
#     # print(f'翻译结果是:{res_}')
#     print(py_data)
import requests
import jsonpath
import time
import random
import hashlib
if __name__ == '__main__':
    while True:
        data_ = input('请输入你想要翻译的东西:')
        # 1.确认url
        url_ = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

        # 请求头
        headers_ = {
            "Cookie": "OUTFOX_SEARCH_USER_ID=265786532@10.169.0.81; OUTFOX_SEARCH_USER_ID_NCOO=879005324.6578022; _ntes_nnid=6d3c8f32846ae1ebc9845de680fca423,1628772129772; ___rl__test__cookies=1654085147757",
            "Referer": "https://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
        }

        # lts:以毫秒为单位的时间戳(格林尼治时间)
        time_ = str(int(time.time()*1000))

        # salt:lts随机加盐
        salt_time = time_ + str(random.randint(0,9))

        # sign值的生成
        a = "fanyideskweb" + data_ + salt_time + "Ygy_4c=r#e#4EX^NUGUc5"
        sign_ = hashlib.md5(a.encode()).hexdigest()

        # 构造form表单
        form_data = {
            "i": data_,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt_time,
            "sign": sign_,
            "lts": time_,
            "bv": "1744f6d1b31aab2b4895998c6078a934",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION"

        }

        try:
            # 发送请求，得到响应
            response_ = requests.post(url_,headers=headers_,data=form_data)
            py_data = response_.json()

            # 解析数据 jsonpath  得到的结果为列表
            res_ = jsonpath.jsonpath(py_data,'$..tgt')[0]

            # 输出打印
            print(f'翻译结果是:{res_}')
            # print(py_data)

            # 延迟
            time.sleep(1)
        except:
            print('输入有误，请重新输入.....')
            continue