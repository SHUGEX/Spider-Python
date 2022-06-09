"""
演示百度翻译案例 --js的逆向解析：https://fanyi.baidu.com/?aldtype=16047#auto/zh
"""
"""
from: zh
to: en
query: 你好
transtype: translang
simple_means_flag: 3
sign: 232427.485594
token: 85b612d55f683458b86c1c84677a256d
domain: common

from: zh
to: en
query: 美女
transtype: translang
simple_means_flag: 3
sign: 551517.821612
token: 85b612d55f683458b86c1c84677a256d
domain: common

query: 你好 美女
sign: 232427.485594 551517.821612
"""


"""
分析过程：
1.全局搜索，由于携带sign的js文件过多，我们选择simple_means_flag进行搜索，
2.打上断点，启动程序，发现sign值疑似由一个I函数执行得到，参数为要被翻译的数据query
3.断点打在函数调用部分，这样可以进入函数看它的执行代码
4.右上角点击向下灰色箭头(F11)进入函数定义部分
5.函数内部，执行按右上角向右箭头(F9)
6.复制对应的js代码块，到本地文件(可以复制对应的部分，实在不行复制全部)    整体调整缩进:ctrl + a选中要调整缩进的代码，再按shift + tab
7.出现未知错误，可以对js代码进行一定程度的删减
8.报错i没有被定义:i is not defined
    --python 
    --js代码   >> 使用了i 却没有定义i
        --u的值跟i相关，极有可能就是i直接赋值，经过分析，发现确实u是由i直接赋值
            --动态数据(相对麻烦)，还是静态数据(十分好办，不会变化)
                美女 > 320305.131321201   你好 > 320305.131321201
            --i 是静态数据 不会变化，直接在js文件里面赋值，定义 
9.报错n没有被定义:n is not defined
    --js代码使用了n却没有定义
        --根据n的使用，判断n是函数的调用
        --经过调试，找到n函数的定义部分，复制过来
"""

import requests
import execjs
import jsonpath
import time

if __name__ == '__main__':
    while True:
        url_ = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

        headers_ = {
            'Cookie': 'PSTM=1627283384; BIDUPSID=E87874A693DB88716FD0E61C71073BCC; __yjs_duid=1_be57b8bfc8bffacdf8573b0697073d511627307214203; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BAIDUID=2CE6267F273BA693BF721A0F8EB54795:FG=1; MCITY=-158%3A; BDUSS=ZDVHNnfkxYNk9ESjVzTnJucS1iZldRMUxKOFc3cmVEYzF1Z09CTTJkbWVCN1JpRVFBQUFBJCQAAAAAAAAAAAEAAAC8Ped2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ56jGKeeoxiLV; BDUSS_BFESS=ZDVHNnfkxYNk9ESjVzTnJucS1iZldRMUxKOFc3cmVEYzF1Z09CTTJkbWVCN1JpRVFBQUFBJCQAAAAAAAAAAAEAAAC8Ped2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ56jGKeeoxiLV; BAIDUID_BFESS=2CE6267F273BA693BF721A0F8EB54795:FG=1; BDSFRCVID_BFESS=AZ_OJexroG0RT0bDroZVIGggZOGM4w5TDYLEOwXPsp3LGJLVgxPTEG0PtjJ5HU4bLrA9ogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJAj_D-btK03fP36qR6sMJ8thmT22-usQDjl2hcHMPoosIJ-353DQbDeWR7A0-bMyeOx2Cb5JxbUoqRHLn5AKhIqbNJi2U5p55bT-p5TtUJMjlFGyh_M-xAXLHryKMniBIj9-pnMWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuD6-2j63yDNts5JtXKD600PK8Kb7VbpjLBUnkbJkXhPtjQq0jKenHWMcCWl3JeUcOQUFM5TL7Qbrr0xRfyNReQIO13hcdSR390hOpQT8r5M6ZtxvPJIrrQqDXab3vOpRzXpO1KMPzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqtJHKbDJ_KLXJfK; ZFY=edWl72TVdsN63OUxMH9UQUgFwnQFNIY5qvSwzZvFZ6Y:C; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=z7cfglbcves&ss=l3valusr&sl=2&tt=1n7&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=6p8t&ul=8dbr&hd=8dcr"; BA_HECTOR=a40l2420012k0l80a41h9r7gf15; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; delPer=0; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1654498677; APPGUIDE_10_0_2=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1654511981; ab_sr=1.0.1_ODI4OTAzZTRiM2UyNjlkM2NiYTg2YjViYjgzN2M0NWJkODc4MTE5NmYwNzY0NDNiZTRkZDkwYmMwNjVjYzlkNzc5YjZiMzFlMGI1ZjI4YWRlMTViZjYzMDI3ZmZmNDg1OTcxNTkzZDUyNDE5MTViMTViNThiMmExOTMxOGVjNjA3Yjk2MTRiZWJkNTk0ZjdkMjc1MmFmMzY1MzJjMzg5YjBkYzc1ZjI3N2ZiNTQ3MDY0ZjU1NGY1NjhmZjViNzll; H_PS_PSSID=36426_36554_36455_31660_36452_36420_36167_36488_36518_36074_26350_36467_36315',
            "Referer": "https://fanyi.baidu.com/?aldtype=16047",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
        }

        # 构造表单数据
        # 1.要被翻译的数据
        data_ = input('请输入要被翻译的中文:')

        # 打开js文件，得到里面的js代码
        with open('baidu_.js','r') as f:
            js_data = f.read()

        # 实例化对象
        js_obj = execjs.compile(js_data)

        # 执行js代码，得到返回数据
        sign_data = js_obj.call('e',data_)

        # 2.sign值
        sign_ = sign_data
        # print(sign_)

        form_data = {
            "from": "zh",
            "to": "en",
            "query": data_,
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": sign_,
            "token": "85b612d55f683458b86c1c84677a256d",
            "domain": "common"
        }


        response_ = requests.post(url_,headers=headers_,data=form_data)
        py_data = response_.json()
        # print(py_data)

        # 解析
        res_ = jsonpath.jsonpath(py_data,'$..dst')[0]

        print(f'翻译结果为:{res_}')

        time.sleep(1)