import requests

if __name__ == '__main__':
    # 1.确认目标url 找到对应的数据包 右键点击copy > just url
    url_ = "https://mlol.qt.qq.com/go/mlol_news/varcache_article?docid=12886315326806732363&gameid=3&zone=plat&webview=cc"

    # 用户代理
    headers_ = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 Channel/3 lolapp/8.15.1.10751 lolappcpu/armeabi-v7a"
    }

    # 2.发送请求，获取响应
    response_ = requests.get(url_,headers=headers_)

    str_data = response_.text

    # 保存
    with open('1.html','w',encoding="utf-8") as f:
        f.write(str_data)