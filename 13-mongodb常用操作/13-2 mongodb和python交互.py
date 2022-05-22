
import pymongo

# 建立连接
client = pymongo.MongoClient()

# 指定数据库
db = client['sisi']

# 指定集合
col = db['s1']

# 查询

# a = col.find()    # find返回的是可迭代对象，需要用for遍历取值
# for i in a:
#     print(i)

# 查找一条文档，直接显示出来
# a1 = col.find_one()
# print(a1,type(a1))



# 添加一条文档  insert_one
# col.insert_one({'name':'安安','age':18})

# 修改一条文档 update_one
# col.update_one({'name':'安安'},{'$set':{'name':'靓仔'}})

# 删除一条文档
col.delete_one({'name':'靓仔'})

a = col.find()    # find返回的是可迭代对象，需要用for遍历取值
for i in a:
    print(i)