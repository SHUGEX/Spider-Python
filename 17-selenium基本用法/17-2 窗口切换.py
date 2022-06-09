import time
from selenium import webdriver

chrome_obj = webdriver.Chrome()

# 打开第1个网站，京东，窗口索引为0
chrome_obj.get('https://www.jd.com/')

# 打开第2个网站，豆瓣，窗口索引1
chrome_obj.execute_script('window.open("https://www.douban.com/","_blank");')

time.sleep(4)

# 获取当前所有的窗口
current_windows = chrome_obj.window_handles

# 根据窗口索引进行切换  两个窗口的话，索引分别为0和1
# 切换为京东，京东窗口索引为0
chrome_obj.switch_to.window(current_windows[0])

time.sleep(2)

# 切换为豆瓣，豆瓣窗口索引为1
chrome_obj.switch_to.window(current_windows[1])

time.sleep(2)

# 切换为京东，京东窗口索引为0
chrome_obj.switch_to.window(current_windows[0])

time.sleep(2)

# 切换为豆瓣，豆瓣窗口索引为1
chrome_obj.switch_to.window(current_windows[1])

time.sleep(2)

chrome_obj.quit()
