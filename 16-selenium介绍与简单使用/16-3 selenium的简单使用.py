"""
1.已经有了第三方库 selenium
2.已经有了驱动chromedriver 并且放到了和python解释器同一目录
"""
# selenium本质就是模拟浏览器
# import time
#
# from selenium import webdriver
#
# if __name__ == '__main__':
#     # 1.创建浏览器对象
#     chrome_obj = webdriver.Chrome()   # 运行 > 效果 > 打开一个谷歌浏览器
#     # chrome_obj = webdriver.Chrome(executable_path='D:\chromedeiver.exe')   # 运行 > 效果 > 打开一个谷歌浏览器
#
#     # 2.发送请求
#     chrome_obj.get('https://www.baidu.com/')   # 执行 > 效果 > 发送请求，访问相关的页面
#
#     # 3.提取访问页面的数据 源代码
#     str_data = chrome_obj.page_source   # 执行 > 效果 > 获取当前页面的源代码
#
#     with open('baidu01.html','w',encoding="utf-8") as f:
#         f.write(str_data)
#
#     # 截取更多(窗口最大化)
#     chrome_obj.maximize_window()
#
#     # 网页截屏
#     chrome_obj.save_screenshot('baidu02.png')
#
#     # 4.关闭浏览器
#     # 关闭页面
#     # time.sleep(2)
#     # chrome_obj.close()
#     # 关闭浏览器
#     time.sleep(2)
#     chrome_obj.quit()


"""
chrome_obj = webdriver.Chrome() 能够打开浏览器，就是依靠的chromedriver
因为chromedeiver与python解释器同一目录  所以可以直接调用 
D:\chromedeiver.exe
"""





"""
selenium无界面模式：无头模式
之前的代码是可以看到浏览器的创建打开
优点>肉眼可见，清晰
缺点>影响效率

解决办法:设置成无头模式，浏览器不会出现打开关闭的肉眼操作，但是数据还是一样能够获取到
"""





import time
from selenium.webdriver.chrome.options import Options # 注意点 最后一个Options首字母是大写的O
from selenium import webdriver
if __name__ == '__main__':
    # 设置无界面模式
    option_ = Options()
    option_.add_argument('--headless')   # 设置参数，改成无界面模式
    # 1.创建浏览器对象
    chrome_obj = webdriver.Chrome(options=option_)   # 运行 > 效果 > 打开一个谷歌浏览器
    # chrome_obj = webdriver.Chrome(executable_path='D:\chromedeiver.exe')   # 运行 > 效果 > 打开一个谷歌浏览器

    # 2.发送请求
    chrome_obj.get('https://www.baidu.com/')   # 执行 > 效果 > 发送请求，访问相关的页面

    # 3.提取访问页面的数据 源代码
    str_data = chrome_obj.page_source   # 执行 > 效果 > 获取当前页面的源代码

    with open('baidu02.html','w',encoding="utf-8") as f:
        f.write(str_data)

    # 截取更多(窗口最大化)
    # chrome_obj.maximize_window()

    # 网页截屏  无界面模式下 无用
    # chrome_obj.save_screenshot('baidu02.png')

    # 4.关闭浏览器
    # 关闭页面
    # time.sleep(2)
    # chrome_obj.close()
    # 关闭浏览器
    time.sleep(2)
    chrome_obj.quit()
