"""
加密方式 --base64
"""
"""
--密文长度不固定
--可以反解析  解密 
"""


import base64
# a = '123'
# b = '123456789'
# c = '456789'
# res_a = base64.b64encode(a.encode()).decode()
# res_b = base64.b64encode(b.encode()).decode()
# res_c = base64.b64encode(c.encode()).decode()
# print(res_a)
# print(res_b)
# print(res_c)

"""
反解析
"""
a = "MTIz"
b = "MTIzNDU2Nzg5"
c = "NDU2Nzg5"

res_a = base64.b64decode(a.encode()).decode()
res_b = base64.b64decode(b.encode()).decode()
res_c = base64.b64decode(c.encode()).decode()

print(res_a)
print(res_b)
print(res_c)