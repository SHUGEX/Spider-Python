
# 装饰器
# def check(fn):
#     def inner():
#         print('请先登录....')
#         fn()        # 4.调用test函数
#     return inner    # 1.返回的是inner引用


# 1> 使用装饰器来装饰函数
# def a():
#     print('发表评论....')

# 2.ch里面是inner的引用
# ch = check(a)
# ch()     # 3.调用inner函数

# 2.语法糖 @函数名  @check 等价于ch = check(a)
# @check
# def a():
#     print('发表评论....')
#
# a()








# 无参数的函数
# import time
# def b(func):
#     def inner():
#         print('----装饰器----')
#         func()
#     return inner
#
# @b
# def t1():
#     print('哈哈哈')
#
# t1()
# time.sleep(2)
# t1()

# 有参数的函数
# def b(func):
#     def inner(c,d):
#         print(c,d)
#         func(c,d)
#     return inner
#
# @b
# def t1(c,d):
#     print('结果是:',c+d)
#
# t1(1,2)


# 多个装饰器
def c1(fn):
    def inner():
        return '哈' + fn() + '哈'
    return inner

def c2(fn):
    def inner():
        return '嘻' + fn() + '嘻'
    return inner

@c1
def t1():
    return 'hello'
@c2
def t2():
    return 'python'

@c1
@c2

def t3():
    return 'world'
print(t3())    # 离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰






# print(t1())
# print(t2())