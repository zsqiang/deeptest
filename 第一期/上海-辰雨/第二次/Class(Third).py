#!/usr/bin/env python
# encoding: utf-8
'''python中的hasattr(),getattr(),setattr,delattr()的用法'''
'''
1.hasattr(object,name)
判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True,否则返回False
需要注意的是name 要用括号括起来
'''
class test():
	name ='xiaoming'
	def run(self):
		return 'HelloWorld'

t = test()
#判断对象是否有name属性
print hasattr(t,'name')
#判断对象是否有run方法
print hasattr(t,'run')


'''
getattr(object,name[,default])
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
需要注意的是，如果是返回对象方法，返回的是方法的内存地址，如果运行这个方法，可以在可以添加一对括号
'''
class test():
	name = 'xiaohua'
	def run(self):
		return 'HelloWorld'

t = test()
#获取name属性，存在就打印出来
print getattr(t,'name')
#获取run方法，存在就打印出方法的内存地址
print getattr(t,'run')
#获取run方法，后面加括号可以将这个方法运行
print getattr(t,'run')()
#获取一个不存在的属性
# print getattr(t,'age')
#若属性不存在，返回一个默认值
print getattr(t,'age','18')

'''
setattr(object,name,values)
给对象属性赋值，若属性不存在，先创建在赋值
'''
class test():
	name = 'xiaohua'
	def run(self):
		return 'HelloWorld'

t = test()
#判断属性是否存在
print hasattr(t,'age')
#为属相赋值，并没有返回值
print setattr(t,'age','18')
#属性存在了
print hasattr(t,'age')


'''
delattr(object,name) 删除object对象名为name的属性
'''
class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

tom = Person('Tom',35)
print dir(tom)
#删除object对象名为name的属性
print delattr(tom,'age')
print dir(tom)
