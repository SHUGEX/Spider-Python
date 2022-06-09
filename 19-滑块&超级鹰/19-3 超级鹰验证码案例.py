"""
1.创建浏览器对象
2.发送请求
3.窗口最大化
4.页面截图
5.获取图片坐标
6.进行图片裁剪
7.把图片给超级鹰，帮助我们识别验证码
8.输入账号 密码，验证码
9.点击登录
"""
import time

from selenium import webdriver
from PIL import Image

# 1.创建浏览器对象
chrome_obj = webdriver.Chrome()

# 2.发送请求
chrome_obj.get('https://www.chaojiying.com/user/login/')

# 3.窗口最大化
chrome_obj.maximize_window()

# 4.页面截图
chrome_obj.save_screenshot('login.png')

# 5.获取图片坐标
# 定位元素
img_obj = chrome_obj.find_element_by_xpath('//div[@class="login_form"]//img')

# 获取左上角坐标
location_ = img_obj.location
print('左上角坐标:',location_)

# 获取图片的宽高
size_ = img_obj.size
print('图片的宽高:',size_)

             # 左上角的x坐标  左上角的y坐标        右下角的x坐标                     右下角的y坐标
img_range = (location_['x'],location_['y'],location_['x'] + size_['width'],location_['y'] + size_['height'])

# 读取图片
img_ = Image.open('login.png')

# 裁剪图片
res_ = img_.crop(img_range)

# 保存结果
res_.save('cjy.png')     # 注意点：缩放要设置成100%

# 7.把图片交给超级鹰，帮助我们识别验证码
#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64':base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    # 创建客户端对象                 用户名       密码       软件ID
    chaojiying = Chaojiying_Client('dahai789', '123456', '934361')	#用户中心>>软件ID 生成一个替换 96001
    # 验证码图片对象
    im = open('cjy.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    #     客户端对象.处理图片方法(验证码图片对象,验证码的类型编号)
    # print(chaojiying.PostPic(im, 1902))												#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    #print chaojiying.PostPic(base64_str, 1902)  #此处为传入 base64代码
    # 返回一个字典，我们需要pic_str的值

    # 获取验证码
    code_ = chaojiying.PostPic(im, 1902)['pic_str']
    print(code_)

    # 输入账号
    chrome_obj.find_element_by_name('user').send_keys('dahai789')
    time.sleep(1)

    # 输入密码
    chrome_obj.find_element_by_name('pass').send_keys('123456')
    time.sleep(1)

    # 输入验证码
    chrome_obj.find_element_by_name('imgtxt').send_keys(code_)
    time.sleep(1)

    # 点击登录
    chrome_obj.find_element_by_class_name('login_form_input_submit').click()
    time.sleep(1)

    # chrome_obj.quit()

