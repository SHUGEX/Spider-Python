"""
演示自动化测试工具 selenium元素定位方法
"""

# 导包selenium
# import time
#
# from selenium import webdriver
#
# if __name__ == '__main__':
#     # 1.创建一个浏览器对象
#     chrome_obj = webdriver.Chrome()   # C大写，加括号
#
#     # 2.往网页地址栏输入网址，发送请求
#     chrome_obj.get('https://www.baidu.com/')
#     # 手动延迟，确保百度首页加载完毕，不会出现定位不到节点元素的情况
#     time.sleep(1)
#
#     # 3.1 在百度首页搜索框输入关键字
#     # (1) 定位到搜索输入框 拥有id属性的节点，定位起来就很简单  找到节点id的值  kw keyword
#     input_obj = chrome_obj.find_element_by_id('kw')   # 写完检查一下element有没有s
#     # (2) 定位到了搜索框，往里面输入想要进行搜索的关键字
#     input_obj.send_keys('京东')
#
#     # 3.2 利用python代码点击百度一下，进行搜索
#     # (1) 定位到(找到)'百度一下'那个按钮
#     click_obj = chrome_obj.find_element_by_id('su')   # 定位input
#     # (2) 利用python代码点击
#     click_obj.click()   # 点击
#
#     # 此时此刻，浏览器对象的页面 处于京东的搜索页面
#     str_data = chrome_obj.page_source
#
#     # with open('jingdong01.html','w',encoding="utf-8") as f:
#     #     f.write(str_data)
#
#     # 获取当前时刻的cookie
#     cookie_ = chrome_obj.get_cookies()
#     print(cookie_)
#     time.sleep(2)
#     chrome_obj.quit()
"""
由于网络问题，渲染页面，有可能会慢一点
当网速问题，搜索框还没有被渲染出来 
那么此时去定位搜索框，往里面输入关键字，就会出错







页面等待
如果网站采用了动态html技术，那么页面上的部分元素出现时间便不能确定，这个时候就可以设置一个等待时间，强制要求在时间内出现，否则报错

解决办法：
1.time.sleep(5)  优点：简单  缺点：有可能会造成一个时间上的浪费 
2.显示等待，隐式等待
    --selenium三种等待方式：https://www.cnblogs.com/gqv2009/p/12966181.html
    
selenium绕过js
selenium能够执行页面上的js，对于js渲染的数据和模拟登陆处理起来非常容易
selenium由于在获取页面的过程中会发送很多请求，所以效率非常低，所以在很多时候需要酌情使用

点击下一页
拖动网页进度条

"""
import time

from selenium import webdriver

if __name__ == '__main__':
    # 1.创建一个浏览器对象
    chrome_obj = webdriver.Chrome()   # C大写，加括号

    # 2.往网页地址栏输入网址，发送请求
    chrome_obj.get('https://www.baidu.com/')
    # 手动延迟，确保百度首页加载完毕，不会出现定位不到节点元素的情况
    time.sleep(1)

    # 3.1 在百度首页搜索框输入关键字
    # (1) 定位到搜索输入框 拥有id属性的节点，定位起来就很简单  找到节点id的值  kw keyword
    input_obj = chrome_obj.find_element_by_id('kw')   # 写完检查一下element有没有s
    # (2) 定位到了搜索框，往里面输入想要进行搜索的关键字
    input_obj.send_keys('京东')

    # 3.2 利用python代码点击百度一下，进行搜索
    # (1) 定位到(找到)'百度一下'那个按钮
    click_obj = chrome_obj.find_element_by_id('su')   # 定位input
    # (2) 利用python代码点击
    click_obj.click()   # 点击


    # 利用js来滑动页面
    # time.sleep(2)
    # chrome_obj.execute_script('window.scrollTo(0,2000)')

    # 拖动滚动条到底部
    # time.sleep(2)
    # chrome_obj.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # 拖动滚动条到指定位置
    time.sleep(2)
    chrome_obj.execute_script('document.documentElement.scrollTop=6000')  # 底部一般是一个较大的数值，比方说6000

    time.sleep(4)
    chrome_obj.quit()

