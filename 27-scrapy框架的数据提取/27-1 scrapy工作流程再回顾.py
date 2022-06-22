"""
scrapy工作流程原理：
1.由爬虫器确认起始url,构造一个request对象，交给引擎
2.引擎把request对象交给调度器，是一个队列，相当于一个容器(先进先出，后进后出)，排序的功能
3.调度器把排序之后的request对象发送给引擎
4.引擎把request对象交给了下载器
5.下载器拿了request对象发送了网络请求，获得了响应对象response,交给引擎
6.引擎把响应response交给了爬虫器
7.爬虫器拿到了response进行解析：
    --(1) 如果直接保存的数据data，返回给引擎之后，那么引擎就交给了管道
    --(2) 是需要继续发送请求的url,返回给引擎之后，把之前的流程再走一遍
8.管道拿到了由引擎发送过来的数据data,直接进行保存


看上去很麻烦，但是很多部分都是自动完成的
哪些部分是手动完成的
    --(1)起始url的确认
    --(2)解析逻辑
    --(3)保存
"""



"""
爬虫项目的创建
    -- scrapy startproject Douban
    -- cd 进入项目根目录，然后scrapy genspider movie movie.com
    
    
    
启动爬虫:
    --1.需要先确认路径处于项目的根目录
    --2.scrapy crawl 爬虫任务名称
    屏蔽调试信息：scrapy crawl 爬虫任务名称 --nolog
    当你运行爬虫程序，没有出现想要的效果，千万不要加上--nolog去屏蔽掉log信息
    
数据提取
    --方法有4种，2种类型，只需要学习其中2种就可以了
        --extract() > 取出所有的数据，以列表的方式呈现 
        --extract_first() > 得到第一条数据
        --get() > 得到第一条数据
        --getall() > 取出所有的数据，以列表的方式呈现 
        

数据的保存：
    --需要以items对象为载体，进行保存
        pipelines是一个仓库，它只允许以items对象为载体的数据进行保存
    --yield items_对象给了pipeline管道 ，管道需要进行接收
    
管道pipeline > 需要在settings里面开启
    --里面已经自动生成了一个方法，处理items对象
    --为什么需要添加方法：
        --创建文件,只需要最开始执行一次           open_spider   > __init__
        --然后保存                              process_item
        --最后关闭文件对象，只需要在最后执行一次   close_spider  > __del__
"""





"""
目的:
获取到电影名称
获取一个评分


想要获取2个数据，需要先在items文件当中设置2个字段
"""




"""
[<Selector xpath='//a/span[@class="title"][1]/text()' data='肖申克的救赎'>, <Selector xpath='//a/span[@class="title"][1]/t
ext()' data='霸王别姬'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='阿甘正传'>, <Selector xpath='//a/span[
@class="title"][1]/text()' data='泰坦尼克号'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='这个杀手不太冷'>
, <Selector xpath='//a/span[@class="title"][1]/text()' data='美丽人生'>, <Selector xpath='//a/span[@class="title"][1]/text
()' data='千与千寻'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='辛德勒的名单'>, <Selector xpath='//a/span
[@class="title"][1]/text()' data='盗梦空间'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='星际穿越'>, <Sele
ctor xpath='//a/span[@class="title"][1]/text()' data='忠犬八公的故事'>, <Selector xpath='//a/span[@class="title"][1]/text(
)' data='楚门的世界'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='海上钢琴师'>, <Selector xpath='//a/span[
@class="title"][1]/text()' data='三傻大闹宝莱坞'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='机器人总动员
'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='放牛班的春天'>, <Selector xpath='//a/span[@class="title"][1
]/text()' data='无间道'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='疯狂动物城'>, <Selector xpath='//a/sp
an[@class="title"][1]/text()' data='大话西游之大圣娶亲'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='熔炉'
>, <Selector xpath='//a/span[@class="title"][1]/text()' data='控方证人'>, <Selector xpath='//a/span[@class="title"][1]/tex
t()' data='教父'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='当幸福来敲门'>, <Selector xpath='//a/span[@c
lass="title"][1]/text()' data='触不可及'>, <Selector xpath='//a/span[@class="title"][1]/text()' data='怦然心动'>]


肖申克的救赎 泰坦尼克号 
"""