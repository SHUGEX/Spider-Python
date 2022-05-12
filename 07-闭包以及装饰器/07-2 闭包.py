
# 1.函数嵌套
# 2.内部函数使用外部函数的变量
# 3.外部函数返回内部函数

# def outer(m):
#     n = 10
#     def inner():
#         print(m+n)
#     # 外函数的返回值是内函数inner的引用
#     return inner
#
# # outer(2)()
# ot = outer(2)
#
# # 相当于执行inner函数
# ot()

# def test(num):
#     print('test函数中的值:',num)
#
#     def test_in(num_in):
#         print('test_in函数中的值:',num_in)
#         return num + num_in
#
#     return test_in
#
# te = test(10)
# print(te(100))
#
#
# print(te(200))

# def test1(a,b):
#     def test2(c):
#         return a*c + b
#     return test2
#
# t1 = test1(1,2)
# print(t1(3))



"""
修改闭包内使用的外部变量
"""

# 定义一个外部函数
def outer(a):
    # 定义一个内部函数
    def inner(b):
        nonlocal a # 告诉解释器，此处使用的是外部变量a
        # 修改外部变量a
        a = 20
        # 内函数使用了外部函数的变量a
        result = a + b
        print('结果是:',result)

    print(a)
    inner(6)
    print(a)

    # 外部函数返回内部函数inner的引用
    return inner

a = 2
b = 4
c = outer(a)
c(b)
