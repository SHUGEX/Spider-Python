# list_ = ['a','b','c']
#
# # for i in list_:
# #     print(i)
#
# for i in enumerate(list_):  # 以元组方式获得，索引以及对应的值
#     print(i[1])


a = ['a','b','c']
b = [1,2,3]

c = dict(zip(a,b))
print(c)