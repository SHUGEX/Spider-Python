"""
目标 https://search.bilibili.com/all?vt=76225871&keyword=%E4%B8%80%E7%B2%9F%E5%B0%8F%E8%8E%8E%E5%AD%90&from_source=webtop_search&spm_id_from=333.1007
心路历程：
    --1.关于如何自动获取到纯视频，纯音频文件
        -- 复制纯视频的url进行全局搜索，右上角三个点，菜单栏选择search
        -- 搜索，找到了存有纯视频的url,如果搜索不到，把https删掉s 再进行搜索
        -- 点击左上角{} 格式化输出，点击文件，ctrl + f
    --2.发现纯视频文件的url和纯音频文件的url都在同一个文件当中
        如果我们能够获取到这个文件的response,那么就能够提取了url进行请求，保存，合成
    --3.该文件实际为url地址栏的url请求对应的response
    --4.大概的网页框架
    --5.我们提前下载好的html，我们拿着在浏览器找到的url,发现能够找到


大概步骤：
1.input输入得到视频网页，利用这个url得到response
2.是一个html文件，html的代码，解析出来纯视频的url,纯音频的url
3.纯视频的url，纯音频的url去发送请求，得到响应，获取2个文件
4.合并视频
"""
"""
扩展：
        --1.发现video对应好几个部分 id: 60 64 32 16
            对应的是清晰度，可以用正则去取 id:80后面的url 1080P高清
"""

# 直接请求地址栏的url，尝试一下是否能拿到纯视频纯音频url

# import requests
#
# if __name__ == '__main__':
#     # 1.输入播放页面的url
#     url_ = input('请输入播放页面的url：')
#
#     # 设置请求头
#     headers_ = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
#         "referer": "https://www.bilibili.com/video/BV1uf4y187mm?spm_id_from=333.337.search-card.all.click"
#     }
#
#     response_ = requests.get(url_, headers=headers_)
#     str_data = response_.text
#
#     with open('战衣.html','w',encoding="utf-8") as f:
#         f.write(str_data)



"""
B站单个视频加强案例
"""
from moviepy.editor import *
import requests
from lxml import etree
import re
if __name__ == '__main__':
    # 1.输入播放页面的url
    url_ = input('请输入播放页面的url：')

    # 设置请求头
    headers_ = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
        "referer": "https://www.bilibili.com/video/BV1uf4y187mm?spm_id_from=333.337.search-card.all.click"
    }

    response_ = requests.get(url_, headers=headers_)
    str_data = response_.text # 视频主页的html代码，类型是字符串

    # 使用xpath解析html代码，得到想要的url
    html_obj = etree.HTML(str_data)

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
    response_video = requests.get(video_url, headers=headers_)
    bytes_video = response_video.content

    response_audio = requests.get(audio_url, headers=headers_)
    bytes_audio = response_audio.content

    # 保存
    with open('蓝色战衣_30080.mp4', 'wb') as f:
        f.write(bytes_video)
        print('纯视频文件下载完毕....')

    with open('蓝色战衣_30280.mp3', 'wb') as f:
        f.write(bytes_audio)
        print('纯音频文件下载完毕....')

    ffmpeg_tools.ffmpeg_merge_video_audio('蓝色战衣_30080.mp4', '蓝色战衣_30280.mp3', '蓝色.mp4')
    print('视频合成成功....')