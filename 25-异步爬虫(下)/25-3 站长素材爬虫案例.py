import asyncio
import aiohttp
import time
import random
from lxml import etree
from fake_useragent import FakeUserAgent

t1 = time.time()


class  ZZ_Class:
    def __init__(self):
        self.url = "https://sc.chinaz.com/tupian/"
        self.headers = {'User-Agent':FakeUserAgent().random}
        self.page = 1   # 控制翻页

    async def SendRequest_Index(self):
        # 如果异步任务中遇到上下文管理器 with....as   95%的情况都需要在最前面加上async关键字
        # 不加的情况-> with ....open()as
        async with aiohttp.ClientSession() as session:  # session->requests.session
            # 请求方式：get/post/delete  与requests一致
            # post(data=data,params)
            # 不同：代理IP的使用
            # requests-->代理IP的使用 -->{'https':'http://ip:port'}-->proxies
            # aiphttp-->代理IP的使用 -->'https://IP:port' -->proxy
            async with await session.get(self.url,headers=self.headers) as response:
                # 字节内容(二进制数据)-->response.read()
                # json --> response.json()
                text_data = await response.text()   # 获取响应文本内容
                # print(text_data)
                return text_data
                # response.status   # 获取响应状态码

    async def GetDataImg(self):
        """解析图片的标题以及所在的url地址"""
        index_text = await self.SendRequest_Index()
        await asyncio.sleep(random.randint(1, 3))
        tree = etree.HTML(index_text)
        title_list = tree.xpath('//*[@id="container"]/div[*]/div[1]/a/img/@alt')
        src_list = tree.xpath('//*[@id="container"]/div[*]/div[1]/a/img/@src')
        urls = []
        for v in src_list:
            url = 'https:' + v
            urls.append(url)
        res = dict(zip(title_list,urls))
        print(res)
        return res

    async def download_img(self,url):
        """向图片所在的url发起请求，以获取图片的字节(二进制)数据"""
        async with aiohttp.ClientSession() as session:
            async with await session.get(url,headers=self.headers) as response:
                content_ = await response.read()
                return content_

    async def Save_Img(self):
        dic_img_data = await self.GetDataImg()
        await asyncio.sleep(random.randint(1,3))
        for k,v in dic_img_data.items():
            content_ = await self.download_img(v)
            with open('imgs/' + k + '.jpg','wb') as f:
                f.write(content_)
        # 当上方循环结束，意味着一页的图片全部爬取完毕
        self.page += 1
        self.url = 'https://sc.chinaz.com/tupian/index_%s.html' % self.page
        if self.page <= 3:
            return await self.Save_Img()


if __name__ == '__main__':
    t = ZZ_Class()
    task = asyncio.ensure_future(t.Save_Img())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    t2 = time.time()
    print('程序运行总耗时为:',t2-t1)