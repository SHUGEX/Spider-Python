"""
演示retrying模块
"""
"""
如果由于瞬间的网络波动，导致请求不成功
0.01s
在这种情况下，多给几次发送请求的机会，避免开由于瞬间的网络波动导致的请求不成功
"""

"""
第三方模块 retrying 
pip install retrying -i https://pypi.doubanio.com/simple
"""

# from retrying import retry

# retry是一个三层函数的嵌套，并且返回了内部函数的引用  闭包
# 三层 >> 有参数的装饰器

import requests
from retrying import retry


class Baidu:
    def __init__(self):
        self.url_ = "xxxxx.com"
        self.num_ = 0

    @retry(stop_max_attempt_number=3)
    def send_request(self):
        self.num_ += 1
        print(self.num_)
        requests.get(self.url_)

    def run(self):
        try:
            self.send_request()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    bd_obj = Baidu()
    bd_obj.run()

"""
模拟瞬间的网络波动，只会进行一次请求
根据打印结果
1
2
3
就证明发送请求部分执行了三遍
"""