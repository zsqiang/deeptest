#!/usr/bin/env python
# encoding: utf-8
import time
'''装饰器可以提取大量函数中与本身功能无关的类似代码，从而达到代码重用的目的'''
'''
现有一个简单函数，想通过代码得到这个函数的大概执行时间，我们直接把计时逻辑方法'myfunc内部，
如果想要给另一个函数计时，就需要重复计时的逻辑。比较好的做法就是把计时逻辑放到另一个函数deco中：
'''
def deco(func):
	startTime = time.time()
	func()
	endTime = time.time()
	msecs = (endTime - startTime)* 1000
	print ('-> elapsed time :%f ms'%msecs)

def myfunc():
	print 'start myfunc'
	time.sleep(0.6)
	print 'end myfunc'

deco(myfunc)
myfunc()


'''
改良版：
'''
def deco(func):
	def wrapper():
		startTime = time.time()
		func()
		endTime = time.time()
		msecs = (endTime - startTime)*1000
		print ('-> elapsed time:%f ms'%msecs)
	return wrapper

def myfunc():
	print 'start myfunc'
	time.sleep(0.8)
	print ('end myfunc')

print 'myfunc is:',myfunc.__name__
myfunc = deco(myfunc)
print 'myfunc is:',myfunc.__name__
print myfunc()


'''
在python中，可以使用'@'语法糖来精简装饰器的代码,使用了'@'语法糖后，我们就不需要额外代码来给
myfunc 重新赋值，其实'@deco'的本质就是"myfunc = deco(myfunc)"
'''
def deco(func):
	def wrapper():
		startTime = time.time()
		func()
		endTime = time.time()
		msecs = (endTime - startTime)*1000
		print ('-> elapsed time:%f ms'%msecs)
	return wrapper

@deco
def myfunc():
	print ('start myfunc')
	time.sleep(0.2)
	print 'end myfunc'

print 'myfunc is:',myfunc.__name__
print myfunc()

'''
被装饰的函数带参数
'''
def deco(func):
	def wrapper(a,b):
		startTime = time.time()
		func(a,b)
		endTime = time.time()
		msecs = (endTime - startTime)*1000
		print '->elapsed time :%f ms'%msecs
	return wrapper

@deco
def addFunc(a,b):
	print 'start addFun'
	time.sleep(0.9)
	print 'result is %d'%(a+b)
	print 'end addFun'

addFunc(3,8)

'''
带参数的装饰器
装饰器本身也可以支持参数，例如说可以通过装饰器的参数禁止计时功能：
'''
def deco(arg = True):
	if arg:
		def _deco(func):
			def wrapper(*args,**kwargs):
				startTime = time.time()
				func(*args,**kwargs)
				endTime = time.time()
				msecs = (endTime - startTime)*1000
				print '->elapsed time:%f ms'%msecs
			return wrapper
	else:
		def _deco(func):
			return func
	return _deco


'''
装饰器是可以叠加使用的，对于python中的'@'语法糖，装饰器的调用顺序与使用@语法糖的顺序相反
'''
def deco_1(func):
	print 'enter into deco_1'
	def wrapper(a,b):
		print "enter into deco_1_wrapper"
		func(a,b)
	return wrapper

def deco_2(func):
	print ('enter into deco_2')
	def wrapper(a,b):
		print "enter into deco_2_wrapper"
		func(a,b)
	return wrapper

@deco_1
@deco_2
def addFunc(a,b):
	print 'result is %d'%(a+b)
addFunc(3,8)
