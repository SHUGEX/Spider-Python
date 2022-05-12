"""
面向对象方式完成翻页贴吧案例
"""

import requests

class Tieba:
    # 初始化init方法 >> 是不是只要创建对象，那么该方法就会执行
    def __init__(self):
        self.url_ = "https://tieba.baidu.com/f"
        self.headers_ = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }

    # 发送请求，得到响应数据
    def send_request(self,params_):
        response_ = requests.get(self.url_,headers=self.headers_,params=params_)
        str_data = response_.content.decode()
        return str_data

    # 解析数据

    # 保存数据
    #                  页数   保存的内容  标题
    def save_data(self,page,str_data,data_): # 保存就需要接收数据
        with open(f'{data_}_第{page+1}页.html','w',encoding="utf-8") as f:
            f.write(str_data)

    # 调度方法(用来调用其它的方法组合在一起使用)
    def run(self):
        data_ = input('请输入你要搜索的贴吧:')
        pages_ = int(input("请输入你要爬取的页数:"))

        for page in range(pages_):
            params_ = {
                "kw": data_,
                "pn": page* 50
            }

            # 调用send_request()方法
            str_data = self.send_request(params_)

            # 保存数据
            self.save_data(page,str_data,data_)

if __name__ == '__main__':
    # 创建对象
    tieba_ = Tieba()
    tieba_.run()

