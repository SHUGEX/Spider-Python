"""
演示url传参
"""
"""
疑问，我们输入'五一'两个字 然后呢就得到了相关的数据，页面
该页面是谁给我们的    >> 服务器 >> 
我们客户端告诉了服务器

五一  >> 也是一种数据，信息 >> 服务器
url:www.baidu.com

url携带参数的情况 
根据network里面的数据包的分析，图片都是一个单独的数据包，单独发送
html的骨架

我们在网址栏输入的url 一般都是网页主框架的url
当浏览器拿到了主框架的url的响应response之后
浏览器接收到了这个html文件的代码之后
它就会发现想要呈现(渲染)，发现里面有很多的坑坑洼洼
一个应该放图片的地方，它放的是图片url
此时浏览器就会拿着坑里面的图片的url去发自动发送网络请求
得到具体的响应之后，就填坑

最终组成了一个完整的页面，给我们看
"""



"""
url携带参数的体现 只填入了 五一 两个字
https://www.baidu.com/s?wd=%E4%BA%94%E4%B8%80&
rsv_spt=1&
rsv_iqid=0xaadb6777000337b8&
issp=1&f=8&
rsv_bp=1&
rsv_idx=2&
ie=utf-8&
tn=baiduhome_pg&
rsv_enter=0&
rsv_dl=tb&
rsv_sug3=9&
rsv_sug1=6&
rsv_sug7=100&
rsv_btype=i&prefixsug=%25E4%25BA%2594%25E4%25B8%2580&rsp=1&inputT=17257&rsv_sug4=34883

障眼法
某些参数其实是不影响我们的请求结果 
自url的?之后都是参数 以键值对的方式存在 a=b&c=d
经过分析，只有wd=五一 这个键值对(参数) 是必须的
百度输入框搜索一下的 关键字 实际上就是传给url wd = xxxx  word 
"""


"""
新的问题：
在network发现，传给服务器的参数 
wd=五一
wd=%E4%BA%94%E4%B8%80

中文传参不是那么地友好方便，中文经过浏览器的解析发送给服务器  五一  > %E4%BA%94%E4%B8%80
转义部分直接进行请求，也是可以的
类似的url的转义 了解即可
"""
# from urllib.parse import unquote,quote

# 明文(看得懂的数据) 五一   固定的关系映射表(固定的格式)   明文  > 密文   加密的场景
# data_ = '五一'
# print(quote(data_))    #  %E4%BA%94%E4%B8%80
                       #  %E4%BA%94%E4%B8%80

# 密文转为明文
# print(unquote('%E4%BA%94%E4%B8%80'))   # 五一
"""
url传参第一种方式，携带参数直接放在url里面
"""

# 导入发送请求的requests库
# import requests
#
#
# if __name__ == '__main__':
#     input_wd = input('请输入你想搜索的关键字:')
#     # 1.确认目标的url
#     url_ = f"https://www.baidu.com/s?wd={input_wd}"
#
#     # 1.1.添加用户代理User-Agent，伪造身份
#     headers_ = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#     # 2.发送网络请求，获取响应对象
#     response_ = requests.get(url_,headers=headers_)
#
#     # 2.1提取出里面的文本数据
#     bytes_data = response_.content
#     str_data = bytes_data.decode()  # 默认是utf-8
#
#     # 3.解析(目前略过)
#     # 4.保存
#     with open(f'baidu_{input_wd}.html','w',encoding="utf-8") as f:
#         f.write(str_data)



"""
url传参第二种方式，发送请求的时候再进行传参携带，而不是直接放在url里面
"""

# import requests
#
#
# if __name__ == '__main__':
#     input_wd = input('请输入你想搜索的关键字:')
#     # 1.确认目标的url
#     url_ = "https://www.baidu.com/s?"
#
#     # 1.1.添加用户代理User-Agent，伪造身份
#     headers_ = {
#         # Cookie:前后端的会话记录
#         "Cookie":'PSTM=1627283384; BIDUPSID=E87874A693DB88716FD0E61C71073BCC; __yjs_duid=1_be57b8bfc8bffacdf8573b0697073d511627307214203; sugstore=0; BD_UPN=12314753; BDUSS=VFelpXRlRSc2NTNHFLVkN3TWwyMlJqT0FkNGlPaWg3ZHM1eWM0dDJvOGl-VnhpRVFBQUFBJCQAAAAAAAAAAAEAAAC8Ped2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACJwNWIicDVid2; BDUSS_BFESS=VFelpXRlRSc2NTNHFLVkN3TWwyMlJqT0FkNGlPaWg3ZHM1eWM0dDJvOGl-VnhpRVFBQUFBJCQAAAAAAAAAAAEAAAC8Ped2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACJwNWIicDVid2; BAIDUID=2CE6267F273BA693BF721A0F8EB54795:FG=1; MCITY=-158%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=2CE6267F273BA693BF721A0F8EB54795:FG=1; delPer=0; BD_CK_SAM=1; BA_HECTOR=210h8k01810501243j1h658kg0q; BD_HOME=1; PSINO=6; COOKIE_SESSION=136_0_8_9_13_11_1_0_8_8_1_2_437_0_343_0_1650615451_0_1650615108%7C9%23598680_357_1650262393%7C9; H_PS_PSSID=36309_31660_36167_34584_36120_36339_36126_36233_26350_36315_36061; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; H_PS_645EC=f6e8TNLDlwwzIitD6OzKt07J%2Fsx64pwYM3Ir5D4TFpNMtCA3TRvdkhe%2BCS0; baikeVisitId=d43b865a-0cca-4cec-ac87-75006e5bd33c',
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#
#     # 设置字典，用来进行url携带参数
#     params_ = {
#         'wd':input_wd
#     }
#
#     # 2.发送网络请求，获取响应对象
#     #                      目标url    请求头(用户代理)   url传参
#     response_ = requests.get(url_,headers=headers_,params=params_)   # 把字典键值对自动拼接到url上面去
#
#     # 2.1提取出里面的文本数据
#     bytes_data = response_.content
#     str_data = bytes_data.decode()  # 默认是utf-8
#
#     # 3.解析(目前略过)
#     # 4.保存
#     with open(f'baidu_{input_wd}.html','w',encoding="utf-8") as f:
#         f.write(str_data)







"""
只要没有拿到想要的数据
而是出现'百度安全验证'，说明被反爬了，被识别出来了是一个爬虫程序
"""




"""
小作业
爬取百度贴吧
     美食吧
     
     加强：翻页(for循环) 10 可做可不做
     

网易云   一张图片的下载       >>  jpg png
        一首非VIP歌曲的下载   >> mp3
        一个MV的下载          >> mp4 
        
下周一之前写完，把代码发送给我的邮箱：1919270709@qq.com
"""