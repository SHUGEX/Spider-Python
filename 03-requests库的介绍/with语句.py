# f = open('sisi.txt','w')
# f.write('sisi,hello')
# f.close()

# with和编码格式
# with:代码执行完，系统会自动调用f.close()方法
with open('test.txt','w',encoding="utf-8") as f:   # 注意缩进！！！！
    f.write('思思是我女神')

print(f.closed)   # True 代表文件已关闭

