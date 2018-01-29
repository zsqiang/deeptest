#!/usr/bin/env python
# encoding: utf-8
'''
第一个知识点：
isinstance(object,type) #作用：判断一个对象是否是一个已知的类型
其中第一个参数object为对象，第二个参数type为类型名（int,list,dict,tumple...）或者
类型名的一个列表（int,list,float）是一个列表，其返回值为布尔型（True or false）
若第一个参数的类型和第二个参数的类型相同则返回True
'''
'''int类型的判断'''
a =4
print isinstance(a,int)
'''print False'''
print isinstance(a,str)
'''print True'''
print isinstance(a,(str,int,list))

'''判断是否是列表'''
a = [1,2,3]
if isinstance(a,list):
	print 'a is list '
else:
	print 'a is not list'

'''字符串的判断'''
a = 'b'
print isinstance(a,str)
print isinstance(a,int)
print isinstance(a,(int,list,float))
print isinstance(a,(int,list,float,str))

'''
第二部分：异常的执行顺序：
首先从try开始运行代码，捕捉Execpt 错误，如果出现Exception错误，则打印异常信息，其中
Exception是对异常的总称，如果不知道具体的异常是什么时，可以采用Exception表示异常名，
Exception 表示异常名，e表示异常的错误信息
'''

'''例1'''
i = 0
while i< 2:
	num1 = input('num1:')
	num2 = input('num2:')
	a = range(5)
	try:
		result = num1 + num2
		print result
		a[8]
	except IndexError,e:
		print 'IndexError:'
		print e
	finally:
		i = i + 1

'''
try...except...finally 结构异常：
不管是执行try部分的程序还是except部分的程序，【try和except只能执行其中的一部分】，
最终都会执行finally 部分的程序。
finally部分的作用是:
举例：当server和客户端端看连接后，无论是出现任务异常，是否执行try和except部分，
可以在finally部分，设置清理临时数据，无论如何最终都会清理的
finally子句和try子句联合使用但是和except语句不同，finally不管try子句内部是否有异常发生，
都会执行finally子句内的代码。所有一般情况下，finally自己常常用于关闭文件或者在Socket中。
'''
try:
	pass
except:
	pass
finally:
	pass

'''
try...except..else...finally异常结构：
else的作用是：当try部分的程序，正确执行后才会执行这部分的内容，
当以后再编写测试用例的时候，当用例正确执行后，在此部分输入，主要是检测
用例是否执行完毕的结果状态
'''
i = 0
while i < 1:
	try:
		num1 = input('num1:=')
		num2 = input('num2:=')
		result = num1 + num2
		print result
	except SyntaxError,e:
		print e
	else:
		print 'input num1,num2 is right'

	finally:
		i = i + 1
		print 'last step'


'''
raise 主动触发异常：
python中的raise关键字用于引发一个异常，基本上和java中的throw关键字相同:
'''
def ThrowErr():
	raise Exception("抛出一个异常")
#Exception:抛出一个异常:
# ThrowErr()

'''
raise 关键字后面是抛出是一个通用的异常类型(Exception)，一般来说抛出的异常越详细越好，python
在exceptions 模块内间了很多的异常类型，通过使用dir 函数来查看dir函数来查看exception中的异常类型：
'''
import exceptions
print dir(exceptions)

'''
自定义异常：自定义异常主要是针对工作中业务逻辑的产生的异常进行处理：
自定义异常必须继承Exception类，自定义异常按照命名规范以Error结尾，显示地告诉程序这是异常，自定义异常
使用raise语句引发,而且只能通过人工方式触发：
'''
'''写一个类，继承excepton'''
class CustomerException(Exception):
	def __init__(self,msg):
		self.msg = msg
	def __str__(self):
		return self.msg
'''自定义的异常，python不知道如何触发，需要自己触发'''
try:
	raise CustomerException('we are exception')
except CustomerException,e :
	print 'hello'
	print e

'''
断言：AssertionErrot
在try部分：如果a = 1 则不会进行任何操作，直接进行finally操作，如果设置a=1 出现错误，
则会引发异常AssertionError.
'''
a = 1
try:
	assert a == 2
except Exception,e:
	print e
finally:
	print 'last step'

'''
常见的异常种类：
1.NameError:尝试访问一个未声明的变量
2.ZeroDivisionError:除数为0
3.SyntaxError：语法错误
4.IndexError:索引超出范围
5.KeyError:字典的关键字不存在
6.IOError:输入输出错误
7.AttributeError:访问未知对象属性
8.ValueError：数值错误
9.TypeError:类型错误
10.AssertionError:断言错误
11.MemoryError:内存耗尽异常
12.NotImplementedError：方法没实现引起的异常
13.LookupError：键、值不存在引发的异常
14.StandardError：标准异常
'''






