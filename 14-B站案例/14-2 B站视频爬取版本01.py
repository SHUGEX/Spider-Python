"""
如何找B站视频数据包(B站视频数据包的特征)：
1.找数据包包名问号前面出现有m4s的
2.连续不断出现的


30080：https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/23/56/350715623/350715623-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1652883554&gen=playurlv2&os=hwbv&oi=2936639454&trid=4b3b9c2681ab492e8516494bbdd6d95eu&platform=pc&upsig=220e4d5530b598aff5436a9680f694bd&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=480316594&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=333704&logo=80000000

30280：https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/23/56/350715623/350715623-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1652883554&gen=playurlv2&os=hwbv&oi=2936639454&trid=4b3b9c2681ab492e8516494bbdd6d95eu&platform=pc&upsig=402bce4835763fba03257e8bd6db3c09&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=480316594&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=16623&logo=80000000
"""



import requests
from moviepy.editor import *
if __name__ == '__main__':
    # 1.确认目标url
    url_30080 = "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/23/56/350715623/350715623-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1652883881&gen=playurlv2&os=hwbv&oi=2936639454&trid=9b40386204774fedb37ee4273b472b53u&platform=pc&upsig=d34a9551a4a704e68efce76e83132827&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=480316594&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=333704&logo=80000000"
    url_30280 = "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/23/56/350715623/350715623-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1652883881&gen=playurlv2&os=hwbv&oi=2936639454&trid=9b40386204774fedb37ee4273b472b53u&platform=pc&upsig=0b68e5c220803124d2220c261e8ff56d&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=480316594&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=16623&logo=80000000"

    # 设置请求头
    headers_ = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
        "referer": "https://www.bilibili.com/video/BV1uf4y187mm?spm_id_from=333.337.search-card.all.click"
    }

    # 2.发送请求得到响应
    response_30080 = requests.get(url_30080,headers=headers_)
    response_30280 = requests.get(url_30280,headers=headers_)

    data_30080 = response_30080.content
    data_30280 = response_30280.content

    # 保存
    with open('蓝色战衣_30080.mp4','wb') as f:
        f.write(data_30080)

    with open('蓝色战衣_30280.mp3','wb') as f:
        f.write(data_30280)

    # 选择一个已经拥有的纯视频文件
    video_obj = VideoFileClip('蓝色战衣_30080.mp4')

    # 选择一个对应的已经拥有的纯音频文件
    audio_obj = AudioFileClip('蓝色战衣_30280.mp3')

    # 往视频对象里面添加音频
    movie_ = video_obj.set_audio(audio_obj)

    # 保存
    movie_.write_videofile('蓝色.mp4')











"""
30080数据包是一个纯视频文件，没有声音    10s    37s
30280数据包是一个纯音频文件，没有画面    11s    37s

想办法：让纯视频文件，纯音频文件合二为一
1.同时打开2个文件，再录制，感觉还可以
2.第三方库moviepy合成 
pip install moviepy -i https://pypi.doubanio.com/simple

在拥有了一个纯视频文件跟一个纯音频文件的情况下
利用第三方库moviepy合成  速度很慢 

注意点！！！！
1.B站纯视频纯音频的url，是动态变化着的，当之前写好的代码运行报错的时候，重新加载，重新抓包，把最新的
  纯视频纯音频url替换进去 

2.B站纯视频纯音频数据包的包名，也是动态变化着的
"""