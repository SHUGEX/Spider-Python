"""
演示抓取登录后的页面
cookie
post请求
"""

"""
利用cookie抓取登录过后的页面
"""
# 目标网站：http://www.qishu7.com/
# import requests
#
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "http://www.qishu7.com/modules/article/bookcase.php"
#
#     # 设置用户代理
#     headers_ = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#
#     # 2.利用requests发送get请求，得到响应对象
#     response_= requests.get(url_,headers=headers_)
#
#     str_data = response_.content.decode('gbk')
#
#     # 保存
#     with open('qishu01.html','w',encoding="gbk") as f:
#         f.write(str_data)

"""
结果：打开的是一个登录页面 html代码  css样式美术功底 
同一个url:http://www.qishu7.com/modules/article/bookcase.php
爬虫程序访问 > 登录页面
浏览器访问   > 美观的主页

浏览器访问:会自动携带上cookie
爬虫程序访问：没有带上cookie

cookie:会话记录 > 记录着你的客户端和服务端进行交互的记录
浏览器：我们填入了一次用户名和密码之后 就会被记录在cookie里面
        第二次访问该网站的时候，自动携带了拥有登录信息的cookie，所以就实现了自动登录
        
爬虫：并没有携带带有(登录信息)的cookie,所以服务器就返回给你登录页面
如果我们的爬虫程序 拥有了登录过后的cookie(登录信息)，就可以请求得到登录过后的页面
"""



"""
如何利用cookie抓取登录过后的页面
"""


"""
第一种cookie添加方法，直接以键值对的方式，放到headers里面
为了尽可能的模拟正常的用户
1.添加用户代理
2.添加cookie:去浏览器寻找正常用户的登录过后的cookie
"""

# import requests
#
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "http://www.qishu7.com/modules/article/bookcase.php"
#
#     # 设置用户代理
#     headers_ = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
#         "Cookie":"UM_distinctid=17fdfc949e53ee-011b40f6521126-576153e-1fa400-17fdfc949e6589; CNZZDATA1254529914=2131565625-1648718962-https%253A%252F%252Fwww.baidu.com%252F%7C1651056908; PHPSESSID=ivm9gemo7hvesu8vb224uibub1; jieqiUserInfo=jieqiUserId%3D1164%2CjieqiUserUname%3Dsixstar_dahai%2CjieqiUserName%3Dsixstar_dahai%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D%2CjieqiUserHonor%3D%D0%C2%CA%D6%C9%CF%C2%B7%2CjieqiUserUname_un%3Dsixstar_dahai%2CjieqiUserName_un%3Dsixstar_dahai%2CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1651062880; jieqiVisitInfo=jieqiUserLogin%3D1651062880%2CjieqiUserId%3D1164"
#     }
#
#     # 2.利用requests发送get请求，得到响应对象
#     response_= requests.get(url_,headers=headers_)
#
#     str_data = response_.content.decode('gbk')
#
#     # 保存
#     with open('qishu02.html','w',encoding="gbk") as f:
#         f.write(str_data)



"""
第二种携带cookie的方法
"""
# import requests
#
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "http://www.qishu7.com/modules/article/bookcase.php"
#
#     # 设置用户代理
#     headers_ = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
#     }
#
#
#     # 单独构造一个字典，携带cookie
#     cookies_ = {"Cookie":"UM_distinctid=17fdfc949e53ee-011b40f6521126-576153e-1fa400-17fdfc949e6589; CNZZDATA1254529914=2131565625-1648718962-https%253A%252F%252Fwww.baidu.com%252F%7C1651056908; PHPSESSID=ivm9gemo7hvesu8vb224uibub1; jieqiUserInfo=jieqiUserId%3D1164%2CjieqiUserUname%3Dsixstar_dahai%2CjieqiUserName%3Dsixstar_dahai%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D%2CjieqiUserHonor%3D%D0%C2%CA%D6%C9%CF%C2%B7%2CjieqiUserUname_un%3Dsixstar_dahai%2CjieqiUserName_un%3Dsixstar_dahai%2CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1651062880; jieqiVisitInfo=jieqiUserLogin%3D1651062880%2CjieqiUserId%3D1164"}
#
#     # 2.利用requests发送get请求，得到响应对象
#     response_= requests.get(url_,headers=headers_,cookies=cookies_)
#
#     str_data = response_.content.decode('gbk')
#
#     # 保存
#     with open('qishu03.html','w',encoding="gbk") as f:
#         f.write(str_data)





"""
利用post请求完成模拟登录，去得到登录过后的数据
post请求 > url
模拟登录 > 用户名，密码(最基本的)

username: sixstar_dahai
password: abc
usecookie: 0
action: login
submit: %26%23160%3B%B5%C7%26%23160%3B%26%23160%3B%C2%BC%26%23160%3B

username: sixstar_dahai
password: 123456
usecookie: 0
action: login
submit: %26%23160%3B%B5%C7%26%23160%3B%26%23160%3B%C2%BC%26%23160%3B

快速添加引号：按住Alt不放，鼠标点击你想要添加引号的地方，最后再输入引号
"""





import requests

if __name__ == '__main__':
    # 1.确认目标的url
    url_ = "http://www.qishu7.com/login.php?do=submit"

    # 设置用户代理
    headers_ = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    }


    # 模拟登录，就不需要携带登录信息
    # 携带数据(form表单里面携带)
    form_data = {
        "username": "sixstar_dahai",
        "password": "123456",
        "usecookie": "0",
        "action": "login",
        "submit": "%26%23160%3B%B5%C7%26%23160%3B%26%23160%3B%C2%BC%26%23160%3B"
    }

    # 2.利用requests去发送post请求，模拟登录
    response_ = requests.post(url_,headers=headers_,data=form_data)

    str_data = response_.content.decode('gbk')

    # 保存
    with open('qishu04.html', 'w', encoding="gbk") as f:
        f.write(str_data)


"""
cookie也能够拿到登录过后的数据
每次都需要去现拿，存在一个cookie过期的问题

使用post请求模拟登录的好处是什么
"""