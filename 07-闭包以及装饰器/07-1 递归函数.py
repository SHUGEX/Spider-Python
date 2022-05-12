# 累积和
# def funa(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     print(sum)
#
# funa(3)

# 递归函数
# def funb(n):
      # 第一种
#     if n == 1 :
#         return 1
#     return n + funb(n-1)
#
      # 第二种
#     # if n > 0:
#     #     return n + funb(n - 1)
#     # else:
#     #     return 0
# print(funb(3))


# 函数引用
# -5~256之间整数内存地址固定
# a = 1
# b = 1
# print(id(a),id(b))

def test():
    print('hello')

# test()
# 引用函数
te = test
# print(id(te))
# print(id(test))
# 通过引用调用函数
te()
