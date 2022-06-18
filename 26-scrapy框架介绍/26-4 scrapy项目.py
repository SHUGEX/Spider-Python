"""
1.安装 pip install scrapy -i https://pypi.doubanio.com/simple
    --重点:添加镜像源地址，可以自动下载需要配合的第三方库
2.安装完毕，终端输入命令 scrapy
    bench > 模拟框架项目运行起来大概是一个什么样子 log日志 > 运行起来的一些信息(配合时间)
    fetch > 添加一个url进行演示

3.手动创建一个新的爬虫项目
    --创建爬虫项目的命令 > scrapy startproject 项目名称
        --需要切换到爬虫项目中, cd 项目名称
        --需要输入命令去创建一个爬虫任务 scrapy genspider example(爬虫任务名称) example.com(范围域名)

"""