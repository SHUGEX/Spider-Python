"""
演示windows上的数据写入本地mysql数据库
"""
import time

"""
1.进入mysql: mysql -uroot -p
2.查看有多少个数据库： show databases;
3.创建一个新的数据库：create database spider2201 charset=utf8mb4;  # 爱心，表情等特殊符号
4.使用该数据库：use spider2201;
5.创建数据表：create table 表名(列及类型); 
如：
create table txkt001( 
id int auto_increment primary key, 
nick_name varchar(10) not null,
comments varchar(4000) not null
);
6.查看数据表中的内容(全部字段)：select * from txkt001;
7.查看数据表的结构：desc txkt001;

"""

"""
txkt001
id(序号)          nick_name            comment
1                  叶子                 六星我最美
2                  思思                 我不同意
3                  雪锐                 我才是六星班主任颜值的天花板
4                  长清                 我是六星最靓的仔                 男    不行

char(10):不可变的  2个字符会增长成10个字符
varchar:可变       2个字符就是2个字符
"""


"""
mysql数据库是一个单独的东西，它不是依靠于python
python控制mysql数据库，连接 pymysql 第三方库
pip install pymysql -i https://pypi.doubanio.com/simple
"""
"""
单页
"""


# import requests
# import jsonpath
# # 1.导入连接mysql数据库的第三方库 pymysql
# from pymysql import *
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=383855&count=10&page=0&filter_rating=0&bkn=&r=0.4714014617273816"
#
#     # 用户代理的设置，添加跳转referer
#     headers_ = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
#         "Referer":"https://ke.qq.com/course/383855?tuin=9f751c76"   # 教室主页(客厅)
#     }
#
#     # 2.发送请求得到响应数据
#     response_ = requests.get(url_,headers=headers_)
#
#     py_data = response_.json()   # 直接转化成python类型的数据
#     # json_data = response_.text
#
#     # print(json_data)
#
#     # 数据的提取，jsonpath,解析python格式类型的数据
#     name_list = jsonpath.jsonpath(py_data,"$..nick_name")   # 列表
#     # print(name_list)
#
#     comment_list = jsonpath.jsonpath(py_data, "$..first_comment")  # 列表
#     # print(comment_list)
#
#
#     # 循环之外
#     # 二.与mysql数据库进行连接,会创建一个连接对象
#     con_obj = connect(host="127.0.0.1",user="root",password="mysql",database="spider2201",port=3306,charset='utf8mb4')
#     print('连接成功....')
#
#     # 连接数据库成功之后，想要往数据库里面写入数据
#     # 三.创建一个游标对象
#     mysql_ = con_obj.cursor()
#
#     # 因为数据一条条添加，所以放在循环内去做
#     for i in range(len(name_list)):
#         # 四.写sql语句，并且使用python代码让sql语句执行
#         mysql_.execute('insert into txkt001(id,nick_name,comments) values(0,("%s"),("%s"))' % (name_list[i], comment_list[i]))
#
#         # 五.提交才能生效
#         con_obj.commit()
#
#         print(f'第{i+1}条数据写入完毕.....')
#
#     # 六.关闭与数据表的连接
#     mysql_.close()
#
#     # 七.数据全部写完，关闭跟mysql数据库的连接
#     con_obj.close()

"""
(重点！！！)
数据入库7步骤

1.导入连接mysql数据库的第三方库
from pymysql import *

2.创建与数据库的连接：
连接对象 = connect(host='IP',port=3306,user='用户名',password='密码',database='数据库名',charset='编码方式')

3.创建一个游标对象
游标对象 =连接对象.cursor()

4.通过游标对象以及execute()执行sql语句
游标对象.execute('sql语句')

5.提交才能生效
连接对象.commit()

6.关闭与数据表的连接
游标对象.close()

7.关闭与数据库的连接
连接对象.close()
"""






"""
心路历程：
    --1.本机IP地址可用127.0.0.1表示
    --2.mysql的端口号是3306
    --3.id字段是自动增长，写0即可
"""









# import requests
# import jsonpath
# # 1.导入连接mysql数据库的第三方库 pymysql
# from pymysql import *
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=383855&count=10&page=0&filter_rating=0&bkn=&r=0.4714014617273816"
#
#     # 用户代理的设置，添加跳转referer
#     headers_ = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
#         "Referer":"https://ke.qq.com/course/383855?tuin=9f751c76"   # 教室主页(客厅)
#     }
#
#     # 2.发送请求得到响应数据
#     response_ = requests.get(url_,headers=headers_)
#
#     py_data = response_.json()   # 直接转化成python类型的数据
#     # json_data = response_.text
#
#     # print(json_data)
#
#     # 数据的提取，jsonpath,解析python格式类型的数据
#     name_list = jsonpath.jsonpath(py_data,"$..nick_name")   # 列表
#     # print(name_list)
#
#     comment_list = jsonpath.jsonpath(py_data, "$..first_comment")  # 列表
#     # print(comment_list)
#
#
#     # 循环之外
#     # 二.与mysql数据库进行连接,会创建一个连接对象
#     con_obj = connect(host="127.0.0.1",user="root",password="mysql",database="spider2201",port=3306,charset='utf8mb4')
#     print('连接成功....')
#
#     # 连接数据库成功之后，想要往数据库里面写入数据
#     # 三.创建一个游标对象
#     mysql_ = con_obj.cursor()
#
#     # 因为数据一条条添加，所以放在循环内去做
#     for i in range(len(name_list)):
#         # 四.写sql语句，并且使用python代码让sql语句执行
#         mysql_.execute('insert into txkt001(id,nick_name,comments) values(0,("%s"),("%s"))' % (name_list[i], comment_list[i]))
#         # 五.提交才能生效
#         con_obj.commit()
#         print(f'第{i+1}条数据写入完毕.....')
#
#
#     # 六.关闭与数据表的连接
#     mysql_.close()
#
#     # 七.数据全部写完，关闭跟mysql数据库的连接
#     con_obj.close()
#


"""
关于commit提交
10条数据,可以很迅速地执行完，由commit统一提交 
10000条数据 
"""

"""
翻页
"""
import requests
import jsonpath
# 1.导入连接mysql数据库的第三方库 pymysql
from pymysql import *
if __name__ == '__main__':
    num_ = int(input('请输入想要抓取的页数：'))

    # 二.与mysql数据库进行连接,会创建一个连接对象
    con_obj = connect(host="127.0.0.1", user="root", password="mysql", database="spider2201", port=3306,
                      charset='utf8mb4')
    print('连接成功....')

    # 连接数据库成功之后，想要往数据库里面写入数据
    # 三.创建一个游标对象
    mysql_ = con_obj.cursor()
    for i in range(num_):
        # 1.确认目标的url
        url_ = f"https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=383855&count=10&page={i}&filter_rating=0&bkn=&r=0.4714014617273816"

        # 用户代理的设置，添加跳转referer
        headers_ = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
            "Referer":"https://ke.qq.com/course/383855?tuin=9f751c76"   # 教室主页(客厅)
        }

        # 2.发送请求得到响应数据
        response_ = requests.get(url_,headers=headers_)

        py_data = response_.json()   # 直接转化成python类型的数据
        # json_data = response_.text

        # print(json_data)

        # 数据的提取，jsonpath,解析python格式类型的数据
        name_list = jsonpath.jsonpath(py_data,"$..nick_name")   # 列表
        # print(name_list)

        comment_list = jsonpath.jsonpath(py_data, "$..first_comment")  # 列表
        # print(comment_list)


        # 循环之外


        # 因为数据一条条添加，所以放在循环内去做
        for i in range(len(name_list)):
            # 四.写sql语句，并且使用python代码让sql语句执行
            mysql_.execute('insert into txkt001(id,nick_name,comments) values(0,("%s"),("%s"))' % (name_list[i], comment_list[i]))

            # 五.提交才能生效
            con_obj.commit()

            # print(f'第{i+1}条数据写入完毕.....')
        # 翻页，手动延迟，降低请求频率，避免被反爬
        time.sleep(0.5)

    # 六.关闭与数据表的连接
    mysql_.close()

    # 七.数据全部写完，关闭跟mysql数据库的连接
    con_obj.close()