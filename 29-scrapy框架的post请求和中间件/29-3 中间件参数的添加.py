"""
Cookie:
三种方法:手动登录之后，拿着登录过后的cookie
    --1.全局cookie的，settings.py，COOKIES_ENABLED = False，在DEFAULT_REQUEST_HEADERS添加登录过后的cookie,为字符串的形式，可以直接复制network里面的

    --2.每一个请求对象，单独设置Cookie,settings.py，COOKIES_ENABLED = True，cookie值不能再使用字符串，而是要以键值对字典的形式存在

    --3.下载器中间件里面去添加cookie

想要中间件生效，就需要到settings.py里面去进行配置

User-Agent:
下载器中间件的配置

代理IP

跳转Referer
"""



"""
复制过来的cookie，如何构造字典
"""
str_ = 'bid=3S5DolklESI; ll="118267"; _vwo_uuid_v2=D3EBE0F7503441D3959402C3D71EEFF0B|4519ecc1b3f605c6b3697a14afd4a59b; _ga=GA1.1.313176198.1627969259; _ga_RXNMP372GL=GS1.1.1635228400.1.1.1635228631.0; __gads=ID=b23142b8741ad35a-22d7870793ce0040:T=1628045181:RT=1636031363:S=ALNI_MYF8fqJxRCbH34B9ikAlBqa1r92rw; __yadk_uid=Rpl8jS0e38SKlLZxhLmR9Y05XHiVBxDg; douban-fav-remind=1; push_doumail_num=0; push_noty_num=0; gr_user_id=3fdfb9be-b87a-4cc3-912f-8f8b07904bd0; __utmv=30149280.23039; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; __gpi=UID=0000054e17920d2a:T=1652440669:RT=1656067139:S=ALNI_MacE_FArVxgYZLUPPx0fB49PDm03Q; dbcl2="235544536:kMI3acMtBFM"; ck=TzZ9; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1656074316%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_id.100001.4cf6=831bebd601806517.1627969259.184.1656074316.1656067175.; _pk_ses.100001.4cf6=*; __utma=30149280.313176198.1627969259.1656067139.1656074316.193; __utmb=30149280.0.10.1656074316; __utmz=30149280.1656074316.193.106.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.400287297.1627969259.1656067139.1656074316.181; __utmb=223695111.0.10.1656074316; __utmz=223695111.1656074316.181.96.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/'

# print(str_.split('; '))
# dict_ = {'bid':'3S5DolklESI'}
# dict_ = {}
# for i in str_.split('; '):   # 索引为0的部分是键值对的键名，而索引为1的部分是键值对的值
#     print(i)
    # print(i.split('='))
#     dict_[i.split('=')[0]] = i.split('=')[1]
# print(dict_)

# 字典推导式
dict_ = {i.split('=')[0]:i.split('=')[1] for i in str_.split('; ')}
print(dict_)