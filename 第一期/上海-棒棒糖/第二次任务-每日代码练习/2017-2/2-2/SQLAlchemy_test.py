# 创建的 user 表
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
# 定义 User 对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
# create_engine()用来初始化数据库连接,'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine =create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建 DBSession 类型:
DBSession = sessionmaker(bind=engine)
'''
如果有多个表，就继续定义其他 class，例如 School：
class School(Base):
__tablename__ = 'school'
id = ...
name = ...
'''

#向数据库表中添加一行记录
# 创建 session 对象:
session = DBSession()
# 创建新 User 对象:
new_user = User(id='5', name='Bob')
# 添加到 session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭 session:
session.close()

#从数据库表中查询数据
# 创建 Session:
session = DBSession()
# 创建 Query 查询， filter 是 where 条件，最后调用 one()返回唯一行，如果调用 all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的 name 属性:
print('type:', type(user))
print('name:', user.name)
# 关闭 Session:
session.close()

#定义一对多关系
class User(Base):
__tablename__ = 'user'
id = Column(String(20), primary_key=True)
name = Column(String(20))
# 一对多:
books = relationship('Book')
class Book(Base):
__tablename__ = 'book'
id = Column(String(20), primary_key=True)
name = Column(String(20))
# “多” 的一方的 book 表是通过外键关联到 user 表的:
user_id = Column(String(20), ForeignKey('user.id'))