"""
selenium绕过js,抓取京东图书
"""
# 京东图书:https://list.jd.com/list.html?cat=1713,3258,3297
"""
分析：
1.数据是json类型还是html类型
    --html类型
    
2.通过xpath调试发现
    --(1) 取到的数据只有部分
    --(2) 鼠标往下拖动，有数据的加载(再次地发送了请求)

3.一页数据应该是有60本书
//div[@class="gl-i-wrap"]/div[@class="p-name"]/a[@target="_blank"]/em/text()

4.需要通过js的触发，滚动条的拖动，才能够加载出来全部的页面，获取到60本书的数据
"""



from selenium import webdriver
# 延迟模块
import time
# 解析html
from lxml import etree
# 页面加载等待的异常处理
from selenium.common.exceptions import TimeoutException

if __name__ == '__main__':
    # 创建浏览器对象
    chrome_obj = webdriver.Chrome()

    # 输入网址 >> 中国当代小说  https://list.jd.com/list.html?cat=1713,3258,3297
    chrome_obj.set_page_load_timeout(5)
    try:
        chrome_obj.get('https://list.jd.com/list.html?cat=1713,3258,3297')
    except TimeoutException:
        print('超时了.....')

    # 进行进度条的滚动
    for i in range(8):
        time.sleep(0.5)
        chrome_obj.execute_script(f'document.documentElement.scrollTop={(i+1)*1000}')  # 底部一般是一个较大的数值，比方说6000

    # 第二次发送了请求，页面已经有了60本书


    # 获取当前页面的html代码
    str_data = chrome_obj.page_source

    # 解析书名
    html_obj = etree.HTML(str_data)
    title_list = html_obj.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name"]/a[@target="_blank"]/em/text()')
    print(title_list)
    print(len(title_list))

    # 解析价格
    price_list = html_obj.xpath('//strong/i/text()')
    print(price_list)
    print(len(price_list))

    for i in range(len(title_list)):
        dict_ = {}
        dict_[title_list[i]] = price_list[i]
        print(dict_)

"""
关于进度条的滚动，不建议一次性滚动到底  8000 
第一次滚动到1000
第二次滚动到2000
第三次滚动到3000
第四次滚动到4000

没有做页面的等待
页面也没有渲染完毕，就马上去拖动滚动条，因此卡住


设置完了5秒
强行执行接下来的代码
"""