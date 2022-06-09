"""
加密操作之salt  加盐操作
"""

"""
明文  > 密文 
原材料  > 一道菜   加盐 
"""

"""
a   盐     加盐操作
123a   

456a 


789a
"""




import hashlib
a = '123'   #  密码 qwe  123a  > qwer
res_a = hashlib.md5(a.encode()).hexdigest()
print(res_a)