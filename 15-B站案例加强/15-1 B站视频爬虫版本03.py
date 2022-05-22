"""
优化:
1.我们下载下来的视频名称是否能够改成网页视频原名
    --网页里面的视频名称，已知网页为html数据，名称可以使用xpath调试拿到
    --有几种方式，有几种xpath语法可以获取到视频名称呢 8种方式可以获取到
        问题：这个视频可以利用  //h1/text() 取到视频名称
              其它视频也可能么  该xpath语法并不通用
              改xpath取视频名称通用  //title/text()
              是七叔呢 -《半生雪》，半生风雪，吹不散花落时节的眼泪，唤不回孤雁终要南飞，心事谁了解唯有明月来相随，思念予我眉间又几分憔悴。_哔哩哔哩_bilibili


            1.通过xpath语法提取到名称，再进行一个切片 ，正则

        问题：视频的名称中，如果包含有空格  / & 都会影响到视频的合成
            解决办法，去掉名称中的 空格  / &

        问题：  title_ = 思思520节日快乐
               纯视频文件： 思思520节日快乐！.mp4
               纯音频文件:  思思520节日快乐！.mp3
               合成的文件:  思思520节日快乐.mp4
               为了避免因为重名造成的问题，可以添加一个字符，改变一下视频名称，避免重名

2.纯视频文件，纯音频文件，自动删除
    --os.remove()


3.如果想显示文件的大小
    --1.发送请求的时候，添加参数 stream=True
    --2.获取大小
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