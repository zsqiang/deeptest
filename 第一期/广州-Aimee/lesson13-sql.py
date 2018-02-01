# coding=utf-8


import pymysql #导入数据驱动
import pymysql.cursors

# 连接数据库 创建一个连接实例
conn = pymysql.connect(
    host='192.168.1.201',  #服务器ip地址
    port=3306,
    user='root',
    passwd='leihou888;',
    db='oola-uat',
    charset='utf8',  #指定编码方式,
    cursorclass = pymysql.cursors.DictCursor
)
# 默认返回的是元祖类型
# 获取查询数据：cursor.fetchone()获取剩余结果的第一行数据，
# cursor.fetchmany(3)获取剩余结果的前3行数据，
# cursor.fetchall()获取剩余结果的所有数据
cur  =conn.cursor()
sql = 'SELECT username FROM star_manager '
cur.execute(sql)
r = cur.fetchmany(2)
print (r)


try:
    #创建交互cursor对象
    cursor = conn.cursor()
    #插入10条数据
    sql = ""






