"""
基本语法：
    --1.每一个语句结尾，都使用分号作为结束符
    --2.mysql里面，sql语句是不区分大小写，大写也行，小写也行

约束：
主键：唯一标识这张表的字段
特点：不能重复，一个表只能有一个主键

外键：可以跟其它表建立关系的字段

区分：
varchar(n)和char(n)中的n表示字符的个数，并不代表字节个数，也就是说最多能存入n个字符(字母，中文，标点)

varchar(10):可变长度，最大可存储10个中文或者10个英文字母，10个标点
char(10):固定长度，不论你存储的数据是否达到了n个字符

重点：
创建数据表：
    --1.表名，不能以数字开头
    --2.在创建数据表的时候，一定要标明你所创建的这个字段是什么字段类型，否则会报错
    --3.两个字段之间要用逗号进行隔开，但最后一个字段不用逗号


insert:
1.自动增长的主键，全列插入的时候，通常使用数字0进行占位

update:
1.记得要加个where限定条件，否则会把这一列下所有的值都给修改了

delete:
1.记得要加个where限定条件，否则会把这一列下所有的值都给删除掉

2.drop和delete的区别
drop database 数据库名;    >> 彻底删除整个数据库
drop table 表名;           >> 彻底删除整个表
delete from 表名;          >> 清空整个表中的数据，但表的字段结构还存在
delete from 表名 where 条件;  >> 删除表中的某一行记录

结论：drop是彻底删除;delete是部分删除或者字段还在

逻辑删除: 数据在逻辑(表面)上是被删除了，但其实数据依然还在数据库中


"""





"""
一.创建表：
 create table hero(
     id int auto_increment primary key,
     name varchar(20) not null,
     age int default 0,
     sex varchar(20),
     score int
 )charset=utf8;

二.插入数据
insert into hero values
(0,'赵云',16,'male',97),
(0,'张飞',23,'male',95),
(0,'关羽',25,'male',95),
(0,'吕布',22,'male',99),
(0,'马超',17,'male',94),
(0,'典韦',24,'male',92),
(0,'张辽',23,'male',93),
(0,'貂蝉',17,'female',39),
(0,'洛神',19,'female',36),
(0,'许诸',22,'male',90),
(0,'孙策',24,'male',92),
(0,'周瑜',24,'male',56),
(0,'小乔',17,'female',36);

--查询表的所有数据
select * from hero;
select 字段名 as 别名 from 表名；  -- as可以省略


--给name取别名
--select name as '姓名' from hero;
--select name '姓名' from hero;


--select选项
All *: 默认的 保留所有的;
	select all * from 表名 [where条件] ;
	select * from 表名 [where条件] ;
	
select all * from hero;
select * from hero;

--Distinct: 去重复， 对查出来的结果会把重复的去掉。
select distinct 字段 from 表名 [where条件] ;
去掉重复年龄的
select distinct age from hero;

Group by : 分组的意思, 根据某个字段进行分组(相同的放一组,不同的分到不同的组)。
select 字段 from 表名 group by 字段;
根据性别分组
select * from hero group by sex;
--注意：分组查询以分组后的每一类所查找到第一条数据来作为显示

--统计函数
count(*)
统计总共有多少人
select count(*) from hero;

--统计男生和女生各有多少人
select sex,count(*) from hero group by sex;

--max(字段) 最大值
查询hero表里面年龄最大的人物
select max(age) from hero;

--查询男生和女生年龄最大分别是多少
select sex,max(age) from hero group by sex;

--min(字段) 最小值
查询hero表里面年龄最小的人物
select min(age) from hero;

--查询男生和女生年龄最小分别是多少
select sex,min(age) from hero group by sex;

--avg(字段) 平均值
查询hero表里面平均年龄
select avg(age) from hero;

查询男生和女生平均年龄
select sex,avg(age) from hero group by sex;

--sum(字段) 求和
查询hero表里面所有人物的年龄总和
select sum(age) from hero;

查询男生和女生的年龄总和
select sex,sum(age) from hero group by sex;

注意：count是计算表里面总共有多少数据，sum是求该字段值的总和
字符串比较大小按照首字母A-Z,越往后值越大
日期比较大小，越往后越大
"""