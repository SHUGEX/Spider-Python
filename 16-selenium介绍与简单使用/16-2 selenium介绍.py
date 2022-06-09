"""
selenium    pip install selenium==3.141.0 -i https://pypi.doubanio.com/simple
1.下载chromedrier插件：https://chromedriver.storage.googleapis.com/index.html

2.查询自己的浏览器版本 >> 101.0.4951.64
3.找到版本对应(最相近)的安装包
    --如何关闭谷歌浏览器自动更新：https://blog.csdn.net/weixin_45755465/article/details/123373290
    --win+r>输入 services.msc>找到Google更新服务> 双击>启动类型选择'禁用' > 点击'应用' > 点击'确定'
4.根据电脑系统版本选择下载
5.解压得到exe文件
6.复制chromedriver.exe文件到python解释器同一目录之下：D:\software\python_w
"""

"""
Selenium是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，
Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器），
可以接收指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏
"""
"""
web:网站  测试(工作岗位)
点击事件:鼠标点击 触发js
可以绕过js
可以绕过 js触发的请求过程  直接获取到数据 
selenium > 浏览器
爬虫代码：解析 得到js的数据
selenium去点击页面 利用代码 模拟浏览器 使用鼠标去点击的操作

selenium就是可以 利用python代码控制浏览器去做一些事情的工具 > 点击某个按钮 
需要一个驱动去启动浏览器 chromedriver
"""