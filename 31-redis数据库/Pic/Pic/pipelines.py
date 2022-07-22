# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import hashlib

from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
# 这是普通的pipepline
from scrapy.utils.python import to_bytes


class PicPipeline:
    def process_item(self, item, spider):
        return item
# 图片pipeline
# 自定义图片管道，以此来达到修改默认文件夹以及图片名称的效果,千万不要忘记去settings.py进行注册，让它生效
class DoubanPicPipeline(ImagesPipeline):
    # 拿到item对象里面的图片名称数据
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u,meta={'sisi':item}) for u in urls]    # 传递item对象

    # 完成重写
    def file_path(self, request, response=None, info=None, *, item=None):
        # image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        item_ = request.meta.get('sisi')
        name_ = item_['name']
        # 修改默认文件夹名称
        return f'xuerui/{name_}.jpg'
