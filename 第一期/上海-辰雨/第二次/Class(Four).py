#!/usr/bin/env python
# encoding: utf-8
'''
python中的特殊类：
__name__:类的名称（字符串）
__doc__:类的文档字符串
__bases__：类的所有父类组成的元祖
__dict__:类的属性组成的字典
__module__:类所属的模块
__class__:类对象的类型
'''
class Student(object):
	'''this is a student class'''
	count = 0
	books = []
	def __init__(self,name,age):
		self.name = name
		self.age = age
	pass

print Student.__name__
print Student.__doc__
print Student.__bases__
print Student.__dict__
print Student.__module__
print Student.__class__

'''
在一个类中，可以出现三种方法，实例方法，静态方法和类方法：
实例方法中第一参数必须是'self','self'类似于C++中的'this'
实例方法中只能通过类调用，这时候'self'就代表这个实例本身。通过'self'可以直接访问实例的属性
'''
class Student(object):
	'''this is a Student class'''
	count = 0
	books = []
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def printInstanceInfo(self):
		print '%s is %d years old'%(self.name,self.age)
	pass

zhangsan = Student('zhangsan',28)
zhangsan.printInstanceInfo()


'''
类方法以cls作为第一个参数，cls表示类本身，定义时使用@classmethod装饰器。
通过cls可以访问类的相关属性
'''
class Student(object):
	'''this is a student class'''
	count = []
	books = []
	def __init__(self,name,age):
		self.name = name
		self.age = age

	@classmethod
	def printClassInfo(cls):
		print cls.__name__
		print dir(cls)
	pass

Student.printClassInfo()
lisi = Student('lisi',28)
lisi.printClassInfo()

'''
静态方法与实例方法和类方法不同，静态方法没有参数限制，即不需要实例参数，也不需要类参数，
定义的时候使用@staticmethod装饰器
同类方法一样，静态方法可以通过类名访问，也可以通过实例访问【如果是这样的话，可以不用生成对象直接调用方法】
'''
class Student(object):
	'''this is a Stduent class'''
	count = 0
	books = []
	def __init__(self,name,age):
		self.name = name
		self.age = age

	@staticmethod
	def printClassAttr():
		print Student.count
		print Student.books
	pass

Student.printClassAttr()
wangwu = Student('wangwu',28)
wangwu.printClassAttr()
'''
这三种方法的主要区别在于参数，实例方法被绑定到一个实例，只能通过实例进行调用，但是对于静态方法和类方法，可以
通过类名和实例两种方式进行调用
'''
















