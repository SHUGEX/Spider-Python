import time
import pymongo
import requests
import jsonpath

class UseMongo:
    def __init__(self,db,colllection):
        # 1.建立连接
        self.client = pymongo.MongoClient()

        # 2.指定数据库
        self.db = self.client[db]

        # 3.指定集合
        self.col = self.db[colllection]

    def insert_data(self,data):
        self.col.insert_many(data)    # insert_many()参数必须要以列表的形式传入

    def find_data(self):
        res = self.col.find()
        for i in res:
            print(i)

if __name__ == '__main__':
    # 实例化 定义数据库参数
    dh = UseMongo('python2204','student')   # 如果没有数据库python2204也没有集合student,就会自动创建
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

        list_data = []    # 用于保存爬取到的每一条评论数据
        for i in range(len(name_list)):
            dict_ = {}
            dict_[name_list[i]] = comment_list[i]
            print(dict_)
            list_data.append(dict_)


        # 降低请求频率，避免被反爬
        time.sleep(1)
        dh.insert_data(list_data)
        dh.find_data()