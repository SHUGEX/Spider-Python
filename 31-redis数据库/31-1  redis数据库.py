"""
redis安装注意点
    --有道翻译去翻译一下
    --尽量默认安装路径
    --path一定要记得勾选 ，添加到环境变量当中
"""

"""
mysql数据库  > 关系型数据库
redis,mongodb  > 非关系型数据库
"""


"""
redis的特点 > 读写速度很快 基于运行内存的数据库
数据以键值对的方式进行保存  key:value
redis key > 字符串的形式
python > value int str list set dict 
redis > value  str hash(键值对对象)  list set(无序) zset(有序集合)
"""

"""
怎么查看redis的运行状态
1.进入任务管道器进行查询 
2.win + r > services.msc
3.开启办法 进入安装路径  redis-server redis.windows.conf
"""


"""
进入redis数据库 redis-cli
# IP:端口
127.0.0.1:6379> 成功进入 
退出> ctrl + c  quit exit 右上角的X
"""



"""
查询：
--keys * > 查看所有的数据
--exists key > 查询特定的键值对，结果返回为1或者0
--type key > 查询类型
--del key > 删除 
--expire key time > 已经存在的数据添加有效期
--ttl key > 查询有效期
--flushall > 清空
"""

"""
字符串类型string:    {'name1':'sisi1'}
保存单条数据：set key value 
得到值:get key 
设置有效期：setex key time value   类似验证码有效期
保存多条数据：mset key1 value1 key2 value2 key3 value3 
添加数据:append key value   
    --没有就新建，有就追加，类似读写模式里面的w跟a的关系 
获取多个值：mget key1 key2 key3 
"""

"""
hash 哈希  {sisi1:{'age':'18'}}
保存单条数据:hset key field value 
得到值：hget key1 field 
设置多个：hmset key1 field1 value1 field2 value2   {sisi1:{'age':'18','height':'180'}}
查询都有哪些字段: hkeys key 
获取多个字段对应值:hmget key field1 field2 
删除:hdel key field1 field2  可多个
"""

"""
列表：push 
lpush>left   rpush>right
往左边放(把一个值插入到已存在的列表头部):lpush key1 value1 value2 value3   后放的在左边
往右边放(把一个值插入到已存在的列表尾部):rpush key1 value1 value2 value3   后放的在右边
查看：lrange key start stop 
往特定部分前面插入数据：linsert key before value new_value
往特定部分后面插入数据：linsert key after value new_value
修改特定索引部分:lset key index new_value
删除: lrem key count value 
"""



"""
集合set: 数据具体唯一无序性，无法修改
添加数据:sadd key value1 value2 value3  
获取:smembers key 
删除:srem key value.... 可以单个  也可以多个
"""

"""
有序集合：zset 顺序的排序是依靠权重 > 权重score值越小，越靠前
添加数据:zadd  key score1 member1  score2 member2  score3 member3 
查看:zrange key start stop  
获取权重值:zscore key member

根据权重取value: zrangebyscore key score1 score2
删除：zrem key value1 value2 
"""