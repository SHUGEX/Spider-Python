# 下载一个第三方库 PyExecJS      pip install PyExecJS -i https://pypi.doubanio.com/simple

import execjs

# 1.使用文件的读写拿到js文件里面的代码
with open('demo.js','r') as f:
    js_data = f.read()

# 2.拿到js代码时候，需要进行一个类似编码的操作
js_obj = execjs.compile(js_data)

# 3.执行js代码
res_ = js_obj.call('add',4,6)

print(res_)