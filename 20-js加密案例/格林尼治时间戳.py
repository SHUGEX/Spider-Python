import time

# 格林尼治时间戳
# 1654088116494
# 1654087267101
# 1654085147758
# 1654087107.2550042
print(time.time())     # 默认以秒为单位的格林尼治时间戳

# 乘以1000得到以毫秒为单位的格林尼治时间戳
print(int(time.time()*1000))




# dfd4ab2478546b7c767639bcbeb6ce86  你好  16540881164949
# 47aa5235ed90be1602eb720fee9205de
import hashlib

a = "fanyideskweb" + '你好' + '16540881164949' + "Ygy_4c=r#e#4EX^NUGUc5"
res_ = hashlib.md5(a.encode()).hexdigest()
print(res_)