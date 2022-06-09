"""
验证码:
登录：
注册：

验证码的分类:
1.滑块
2.纯数字，纯英文
3.英文数字结合
4.汉字 成语点击
5.拼图
6.物品选择  8张思思 1张雪锐
7.图片摆正
"""

"""
目标:滑动验证码
1.定位按钮
2.按住滑块
3.滑动按钮
"""
from selenium import webdriver

# 创建一个浏览器对象
chrome_obj = webdriver.Chrome()

# 发送请求
chrome_obj.get("https://www.helloweba.net/demo/2017/unlock/")

# 1.定位滑块按钮
short_obj = chrome_obj.find_element_by_xpath('//div[@class="bar1 bar"]/div[@class="slide-to-unlock-handle"]')

# 2.按住
# 创建一个动作链对象，参数就是浏览器对象
action_obj = webdriver.ActionChains(chrome_obj)

# 点击并且按住，参数就是定位的按钮
action_obj.click_and_hold(short_obj)

# 定位整条滑块
long_obj = chrome_obj.find_element_by_xpath('//div[@class="bar1 bar"]/div[@class="slide-to-unlock-bg"]')

# 得到整条滑块的宽高
size_ = long_obj.size
width_ = size_['width']

# 3.定位滑动坐标
action_obj.move_by_offset(width_,0).perform()

# 4.松开滑动
action_obj.release()