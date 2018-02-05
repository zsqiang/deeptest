# 导入 SQLite 驱动:
import sqlite3
# 连接到 SQLite 数据库
# 数据库文件是 test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个 Cursor:
cursor = conn.cursor()
# 执行一条 SQL 语句，创建 user 表:
cursor.execute('create table user (id varchar(20) primary key, namevarchar(20))')
# 继续执行一条 SQL 语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\',\'Michael\')')
# 通过 rowcount 获得插入的行数:
cursor.rowcount
# 关闭 Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭 Connection:
conn.close()
#查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', '1')
# 获得查询结果集:
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
要确保打开的 Connection 对象和 Cursor 对象都正确地被关闭，否则，资
源就会泄露。
使用try:...except:...finally:...可确保出错的情况下也可以关闭掉 Connection 对象和 Cursor 对象