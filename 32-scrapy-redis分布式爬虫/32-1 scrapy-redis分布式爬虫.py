"""
scrapy-redis分布式爬虫
"""
# requests > 达到了一定的数据量 > scrapy > scrapy-redis
"""
什么是分布式爬虫:(分开部署方式的爬虫)
    --多个服务器(电脑)一起去运行同一个爬虫项目
    --为什么要多个服务器一起去运行同一个爬虫项目 > 数据量极大的情况下
    
    
    --scrapy-redis只是对原有的scrapy项目进行了修改，让其可以多台服务器一起操作一个项目，达到分布式的效果
    
    
    调度器的本质是一个队列，100个requests请求对象，都需要经过调度器的入队列，出队列操作
    排序之后，再给下载器发送请求，获取响应
    
    一台服务器：那么调度器里面的100个requests请求对象，就只能给一台服务器去发送网络请求
    四台服务器：          100个requests请求对象，可以四台服务器一起去发送网络请求
    这就是分布式爬虫，能够提高效率的道理 
    
    问题：调度器如何把这100个requests请求对象分给四台服务器去做，不重复呢
    
    共享资源的问题：
        --多线程，在同一个文件之内，可以共享资源 
        --多进程，并不是在同一个文件之内，是在同一台电脑(服务器)，共同拥有一个运行内存
            通过在内存中创建队列
        --分布式爬虫：多台电脑，100个requests请求对象，利用的是互联网
                    依靠的是redis数据库
                    
                    100个requests请求对象都放到redis数据库里面，多台电脑进行访问，就完成了任务的分发
                    也就实现了多台服务器共同运行同一个爬虫项目的目的，实现了分布式爬虫
                    把redis数据库部署到云服务器上面，多台电脑都可以进行访问
"""
"""
总结：
主服务器(Master):redis数据库    100个requests请求对象
A从服务器(Slave)    25
B从服务器(Slave)    25
C从服务器(Slave)    25
D从服务器(Slave)    25

有同一份爬虫代码
调度器需要替换成redis数据库，这样才能够进行，100个requests请求对象的分发

无论是request,还是scrapy,还是scrapy-redis
url的确认  start_url 
随机指定一台A从服务器去start_url发送请求获取响应 
100个url 构造100个requests请求对象
100个requests请求对象给了redis数据库
A拿到了25份数据
B拿到了25份数据
C拿到了25份数据
D拿到了25份数据

如果想要汇总数据，怎么办呢    redis替换掉pipeline 

scrapy-redis > 使用redis替换掉分发任务的调度器，和进行保存的管道pipeline 
这样的话，就可以跟多台服务器进行数据的交互 
"""


"""
redis把这个调度器和管道替换掉之后，主要完成了三件事情:

1.保存request请求对象，然后分配给各个服务器去进行运行    >  "movie:requests"
2.保存item对象，保存数据                              >  "movie:items" 
3.任务的去重，以及断点续爬(由于不可搞力的关系，在哪里停止了，下次就在哪里开始)  > "movie:dupefilter"
"""

"""
如何使用scrapy-redis  
pip install scrapy_redis  -i https://pypi.doubanio.com/simple
只是在原有的scrapy上面去进行修改即可




ABCD 
一起运行爬虫任务 
一起进入监听状态(卡住)
"""