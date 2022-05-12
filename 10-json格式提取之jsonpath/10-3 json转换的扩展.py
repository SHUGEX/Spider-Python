



# import requests
# import jsonpath
# import json
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
#
#     headers_ = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#
#     # 2.发送网络请求，得到响应对象
#     response_ = requests.get(url_,headers=headers_)
#
#     # 首先利用text取到文本数据
#     json_data = response_.text # json格式的数据
#     # print(type(json_data))
#
#     py_data = json.loads(json_data)  # 转化成python格式的数据
#     # print(type(py_data))
#
#     res_ = jsonpath.jsonpath(py_data,'$..A[0].name')
#     print(res_)



"""
简化：如果响应对象的文本数据的格式为json
"""
import requests
import jsonpath
if __name__ == '__main__':
    # 1.确认目标的url
    url_ = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

    headers_ = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }

    # 2.发送网络请求，得到响应对象
    response_ = requests.get(url_,headers=headers_)

    # 直接得到python格式的数据，自动转换类型
    py_data = response_.json()   # 这是一个方法，不是import导入的json模块
    # print(type(data_))

    res_ = jsonpath.jsonpath(py_data,'$..A[0].name')
    print(res_)
