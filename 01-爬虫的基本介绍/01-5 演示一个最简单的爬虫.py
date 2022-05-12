# import requests
# from lxml import etree
#
# if __name__ == '__main__':
#     # 确认目标的url
#     url_ = "https://www.douyu.com/g_yz"
#
#     # 设置用户代理
#     headers_ = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
#
#     # 2.发送请求，获取响应
#     response = requests.get(url_,headers=headers_)
#
#     # 获取字符串类型的响应文本
#     str_data = response.content.decode()
#
#     # 转换成html对象
#     html_obj = etree.HTML(str_data)
#
#     # 获取页面中所有图片所在的li标签
#     item_list = html_obj.xpath('.//li[@class="layout-Cover-item"]')
#
#     # 循环遍历每个图片url以及图片名称所在的li标签
#     for i in item_list:
#         # 提取出图片的url
#         url = i.xpath('.//img[@class="DyImg-content is-normal"]/@src')
#
#         # 提取出图片的名称
#         name = i.xpath('.//h3/@title')
#
#         headers_ = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
#
#         # 对图片url发送请求
#         response = requests.get(url[0],headers=headers_)
#
#         # 4.保存图片
#         with open(f'X:/Image/{name[0]}.jpg','wb') as f:
#             f.write(response.content)
#
#         print(f'<<{name[0]}>>已经下载完成....')
