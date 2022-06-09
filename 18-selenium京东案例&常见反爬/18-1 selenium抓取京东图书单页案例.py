from selenium import webdriver
# 延迟模块
import time
# 解析html
from lxml import etree
# 页面加载等待的异常处理
from selenium.common.exceptions import TimeoutException
import json
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


    # 保存
    with open('京东图片01.json','w',encoding="utf-8") as f:
        for i in range(len(title_list)):
            dict_ = {}
            dict_[title_list[i]] = price_list[i]
            json_data = json.dumps(dict_,ensure_ascii=False) + ',\n'
            f.write(json_data)




