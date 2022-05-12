"""
1.使用登录过后的cookie get: cookie是有效期
2.post请求模拟登录

登录一次
10个页面 就需要登录10次 太过于麻烦
容易被检测到非正常的用户行为，从而被封禁账号
"""

"""
解决办法：
首先用post请求模拟登录 我们就可以直接获取到最新的登录后的cookie
再拿着这个最新的cookie去发送get请求不同的页面
"""

import requests

if __name__ == '__main__':
    # 1.确认目标的url()
    login_url = "http://www.qishu7.com/login.php?do=submit"

    # 用户代理
    headers_ = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }

    # 构造form表单数据
    form_data = {
        "username": "sixstar_dahai",
        "password": "123456",
        "usecookie": "0",
        "action": "login",
        "submit": "%26%23160%3B%B5%C7%26%23160%3B%26%23160%3B%C2%BC%26%23160%3B"
    }

    # 如果想要自动携带登录过后的cookie,那么就需要封装一个新的发送请求的对象
    session_ = requests.session()

    session_.post(login_url,headers=headers_,data=form_data)  # 这里可以不接受响应对象

    # 目的主浊为了让这个对象session_携带有登录过后的cookie
    showdata_url = "http://www.qishu7.com/userdetail.php"
    response_ = session_.get(showdata_url,headers=headers_)   # session_自动携带了登录过后的cookie

    str_data = response_.content.decode('gbk')

    # 保存
    with open('qishu05.html', 'w', encoding="gbk") as f:
        f.write(str_data)




