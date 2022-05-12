"""
介绍json格式数据
"""
"""
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，它使得人们很容易的进行阅读和编写。同时也方便了机器进行解析和生成。适用于进行数据交互的场景，比如网站前台与后台之间的数据交互。


后端提供了json格式的数据给前端(浏览器)，django python 

前端 json格式的数据
如果想用python控制，处理json格式的数据，格式的转化操作
转化成我们python能够处理的数据格式
字典
web端
"""


"""
python里面的字典 >> json (前端才能够进行数据的填充)
"""
# import json # 原生自带
#
# if __name__ == '__main__':
#     # python数据 > 字典
#     dict_data = {
#         "name":"思思",
#         "age":18
#     }
#     print(dict_data,type(dict_data))
#
#     # python > json  默认使用的是ascii编码 ensure_ascii=False 显示出中文
#     json_data = json.dumps(dict_data,ensure_ascii=False,indent=10) # indent=3 每一个键值对的缩进空格
#     print(json_data,type(json_data))   # json字符串 本质是一个字符串



"""
json > python 
"""
import json # 原生自带

if __name__ == '__main__':
    # python数据 > 字典
    dict_data = {
        "name":"思思",
        "age":18
    }

    # python > json  默认使用的是ascii编码 ensure_ascii=False 显示出中文
    json_data = json.dumps(dict_data,ensure_ascii=False) # indent=3 每一个键值对的缩进空格
    print(json_data,type(json_data))   # json字符串 本质是一个字符串


    # json > python 才能够去处理前端交互过来的json数据
    python_data = json.loads(json_data)
    print(python_data,type(python_data))