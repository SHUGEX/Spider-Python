"""
字符编码问题
"""

# 为什么会有字符编码问题
"""
python php java c c++ 

二进制  >> 计算机 


每一种文字都有自己的字符集


网络数据的传递  >> 字节 
"""


"""
数据是不是从服务器来
首先，服务器就要把python类型的数据，转化成字节类型，才能放到网上传输
"""
# python数据类型  >> bytes类型
# encode
s = '思思'
print(type(s))
#str编码变为bytes类型
bytes_data = s.encode()
print(type(bytes_data),bytes_data)  # 编码  字节类型

# 解码 把看不懂的解码成看得懂的
# 从网上拿数据 bytes >> python的数据类型(string)
# decode
str_data = bytes_data.decode()
print(type(str_data),str_data)



# encode() decode()   需要格式一样 格式对应
# 编码格式是什么，那么解码格式是什么，才能够成功的解码
# encode() decode() 默认格式 utf-8
# 假如此时的数据是从网上拿到的，那么就要遵循它的编码格式去进行解码
# 一般都是utf-8