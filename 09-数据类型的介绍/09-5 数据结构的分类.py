"""
演示数据结构的分类
"""
# 图片 视频

"""

字符串类型(文本类型的数据)，数据提取
html
json

爬虫抓取的文本数据，一般就2种
结构化数据:
结构比较规范
json xml(极其的稀少)

json格式数据的特点:
1.最外层要么是一个列表一样的[],要么是一个字典一样的{}
2.json数据的引号必须是双引号
3.末尾元素，不写逗号
4.没有注释

作用：填充网页
提取json类型的数据，需要一个第三方库，jsonpath
pip install jsonpath -i https://pypi.doubanio.com/simple

xml:跟html十分的相像，但是结构更加的严谨


非结构化数据
html
xpath解析
正则:效率高，但难度大 
xpath
bs4：难度小，但是效率较低
html
json
"""
"""
数据提取
json >> jsonpath
html >> xpath python里面用lxml这个库去实现xpath语法
        pip install lxml -i https://pypi.doubanio.com/simple
"""

"""
xml跟html的区别
1.xml是严谨的结构化数据

2.xml数据的容器，作用仅仅是保存数据，是一个数据的载体

3.html是一种呈现方式
"""