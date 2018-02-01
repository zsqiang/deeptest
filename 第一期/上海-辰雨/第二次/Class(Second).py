#!/usr/bin/env python
# encoding: utf-8
'''super继承'''
class SchoolMember(object):
	'''初始化学校人数'''
	number = 0
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def tell(self):
		pass

	def enroll(self):
		'''注册'''
		'''SchoolMember.member:方法中调用类变量'''
		SchoolMember.number = SchoolMember.number + 1
		print ('new number [%s] is enrolled,now there are [%s] numbers'%(self.name,SchoolMember.number))

	def __del__(self):
		'''析构方法 ：一般是最后执行'''
		print ('number [%s] is getout!'%self.name)


class Teacher(SchoolMember):
	def __init__(self,name,age,course,salary):
		'''如果没有super则是对父类构造方法的重写'''
		'''super(Teacher,self)继承弗雷的变量name，age'''
		super(Teacher, self).__init__(name,age)
		self.course = course
		self.salary =salary
		'''引用父类的方法，这样Teacher 类每次在声明'''
		self.enroll()

	def teaching(self):
		'''讲课的方法'''
		print ('Teacher [%s] is teaching [%s] for class [%s]'%(self.name,self.course,'s12'))

	def tell(self):
		msg = 'Hi My name is [%s],work on [%s]'%(self.name,self.course)
		print msg


class Student(SchoolMember):
	def __init__(self,name,age,grade,sid):
		super(Student,self).__init__(name,age)
		self.grade = grade
		self.sid = sid
		'''将父类的方法放在构造方法中，当创建子类对象时，调用该方法'''
		self.enroll()

	def tell(self):
		msg = 'Hi my name is [%s],I am study [%s]'%(self.name,self.grade)


if __name__ == '__main__':
	t1 = Teacher('zhangsan',22,'python',200)
	t2 = Teacher('lisi',29,'linux',3000)

	s1 = Student('wangwu',25,'pathon',1483)
	s2 = Student('zhouliu',26,'python',1483)

	t1.teaching()
	t2.teaching()
	t1.tell()
	s1.tell()
	print (s2.number)

'''
私有成员和公有成员访问限制的不同:
私有成员命名时，前两个字符是下划线(特殊成员除外，例如：__init__,__call__,__dict__等)
'''
'''
公有静态字段：公有类变量可以通过 类访问，可以通过类内部的方法访问，还可以通过子类中的方法进行访问
'''
class C:
	name = '公有静态字段'
	def func(self):
		print C.name

class D(C):
	def show(self):
		print C.name

#类访问类中的变量
print ('C.name',C.name)
obj = C()
#类内部的方法访问类中的变量【实例访问类中的变量】
obj.func()
print 'hello'
#派生类【子类】也可以访问父类中的公有变量
obj_son = D()
obj_son.show()
'''私有静态变量【私有类变量】：私有的类变量只能通过 类的内部方法进行访问，不能通过类 访问，也不能通过子类 访问'''

class C():
	__name = '私有静态字段'
	def func(self):
		print C.__name

class D(C):
	def show(self):
		print C.__name

#类访问，系统报错
print (C.__name)
obj = C()
#类 内部的访问可以访问的
obj.func()
print ('hello')
#子类中的【派生类】访问 报错
obj_son = D()
obj_son.show()


'''
普通字段：
1.公有普通字段：对象可以访问，类内部可以访问，派生类中可以访问
2.私有普通字段：仅类内部可以访问
'''
class C:
	def __init__(self):
		self.foo = '公有字段'

	def func(self):
		'''类内部访问'''
		print self.foo

class D(C):
	def show(self):
		'''子类中访问'''
		print self.foo()

obj = C()
#通过对象访问
obj.foo
#通过类内部访问：
obj.func()
obj_son = D()
#在派生类中访问
obj_son.show()


class C:
	def __init__(self):
		self.__foo = '私有字段'

	def func(self):
		'''类内部的访问'''
		print self.foo

class D(C):
	def show(self):
		'''派生类中访问'''
		print self.foo

obj = C()
#通过对象访问--错误
obj.__foo
#类内部访问--正确
obj.func()
obj_son = D()
#在子类中访问--错误
obj_son.show()


