
"""
翻页url的规律
--第2页url参数:
    __refresh__: true
    _extra:
    context:
    page: 2
    page_size: 42
    from_source:
    from_spmid: 333.337
    platform: pc
    highlight: 1
    single_column: 0
    keyword: 是七叔呢
    category_id:
    search_type: video
    dynamic_offset: 30
    preload: true
    com2co: true

-第3页url参数：
    __refresh__: true
    _extra:
    context:
    page: 3
    page_size: 42
    from_source:
    from_spmid: 333.337
    platform: pc
    highlight: 1
    single_column: 0
    keyword: 是七叔呢
    category_id:
    search_type: video
    dynamic_offset: 60
    preload: true
    com2co: true

经过分析，url参数中发生变化的有2个，其中控制翻页的关键参数为page参数，并且page值以1进行递增
        还有dynamic_offset参数是以30进行递增

        第2页：page=2&dynamic_offset=30
        第3页：page=3&dynamic_offset=60
"""
# import time
# import jsonpath
# from moviepy.editor import *
# import requests
# from lxml import etree
# import re
#
# if __name__ == '__main__':
#     data = input('请输入你想要搜索的内容:')
#     pages_ = int(input('请输入你要爬取的页数:'))
#     list_ = []   # 保存全部视频的url
#
#     # 循环翻页爬取
#     for page in range(pages_):    # 5 > 0 1 2 3 4
#         # 列表页的url
#         url_ = "https://api.bilibili.com/x/web-interface/search/type"
#
#         # 用户代理
#         headers_ = {
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
#         }
#
#         params_ = {
#             "__refresh__": "true",
#             "_extra":"",
#             "context":"",
#             "page": str(page+1),
#             "page_size": "30",
#             "from_source":"",
#             "from_spmid": "333.337",
#             "platform": "pc",
#             "highlight": "1",
#             "single_column": "0",
#             "keyword": data,
#             "category_id":"",
#             "search_type": "video",
#             "dynamic_offset": str(page*30),
#             "preload": "true",
#             "com2co": "true"
#         }
#
#
#         response_ = requests.get(url_,headers=headers_,params=params_)
#         py_data = response_.json()
#         url_list = jsonpath.jsonpath(py_data,'$..arcurl')    # 单页30个视频的url的一个列表
#
#         for url in url_list:
#             # 保存视频主页的url，就代表下载着视频
#             list_.append(url)
#
#         # 翻页手动延迟，降低请求频率，避免被反爬
#         time.sleep(2)
#
#     # print(len(list_))     # 1 > 30    5 > 150
#     list2 = list(set(list_))   # 列表去重
#
#     print(len(list2))

"""
此时此刻进行的翻页   5 > 150   
重复的视频 
列表去重
150-144 = 6
相当于丢失了6个视频没有抓取到
如果是50页 >> 60个视频
1 20:24    1 A  B  C    2 D E F 
  20:44    2 B  E  F
动态的 

时间相关: 按照之前的逻辑，做翻页肯定是不行  1 30  > B  2 > B
解决办法：
    --第一页：30url都抓取下来
    --第二页：30url都抓取下来




身份：cookie
 
"""
import time
import jsonpath
from moviepy.editor import *
import requests
from lxml import etree
import re

if __name__ == '__main__':
    data = input('请输入你想要搜索的内容:')
    pages_ = int(input('请输入你要爬取的页数:'))
    list_ = []   # 保存全部视频的url

    # 循环翻页爬取
    for page in range(pages_):    # 5 > 0 1 2 3 4
        # 列表页的url
        url_ = "https://api.bilibili.com/x/web-interface/search/type"

        # 用户代理
        headers_ = {
            "cookie": "_uuid=8E9986D8-D2B1-AE0F-9F4E-057B59DDE7B113399infoc; buvid3=B715F603-8F69-491D-9E9D-C6AD5F30E32C167628infoc; rpdid=|(kmJYYJJm~~0J'uYk~kmukuY; LIVE_BUVID=AUTO7116320481434802; video_page_version=v_old_home_15; buvid4=989625F2-25A5-45BE-BD6A-E429EF7B54B205641-022012415-ITAnNTZexY+HQNpqD0SMFg%3D%3D; i-wanna-go-back=-1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; nostalgia_conf=-1; CURRENT_QUALITY=80; bp_video_offset_346439120=657498886757154800; fingerprint3=58f72d5e80d3c6f7afc44f6bf1ee3db6; fingerprint=76d5fc46f25a25328d6d73e40257d13c; SESSDATA=16371742%2C1667482930%2Cf4314%2A51; bili_jct=254aa78ba6a792b20698197c401bdaff; DedeUserID=480316594; DedeUserID__ckMd5=abb5ecaf86880f0c; sid=brjo57o4; b_ut=5; buvid_fp=76d5fc46f25a25328d6d73e40257d13c; bp_video_offset_480316594=653031313304977400; blackside_state=0; PVID=2; bsource=search_baidu; b_lsid=8DC87A5F_180F0821B12; innersign=1; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_B715F603%22%3A%22180F0814F74%22%2C%22333.337.fp.risk_B715F603%22%3A%22180F0CB1EB4%22%2C%22333.788.fp.risk_B715F603%22%3A%22180F0CC5AB8%22%7D%7D; CURRENT_FNVAL=80",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
        }

        params_ = {
            "__refresh__": "true",
            "_extra":"",
            "context":"",
            "page": str(page+1),
            "page_size": "30",
            "from_source":"",
            "from_spmid": "333.337",
            "platform": "pc",
            "highlight": "1",
            "single_column": "0",
            "keyword": data,
            "category_id":"",
            "search_type": "video",
            "dynamic_offset": str(page*30),
            "preload": "true",
            "com2co": "true"
        }


        response_ = requests.get(url_,headers=headers_,params=params_)
        py_data = response_.json()
        url_list = jsonpath.jsonpath(py_data,'$..arcurl')    # 单页30个视频的url的一个列表

        for url in url_list:      #  已经把时间缩短了
            # 保存视频主页的url，就代表下载着视频
            list_.append(url)

        # 翻页手动延迟，降低请求频率，避免被反爬
        time.sleep(1)

    # print(len(list_))     # 1 > 30    5 > 150
    list2 = list(set(list_))   # 列表去重

    print(len(list2))
