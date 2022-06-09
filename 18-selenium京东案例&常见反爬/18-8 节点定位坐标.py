"""
目标：获取百度logo图片的左上角坐标，宽高，右下角的坐标
"""
import time

from selenium import webdriver

# 创建浏览器对象
chrome_obj = webdriver.Chrome()

# 发送请求
chrome_obj.get('https://www.baidu.com')

time.sleep(1)
# 窗口最大化
chrome_obj.maximize_window()

# 定位百度的logo
img_obj = chrome_obj.find_element_by_id('s_lg_img')

# 获取左上角的坐标
location_ = img_obj.location
print('百度logo图片左上角坐标:',location_)

# 获取图片的宽和高
size_ = img_obj.size
print('图片的宽和高:',size_)

# 获取图片右下角的坐标
# 右下角的x轴:左上角的x轴 + 图片宽度
x_ = location_['x'] + size_['width']

# 右下角的y轴:左上角的y轴 + 图片高度
y_ = location_['y'] + size_['height']
print(x_)
print(y_)
time.sleep(5)
chrome_obj.quit()