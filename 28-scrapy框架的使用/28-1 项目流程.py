"""
1.项目创建 -- scrapy startproject 项目名称

2.cd 到项目的根目录

3.创建爬虫任务-- scrapy genspider 爬虫任务名称  域的范围.com

4.启动爬虫 -- scrapy crawl 爬虫任务的名称

5.屏蔽爬虫开启后的log日志 -- scrapy crawl 爬虫任务的名称 --nolog

6.数据的保存
    --item   是一个载体 对象 以键值对的方式存在数据
    --pipeline 是一个仓库 它只来自item这个载体携带的数据   默认是关闭的，需要到settings里面开启
"""