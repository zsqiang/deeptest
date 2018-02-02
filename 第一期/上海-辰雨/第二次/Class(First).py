#!/usr/bin/env python
# encoding: utf-8
class Role(object):
	def __init__(self,name,age,sex,grade):
		self.name = name
		self.age = age
		self.sex = sex
		self.grade = grade

	def buy_gun(self,age):
		'''函数中的局部变量在函数外面是无法访问的，例如buy_gun(age)就无法访问'''
		print ('[%s] age is [%d]'%(self.name,age))
		'''这句话就是在调用buy_gun 传入的参数age,会改变实例age的值'''
		self.age = age

'''将一个抽象的类，变成一个具体的对象的过程，就叫做类的实例化'''
p = Role('zhangssan',28,'man',100)
'''对象p调用实例的方法'''
p.buy_gun(27)
print ('p.name',p.name)


'''
类变量和对象中的成员变量的区别：
类变量：是可在类的所有实例之间共享的值(也就是说，它们不是单独分配给每个实例的)
		例如下例中的num_of_instance就是类变量，用于跟踪存在着多个Test的实例
实例变量：实例化之后，每个实例单独拥有的变量。
'''
class Test(object):
	num_of_instance = 0
	def __init__(self,name):
		self.name = name
		Test.num_of_instance = Test.num_of_instance + 1

if __name__ == '__main__':
	print Test.num_of_instance
	t1 = Test('jack')
	print t1.name, t1.num_of_instance
	print Test.num_of_instance
	t2 = Test('lucy')
	print t2.name,t2.num_of_instance

'''
python中的类变量：
1.类本身拥有自己的类变量(保存在内存),当一个TestClass类的对象被构造时，会将当前类变量拷贝一份给这个对象，当前类变量的值
是多少，这个对象拷贝得到的类变量的值就是多少；
2.而且，通过对象来修改类变量，并不会影响其他对象的类变量的值，因为大家都有各自的副本，更不会影响本身所拥有的那个类变量
的值，只有类自己才能改变类本身拥有的类变量的值。
'''

'''
类中的方法：
@classmethod 类方法的作用：
类的方法中,被@classmethod装饰的函数，不能访问实例变量，只能访问类变量
'''
class Animal():
	#类变量为实例所共有
	hobby = 'meat'
	def __init__(self,name):
		self.name = name

	#@classmethod 类方法的作用，不能访问实例变量，只能访问类变量
	@classmethod
	def talk(self):
		print ('%s is talking...'%self.hobby)

Animal.talk()
Animal.hobby
print Animal.hobby
cat = Animal('xiaomao')
cat.talk()
cat.hobby
print cat.hobby


'''
@staticmethod静态方法：
1.类中的方法被@staticmethod装饰的函数，即不能访问类变量也不能访问实例变量。
2.这种请情况下，被@staticmethod装饰的函数，只是属于类的 的框架内，方法跟类没有任何的关系，
只能做一些其他的操作，打印，输出，或者作为计数器等等.
'''
class Animal():
	hobby = 'meat'
	def __init__(self,name):
		self.name = name

	@staticmethod
	def walk():
		print ('%s is walking...')

dog = Animal('dog')
dog.walk()
print dog.hobby

'''
@property 属性方法:
类中被@property装饰的函数，如下图所示，把habbit方法变成变量，可以向变量一样，直接调用
'''
class Animal():
	hobby = 'meat'
	def __init__(self,name):
		self.name = name

	@property
	def habbit(self):
		print ('%s hobby is eating'%self.name)

cat = Animal(u'二逗')
cat.habbit
