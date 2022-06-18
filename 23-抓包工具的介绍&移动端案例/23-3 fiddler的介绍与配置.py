"""

独立的抓包工具(应用程序)
"""

"""
fiddler的安装以及配置：https://www.cnblogs.com/yyhh/p/5140852.html
安装完毕之后 
配置:
    --1.如何开启，快捷键F12,左下角如果是空白，表示关闭抓包，点击一下左下角出现Capturing，那么就表示开启抓包
    --2.找到工具栏的Tools,里面的第一个选项options
    --3.点击了options之后，选择HTTPS这个选项，勾选Decrypt HTTPS traffic(为了能够获取https一些请求)，最后点击OK
        第一次勾选，会让你安装证书
        
    为了获取移动端(手机端)的数据
    --4.选择Connections 勾选 Allow remote computers to connect(为了能够获取移动端的数据)，最后点击OK
    之后重启抓包工具fiddler
"""


"""
手机 > 抓包工具(fiddler) > 服务器 
它们处于同一个网络环境之下(有联系)


虚拟机 > 电脑
手机模拟器 > 手机
"""


"""
目的：抓取移动端(手机)的数据
1.电脑(装有抓包工具fiddler)开启热点，让我们真正的手机连接这个电脑热点
2.下载一个虚拟的手机(手机模拟器)
    --安卓手机模拟器
    --模拟器的配置
        --1.得知道我们电脑的IPV4地址
        --2.按住WLAN不动，出现'修改网络' >> 填入电脑的IP地址以及fiddler的端口号8888
            (所有手机端的网络请求都会经过这个端口为8888的抓包工具fiddler)
        --3.进入浏览器，访问172.16.20.40(以自己电脑IP为准):8888
            安装证书FiddlerROOT 设置锁屏密码，才能生效

3.此时此刻你的抓包工具fiddler就可以获取到你的手机模拟器(手机)发送请求以及数据 

注意！！
1.fiddler和mumu必须同时打开，如果只打开mumu不打开fiddler,会出现mumu浏览器访问不了的情况 
2.如果网络环境发生变化(IP发生变化),需要重新去mumu配置网络并安装新的证书
    
"""