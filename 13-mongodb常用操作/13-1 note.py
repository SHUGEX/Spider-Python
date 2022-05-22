

"""
进入命令：mongo
1.数据库操作：
显示所有的数据：show dbs 默认三个：admin config local

创建/切换数据库：use 数据库名   空数据库没有显示

创建集合：db.createCollection('集合名称')   C必须大写

删除当前所用的数据库：db.dropDatabase()

2.集合操作
查看集合：show collections
删除集合：db.集合名.drop()      db.s1.drop()  返回为true代表删除成功


3.文档操作
3.1 添加文档：键值对的形式
如果不指定_id参数，mongodb会为文档分配一个唯一的objectid

db.集合名称.insert({键值对})
db.s1.insert({name:'雪锐'})
db.s1.insert({"_id":1,name:"叶子",age:18})

添加多条文档
db.s1.insert([
... {_id:2,name:'冰冰',age:20},
... {_id:3,name:'苏苏',age:16},
... {_id:4,name:'恣意',age:22}])



3.2 查询 文档
db.集合名称.find()
查询全部：db.s1.find()
根据某一项查询: db.s1.find({name:'冰冰'})
格式化显示：db.s1.find().pretty()   数据超过长度会进行美化


3.3 噩梦条件
and : 条件都要符合才能查询出来
db.s1.find({$and:[{name:'苏苏'},{age:16}]})})

or:只要符合条件都查询出来
db.s1.find({$or:[{name:'苏苏'},{age:18}]}))


and,or混用
({$or:[{$and:[{},{}]},{$and:[{},{}]}]})


db.s1.find({
    $or:[
        {$and:[{name:'zs'},{age:18}]},
        {$and:[{name:'ls'},{age:20}]}
        ]
        })



操作符的使用：
$gt
db.s1.find({age:{$gt:18}})

3.4 修改文档
db.s1.update({原内容},{新内容})
db.s1.update({name:'恣意'},{name:'rose'}) 整条数据都会被修改
指定修改属性：set后面是修改的值
db.s1.update({name:'苏苏'},{$set:{name:'susu'}})

更新所有满足条件的文档:{multi:true}
db.s1.update({age:20},{$set:{age:40}},{multi:true})



3.5 删除文档
删除指定条件的文档：db.s1.remove({name:'叶子'})
只删除满足条件的第一条文档:{justOne:true}
删除所有文档：db.s1.remove({})


交互
mongodb跟python交互

安装模块:pip install pymongo
"""



