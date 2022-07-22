"""
如何找B站视频数据包(B站视频数据包的特征):
1.找数据包名url问号前面出现有m4s
2.连续不断出现的

30033：
https://xy123x101x157x254xy.mcdn.bilivideo.cn:4483/upgcxcode/98/91/441399198/441399198_x1-1-30033.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1646148111&gen=playurlv2&os=mcdn&oi=2936635645&trid=00017211271c3bc644009e96f8bc2d080735u&platform=pc&upsig=3fc8f2bfeda29cbf325a99bcddb05cc6&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=2001832&mid=346439120&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=50386&logo=A0000002

30280：
https://xy218x85x123x10xy.mcdn.bilivideo.cn:4483/upgcxcode/98/91/441399198/441399198-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1646148111&gen=playurlv2&os=mcdn&oi=2936635645&trid=00007211271c3bc644009e96f8bc2d080735u&platform=pc&upsig=cb969e294231fda07de7668533421c30&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=11000103&mid=346439120&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=15975&logo=A0000400

"""

import requests
from moviepy.editor import *
if __name__ == '__main__':
    # 1.确认url
    url_30033 = "https://xy1x196x219x73xy.mcdn.bilivideo.cn:4483/upgcxcode/98/91/441399198/441399198_x1-1-30033.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1646148481&gen=playurlv2&os=mcdn&oi=1996142019&trid=000116c42bfb753f4b8a9bdb0008b00f2dafu&platform=pc&upsig=c08e1938178b722467aa85e9d8d8ee9b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=2001832&mid=346439120&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=50386&logo=A0000002"
    url_30280 = "https://xy218x85x123x10xy.mcdn.bilivideo.cn:4483/upgcxcode/98/91/441399198/441399198-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1646148481&gen=playurlv2&os=mcdn&oi=1996142019&trid=000016c42bfb753f4b8a9bdb0008b00f2dafu&platform=pc&upsig=3958acafb01ecee2ee796dae15708828&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mcdnid=11000103&mid=346439120&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=15975&logo=A0000400"

    # 设置请求头
    headers_ = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "referer": "https://www.bilibili.com/video/BV1LT4y1R7Qt?from=search&seid=14932957783913729889&spm_id_from=333.337.0.0",
    }

    # 2.发送请求得到响应
    response_30033 = requests.get(url_30033,headers=headers_)
    response_30280 = requests.get(url_30280,headers=headers_)

    data_30033 = response_30033.content
    data_30280 = response_30280.content

    # 4.保存
    with open('毛肚_30033.mp4','wb') as f:
        f.write(data_30033)

    with open('毛肚_30280.mp3','wb') as f:
        f.write(data_30280)

    # 选择一个已经拥有的纯视频文件
    video_obj = VideoFileClip('毛肚_30033.mp4')

    # 选择一个对应的已经拥有的纯音频文件
    audio_obj = AudioFileClip('毛肚_30280.mp3')

    # 往视频对象里面添加音频
    movie_ = video_obj.set_audio(audio_obj)

    # 保存
    movie_.write_videofile('最终合成_毛肚.mp4')


"""
30033数据包是一个纯视频文件，没有声音  10s   3min53s
30280数据包是一个纯音频文件，没有画面  11s   3min53s

想办法：让纯视频文件，纯音频文件合二为一
1.同时打开两个文件，再录制，感觉还可以
2.第三方库moviepy合成 
pip install moviepy -i https://pypi.doubanio.com/simple

在拥有了一个纯视频文件，跟一个纯音频文件的情况下
利用第三方库moviepy合成：速度比较慢

注意点！！！！
1.B站纯音频纯音频的url，是动态变化着的，如果之前写好的代码运行报错的时候，就要重新加载，重新抓包，把最新的纯视频纯音频url替换进去
2.B站纯视频纯音频数据包的包名，也是动态变化着的
"""