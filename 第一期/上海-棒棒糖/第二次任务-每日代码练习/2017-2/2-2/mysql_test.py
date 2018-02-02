# 导入 MySQL 驱动:
import mysql.connector
# 注意把 password 设为你的 root 口令:
conn = mysql.connector.connect(user='root', password='password',database='test')
cursor = conn.cursor()
# 创建 user 表:
cursor.execute('create table user (id varchar(20) primary key, namevarchar(20))')
# 插入一行记录，注意 MySQL 的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1','Michael'])
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ['1'])
values = cursor.fetchall()
print(values)
# 关闭 Cursor 和 Connection:
cursor.close()
conn.close()

