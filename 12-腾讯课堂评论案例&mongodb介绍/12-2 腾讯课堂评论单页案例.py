"""
演示腾讯课堂评论单页抓取，评论页面：https://ke.qq.com/course/380991/12573838881968191?tuin=7265bf35
"""
"""
评论页面属于通过鼠标单击触发的请求 属于异步加载 
XHR里面找到了数据包
1个数据包 1个url的response 10条评论， json类型
"""

import requests
import jsonpath
if __name__ == '__main__':
    # 1.确认目标的url
    url_ = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=380991&count=10&page=0&filter_rating=0&bkn=953999235&r=0.4877247373921103"

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





"""
{"msg":"refer错误","type":1,"retcode":100101}  >> 没有成功地抓取到数据
分析：referer错误 
新的反爬点 >> refer跳转
1.User-Agent
2.Cookie
3.referer 跳转

添加跳转信息：
部分特殊url的请求，会检查你是从哪一个url跳转过去的
检查点：需要从主页进行跳转，否则拒绝请求

客厅              >         卧室      正常的行为，就不会被反爬
腾讯课堂的主页     >        评论页面

窗户              >         卧室    非正常行为  小偷  抓起来
"""