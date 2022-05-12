"""
网易云 一张图片
"""

# 导入发送网络请求的第三方库requests
# import requests
#
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "https://p1.music.126.net/7AXhBlJt3IIxnuGCUHO1cA==/109951167334756850.jpg?imageView&quality=89"
#
#     # 设置用户代理
#     headers_ = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#
#     # 2.发送请求，得到响应对象
#     response_ = requests.get(url_,headers=headers_)
#
#     # 作为图片，肯定不会是str类型的文本数据,二进制
#     bytes_data = response_.content
#
#     # 3.解析数据
#     # 4.保存
#     with open('LISHALI.jpg','wb') as f:
#         f.write(bytes_data)




"""
网易云 一首非VIP歌曲的下载  >> mp3
"""
# import requests
#
# if __name__ == '__main__':
#     # 1.确认目标的url
#     url_ = "https://m704.music.126.net/20220425210511/6ce2af42298651a6bfafd35fa5f730f1/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096412447/234c/3183/e57c/43880c3836ea3096ead226282d94cf15.m4a?authSecret=0000018060bc8d0b06ca0aa463782415"
#     # url_ = "https://m701.music.126.net/20220425204656/7300c1da0b5ca3bb3cd7d8264c559cb6/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096412004/9fa2/d449/33b6/f88ff9ed4a6ef5a3a12faadcfd632b30.m4a"
#
#     # 设置用户代理
#     headers_ = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
#     }
#
#     # 2.发送请求
#     response_ = requests.get(url_,headers=headers_)
#     bytes_data = response_.content
#
#     # 4.写入
#     with open('美人鱼.mp3','wb') as f:
#         f.write(bytes_data)
# 二进制文件，除了图片可以在pycharm直接双击打开外，mp3还有mp4这种音频视频文件是不能直接在pycharm双击打开，而要在文件夹当中打开
# 如果mp3文件打不开，尝试使用别的播放打开

"""
拿到了url之后
发送网络请求，得到该url对应的响应数据
"""




import requests

if __name__ == '__main__':
    url_ = "https://vodkgeyttp8.vod.126.net/cloudmusic/MCRgMDE0MCMxITIxJDA1Ig==/mv/394037/f77060af07a7d0ad7d3ce9972f99356c.mp4?wsSecret=77a9eda26b7082e0cb3febb045f14423&wsTime=1650890926"
    # url_ = "https://vodkgeyttp8.vod.126.net/cloudmusic/MTI5MDc0OTc=/056900585921c79409acf1b150ea6fa8/001daaba60286411fbb95749f442b240.mp4?wsSecret=1bf6f3dd981bbb098eb5961cb8807648&wsTime=1650890655"

    # 设置用户代理
    headers_ = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }
    response_ = requests.get(url_,headers=headers_)

    bytes_data = response_.content

    with open('那些年你很冒险的梦.mp4','wb') as f:
        f.write(bytes_data)
