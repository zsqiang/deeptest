# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
本地没安mysql。。不要慌 用禅道的，哈哈h
"""
"""
算了，启动不了了

pymysql的基本使用说明：
1.import pymysql
2.构造连接实例：
conn = pymsql.connect(
    host="",
    prot=3306,
    user="",
    password="",
    db="",# 要连接的数据库名称
    charset="utf-8",# 应该要与数据库的编码一致，可以查看数据库的编码是什么，如果不是utf-8可以修改
)

3.创建交互对象：光标
cursor = conn.cursor()

4.构造要插入的数据
cursor.excutemany(sql, sql_data) # 批量执行
cursor.excute(sql) # 单条执行

5.提交数据(若进行了数据的更改)
conn.commit()

6.若不再执行数据的读取或插入或更改，则一定要关闭连接
conn.close()
"""
