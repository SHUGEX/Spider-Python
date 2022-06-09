"""
1.解析js的加密参数
sign = md5的加密

2.有些加密参数，是经由js代码里面的函数调用
函数的嵌套
函数的定义
js代码过多，解析困难，利用python代码模仿执行困难

分析:既然我们要的参数是由js代码运行生成的
    那么直接把js的代码拿过来运行，得到参数
"""


"""
目标:执行js的代码
1.需要 node.js
    --https://blog.csdn.net/weixin_45081575/article/details/105223948  根据电脑版本 官网下载，解压 安装
    --路径添加到系统环境变量  node -v 
    --需要是专业版本的pycharm > professional
        --settings > plug-in > 搜索NodeJS 安装即可
        --settings > Languages & Frameworks > Node.js and NPM > 配置好前边安装的node.exe的绝对路径即可
        
重启pycharm
"""

