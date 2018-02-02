# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
概述
    使用pymysql库进行MySQL的管理操作。
安装pymysql
    pip install PyMySQL
常用对象及API
    在pymysql中，提供了Connection和Cursor对象来管理操作MySQL。
常用对象
    Connection      代表一个与MySQLServer的socket连接，使用connect方法来创建一个连接实例
    Cursor          代表一个与MySQL数据库交互对象，使用Connection.Cursor()在当前socket连接上的交互对象
常用API
Connection对象常用的API
    connect()                   创建一个数据库连接实例
    begin()                     开始一个事务
    close()                     发送一个退出消息，并关闭连接
    commit()                    提交修改至数据库
    cursor()                    创建一个cursor实例
    ping()                      检测服务器是否在运行
    rollback()                  回滚当前事务
    select_db(db)               设置当前db
    show_warnings()             显示警告信息
Cursor对象常用API
    close()                     关闭当前cursor
    execute()                   执行一个sql语句
    executemany()               执行批量sql语句
    fetchall()                  提取所有数据
    fetchone()                  提取一条数据
'''
import pymysql
import random

if __name__ == "__main__":
    print("Python简单操作数据库示例")

    #创建一个连接实例
    conn = pymysql.connect(
        host = "10.68.3.88",# mysql服务IP地址，若服务在本机则用localhost
        port = 3306,# MySQL服务端口
        user = "liyiming",# 访问MySQL的用户名
        password = "liyiming",# 访问MySQL的密码
        db = "zzb_pro",# 默认连接到的数据库
        charset = "utf8"# 连接字符集
    )

    try:
        # 创建用于交互的cursor对象
        cursor = conn.cursor()

        # 先插入10条测试数据

        # 构建插入数据的sql
        sql = "INSERT INTO `users`(`email`,`password`) VALUES (%s,%s)"

        # 生成10条测试数据
        sql_data = []
        for index in range(0,10):
            email = "%.10f@126.com"%random.random()
            password = random.random()
            sql_data.append((email,password))

        # 执行sql，进行批量插入数据
        cursor.executemany(sql,sql_data)

        # 提交至数据库
        conn.commit()

        # 查询5条数据
        sql = "SELECT * FROM `user` LIMIT 5"

        # 执行sql
        cursor.execute(sql)

        # 取查询到的所有数据
        all_data = cursor.fetchall()

        # 遍历打印出来
        print("取所有查询到的数据")
        for data in all_data:
            print("id:%d,email:%s,password:%s"%(data[0],data[1],data[2]))

        #取一条数据
        one_data = cursor.fetchone()
        print("\n取1条数据")
        print("id:%d,email:%s,password:%d"%(one_data[0],one_data[1],one_data[2]))

    finally:
        # 最后把数据库连接关闭
        conn.close()