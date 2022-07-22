# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class DoubanPipeline:
    """处理items对象拿过来的数据"""
    def __init__(self):
        self.file_ = open('douban_12.json','w',encoding="utf-8")
        print('文件打开了....')

    def process_item(self, item, spider):
        """item接收的就是爬虫器丢过来的items对象"""
        py_data = dict(item) # 先把携带键值对数据items对象转化为字典
        json_data = json.dumps(py_data,ensure_ascii=False) + ',\n'
        self.file_.write(json_data)
        print('写入了一条数据>>>>')
        return item  # 先不用管

    def __del__(self):
        self.file_.close()
        print('文件关闭了....')
