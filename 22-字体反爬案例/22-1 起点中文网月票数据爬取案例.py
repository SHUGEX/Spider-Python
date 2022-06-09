"""
目标:
爬取起点中文网的月票榜 小说名:月票数
"""
"""
分析过程:
    --1.数据是什么类型 json html
        --(1)书名有了，先获取书名
"""

import requests
from lxml import etree
import re
from fontTools.ttLib import TTFont
if __name__ == '__main__':
    # 1.目标url
    url_ = "https://www.qidian.com/rank/yuepiao/"

    # 设置请求头
    headers_ = {
        "Cookie": "e1=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C45%22%2C%22l1%22%3A5%7D; e1=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C45%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C45%22%2C%22l1%22%3A5%7D; newstatisticUUID=1628649841_641773021; _csrfToken=Z0ePL0OFXaWOMCfWxGnAxeZ4takdOPOOsWI5ujQ3; fu=2036299009; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; rcr=1031587468; lrbc=1031587468%7C683757380%7C0; _yep_uuid=53c81390-52ee-85d9-d741-a09b4faa7dfa; Hm_lvt_f00f67093ce2f38f215010b699629083=1654671787; _gid=GA1.2.641443816.1654671787; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%2C%22l1%22%3A3%7D; _ga_FZMMH98S83=GS1.1.1654689836.70.1.1654689840.0; _ga_PFYW0QLV3P=GS1.1.1654689836.70.1.1654689840.0; Hm_lpvt_f00f67093ce2f38f215010b699629083=1654689841; _ga=GA1.2.816902508.1628649841",
        "Referer": "https://www.qidian.com/rank/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    # 发送请求，得到主页面的响应
    response_ = requests.get(url_,headers=headers_)
    str_data = response_.text    # 得到html格式的字符串数据


    # 获取书名的xpath语法  >> //h2/a/text()
    html_obj = etree.HTML(str_data)
    title_list = html_obj.xpath('//h2/a/text()')
    print('书名列表title_list:',title_list)

    # 获取月票数据
    # poll_list = html_obj.xpath('//span[@class="OhpHUOcw"]/text()')
    # print('月票数据列表为poll_list:',poll_list)


    # 用字符串得到，用正则解析字符串类型的html格式的数据
    poll_list = re.findall(r'</style><span class=".*?">(.*?)</span></span>月票</p>', str_data)
    print('月票数据密文列表poll_list:',poll_list)
    # 获取字体加密数据包(以woff为后缀的url)
    res_ = html_obj.xpath('//p/span/style/text()')[0]
    font_url = re.findall(r"format\('eot'\); src: url\('(.*?)'\) format\('woff'\)",res_)[0]
    print('字体加密文件的url:',font_url)