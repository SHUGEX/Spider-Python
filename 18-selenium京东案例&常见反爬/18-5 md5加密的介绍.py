"""
MD5加密的介绍

123   >  qweqwr
明文  >  密文

123456789 > abcmoq
"""
"""
md5加密的特点：
    --密文长度固定 
    --不能够反解 
"""

# 导包
import hashlib

# a = '123'         # 3
# b = '123456789'   # 9
#
# res_a = hashlib.md5(a.encode()).hexdigest()
# res_b = hashlib.md5(b.encode()).hexdigest()
# print(res_a)
# print(res_b)



"""
MD5在线工具   
缺点：只能解析一些比较简单的
"""
a = '雪锐123在唱歌'
res_a = hashlib.md5(a.encode()).hexdigest()
print(res_a)