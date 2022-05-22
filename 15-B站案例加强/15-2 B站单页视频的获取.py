"""
目标：输入一个关键字，获取该页所有的视频
     --比方说输入一个'一粟小莎子' 获取到该页30个视频，参数(数据) 发送给服务端的


__refresh__: true
_extra:
context:
page: 1
page_size: 42
order:
duration:
from_source:
from_spmid: 333.337
platform: pc
highlight: 1
single_column: 0
keyword: 一粟小莎子
preload: true
com2co: true

__refresh__: true
_extra:
context:
page: 1
page_size: 42
order:
duration:
from_source:
from_spmid: 333.337
platform: pc
highlight: 1
single_column: 0
keyword: 是七叔呢
preload: true
com2co: true



经过分析，请求方式是get,并且url参数中唯一发生动态变化的是keyword参数
构造url参数字典，发送请求，得到响应  json数据 提取到30个视频详情页的url,执行单个视频的代码运行
"""
import time

import jsonpath
from moviepy.editor import *
import requests
from lxml import etree
import re
if __name__ == '__main__':
    # 输入得到关键字
    data_ = input('请输入你想要搜索的内容:')
    url_ = "https://api.bilibili.com/x/web-interface/search/all/v2"

    headers_ = {
        "cookie": "_uuid=8E9986D8-D2B1-AE0F-9F4E-057B59DDE7B113399infoc; buvid3=B715F603-8F69-491D-9E9D-C6AD5F30E32C167628infoc; rpdid=|(kmJYYJJm~~0J'uYk~kmukuY; LIVE_BUVID=AUTO7116320481434802; video_page_version=v_old_home_15; buvid4=989625F2-25A5-45BE-BD6A-E429EF7B54B205641-022012415-ITAnNTZexY+HQNpqD0SMFg%3D%3D; i-wanna-go-back=-1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; nostalgia_conf=-1; CURRENT_QUALITY=80; bp_video_offset_346439120=657498886757154800; fingerprint3=58f72d5e80d3c6f7afc44f6bf1ee3db6; fingerprint=76d5fc46f25a25328d6d73e40257d13c; SESSDATA=16371742%2C1667482930%2Cf4314%2A51; bili_jct=254aa78ba6a792b20698197c401bdaff; DedeUserID=480316594; DedeUserID__ckMd5=abb5ecaf86880f0c; sid=brjo57o4; b_ut=5; buvid_fp=76d5fc46f25a25328d6d73e40257d13c; bp_video_offset_480316594=653031313304977400; PVID=1; bsource=search_baidu; blackside_state=0; innersign=1; b_lsid=E110AC7E5_180E15E8E89; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_B715F603%22%3A%22180E14D6088%22%2C%22333.337.fp.risk_B715F603%22%3A%22180E19A3EEE%22%2C%22333.788.fp.risk_B715F603%22%3A%22180E1A1F4AF%22%7D%7D; CURRENT_FNVAL=80",
        "referer": "https://search.bilibili.com/all?keyword=%E6%98%AF%E4%B8%83%E5%8F%94%E5%91%A2&from_source=webtop_search&spm_id_from=333.1007",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

    params_ = {
        "__refresh__": "true",
        "_extra":"",
        "context":"",
        "page": "1",
        "page_size": "30",
        "order":"",
        "duration":"",
        "from_source":"",
        "from_spmid": "333.337",
        "platform": "pc",
        "highlight": "1",
        "single_column": "0",
        "keyword":  data_,
        "preload": "true",
        "com2co": "true"
    }

    response_ = requests.get(url_,headers=headers_,params=params_)
    py_data = response_.json()

    # 提取出30个视频的详情页的url
    url_list = jsonpath.jsonpath(py_data,'$..arcurl')
    print(len(url_list),url_list)

    # 循环发送请求，获取到所有的视频
    for url_ in url_list:
        # 设置请求头
        headers_ = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
            "referer": url_
        }

        response_ = requests.get(url_, headers=headers_)
        str_data = response_.text # 视频主页的html代码，类型是字符串

        # 使用xpath解析html代码，得到想要的url
        html_obj = etree.HTML(str_data)

        # 获取视频的名称
        res_ = html_obj.xpath('//title/text()')[0]   # 是七叔呢 -《半生雪》，半生风雪，吹不散花落时节的眼泪，唤不回孤雁终要南飞，心事谁了解唯有明月来相随，思念予我眉间又几分憔悴。_哔哩哔哩_bilibili

        title_ = re.findall(r'(.*?)_哔哩哔哩', res_)[0]

        # 影响视频合成的特殊字符的处理
        title_ = title_.replace('/','')
        title_ = title_.replace(' ','')
        title_ = title_.replace('&','')


        # 取到数据为列表，索引[0]取值取出里面的字符串，包含视频音频文件url所在的字符串
        url_list_str = html_obj.xpath("//script[contains(text(),'window.__playinfo__')]/text()")[0]

        video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"', url_list_str)[0]

        audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"', url_list_str)[0]

        # 设置请求头
        headers_ = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
            "referer": url_
        }

        # 2.发送请求得到响应
        response_video = requests.get(video_url, headers=headers_,stream=True)
        bytes_video = response_video.content

        response_audio = requests.get(audio_url, headers=headers_,stream=True)
        bytes_audio = response_audio.content

        # 获取文件大小 单位为KB
        video_size = int(int(response_video.headers['content-length'])/1024)
        audio_size = int(int(response_audio.headers['content-length'])/1024)

        title_1 = title_ + '!'   # 名称进行修改，避免重名
        # 保存
        with open(f'{title_1}.mp4', 'wb') as f:
            f.write(bytes_video)
            print(f'{title_1}>>>>纯视频文件下载完毕....大小为{video_size}KB,{int(video_size/1024)}MB')

        with open(f'{title_1}.mp3', 'wb') as f:
            f.write(bytes_audio)
            print(f'{title_1}>>>>纯音频文件下载完毕....大小为{audio_size}KB,{int(audio_size/1024)}MB')

        ffmpeg_tools.ffmpeg_merge_video_audio(f'{title_1}.mp4', f'{title_1}.mp3', f'{title_}.mp4')

        # 显示合成文件的大小
        res_ = int(os.stat(f'{title_}.mp4').st_size / 1024)
        print(f'{title_}>>>>视频合成成功....大小为{res_}KB,{int(res_ / 1024)}MB')

        print('视频合成成功....')
        # 移除纯视频文件
        os.remove(f'{title_1}.mp4')
        # 移除纯音频文件
        os.remove(f'{title_1}.mp3')

        # 手动降低请求频率
        time.sleep(1)

        # 隔开每一个视频的信息
        print("*"*100)

    print('视频全部抓取完毕....')