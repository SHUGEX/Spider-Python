"""
jsonpath提取json数据
"""
"""
list_1 =[1,2,3,4,5,6]
"""


"""
.. 跨节点
D:\大海\2204期爬虫1班(改版)\代码\01
D.大海.2204期爬虫1班(改版).01
D..01
"""

dict_data = {"store": {
    "book": [
        {"category": "reference",
         "author": "吴承恩",
         "title": "西游记",
         "price": 8.95
         },
        {"category": "fiction",
         "author": "曹雪芹",
         "title": "红楼梦",
         "price": 12.99
         },
        {"category": "fiction",
         "author": "罗贯中",
         "title": "三国演义",
         "isbn": "0-553-21311-3",
         "price": 8.99
         },
        {"category": "fiction",
         "author": "施耐庵",
         "title": "水浒传",
         "isbn": "0-395-19395-8",
         "price": 22.99
         }
    ],
    "bicycle": {
        "color": "red",
        "price": 19.95
    }
}
}


# 假设是刚从网上下载下来的json格式的数据
# python数据  >> json数据
import json
import jsonpath
json_data = json.dumps(dict_data,ensure_ascii=False)
# print(json_data,type(json_data))

# $.store.book[*].author	store中的所有的book的作者
# python 无法直接操作json格式的数据，格式的转换 字典  列表

# 1.从网上拿到了json格式的数据之后，转换格式，转成python能够操作的格式
py_data = json.loads(json_data)
# print(type(py_data),py_data)
# 2.使用jsonpath进行解析，数据的提取
# res_ = jsonpath.jsonpath(py_data,'$.store.book[*].author')
# res_ = jsonpath.jsonpath(py_data,'$.store.book[1].author')
# res_ = jsonpath.jsonpath(py_data,'$..author')

# jsonpath取到的数据是一个列表，索引也是从0开始
# print(res_)


"""
$.store.*	store下的所有的元素
"""
# res_ = jsonpath.jsonpath(py_data,'$.store.*')
# print(res_)


# """
# $.store..price	store中的所有的内容的价格    跨节点取 要慎重
# """
# res_ = jsonpath.jsonpath(py_data,'$.store..price')
# print(res_)


# """
# $..book[2]	第三本书 索引从0开始
# """
# res_ = jsonpath.jsonpath(py_data,'$..book[2]')
# print(res_)


# """
# $..book[(@.length-1)] | $..book[-1:]	最后一本书   | 或的意思
# """
# # res_ = jsonpath.jsonpath(py_data,'$..book[(@.length-1)]')     # book[3]
# res_ = jsonpath.jsonpath(py_data,'$..book[-1:]')     # book[3]
# print(res_)


# """
# $..book[0,1] | $..book[:2]	前两本书
# """
# # res_ = jsonpath.jsonpath(py_data,'$..book[0,1]')    # 取索引
# res_ = jsonpath.jsonpath(py_data,'$..book[:2]')       # 切片 0 1 同样遵循包前不包后
# print(res_)


# """
# $..book[?(@.isbn)]	获取有isbn的所有数
# """
# res_ = jsonpath.jsonpath(py_data,'$..book[?(@.isbn)]')
# print(res_)


# """
# $..book[?(@.price>10)]	获取价格大于10的所有的书
# """
# res_ = jsonpath.jsonpath(py_data,'$..book[?(@.price>10)]')
# print(res_)


"""
$..*	获取所有的数据
"""
res_ = jsonpath.jsonpath(py_data,'$..*')
print(res_)

"""
$.store.book[*].author	store中的所有的book的作者
$..author	所有的作者
$.store.*	store下的所有的元素
$.store..price	store中的所有的内容的价格
$..book[2]	第三本书
$..book[(@.length-1)] | $..book[-1:]	最后一本书
$..book[0,1] | $..book[:2]	前两本书
$..book[?(@.isbn)]	获取有isbn的所有数
$..book[?(@.price<10)]	获取价格大于10的所有的书
$..*	获取所有的数据
"""