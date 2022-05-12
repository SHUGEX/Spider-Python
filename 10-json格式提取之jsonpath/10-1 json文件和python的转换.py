"""
json文件跟python的交换
"""
import json
# # python格式的数据  >> json文件
#
# # 构造一个字典
# dict_data = {
#     'name':'sisi',
#     'age':18
# }
#
# # 文件对象
# file_obj = open('json_01.json','w')
#
# # 少了一个s，就是直接跟json文件打交道
# json.dump(dict_data,file_obj,ensure_ascii=False)


# json文件 >>  python格式
# 1.文件对象
# file_obj = open('json_01.json','r')
#
#
# # json文件 >> python格式的数据
# python_data = json.load(file_obj)
#
# print(python_data,type(python_data))
#
# file_obj.close()
"""
注意: json.dumps()和json.dump()，json.loads()和json.load()的区别
有s的是直接和json数据打交道；没有s的是和json文件打交道
python数据 >> json数据 : json.dumps(python数据,ensure_ascii=False)
python数据 >> json文件 ：json.dump(python字典,json文件对象,ensure_ascii=False)

json数据  >> python数据：json.loads(json数据)
json文件  >> python数据：json.load(json文件对象)
"""



file_obj = open('douban_1.json','r',encoding="utf-8")


# json文件 >> python格式的数据
python_data = json.load(file_obj)

# print(python_data,type(python_data))
# python_data是一个列表

for i in python_data:
    # print(type(i))
    # print(i)
    print(i['title'],i['score'])

file_obj.close()