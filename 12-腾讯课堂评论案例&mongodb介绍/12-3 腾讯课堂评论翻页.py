"""
第一页:https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page=0&filter_rating=0&bkn=953999235&r=0.5644413795691736
第二页:https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page=1&filter_rating=0&bkn=953999235&r=0.07259275074126625
第三页:https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page=2&filter_rating=0&bkn=953999235&r=0.6201517422282963

经过分析：控制翻页的参数是page,并且page的值是以1进行递增的数据
"""
import time

import requests
import jsonpath
if __name__ == '__main__':
    for i in range(2):
        # 1.确认目标的url
        url_ = f"https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page={i}&filter_rating=0&bkn=953999235&r=0.4877247373921103"

        # 用户代理的设置，添加跳转referer
        headers_ = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
            "Referer":"https://ke.qq.com/course/380991/12573838881968191?tuin=7265bf35"   # 教室的主页(客厅)
        }


        # 2.发送请求得到响应数据
        response_ = requests.get(url_,headers=headers_)
        # json_data = response_.text
        py_data = response_.json()     # 直接转化成python类型的数据

        # print(json_data)
        # 3.数据的提取  jsonpath只能解析python格式类型的数据
        name_list = jsonpath.jsonpath(py_data,"$..nick_name")    # 列表
        # print(name_list)

        comment_list = jsonpath.jsonpath(py_data, "$..first_comment")  # 列表
        # print(comment_list)


        for i in range(len(name_list)):
            dict_ = {}
            dict_[name_list[i]] = comment_list[i]
            print(dict_)

        # 降低请求频率，避免被反爬
        time.sleep(1)