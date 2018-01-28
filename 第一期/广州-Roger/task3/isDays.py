#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-25 16:55:25
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,isPrime,isNum

class theDays():
	'''判断是第几天'''
	months = (0,31,59,90,120,151,181,212,243,273,304,334)
	def __init__(self,x,y,z):
		f = isNum.isNum()
		if f.is_number(x) == False or f.is_number(y) == False \
		or f.is_number(z) == False:
			raise ValueError('ValueError')
		elif int(y)>12 or int(z)>31:
			raise IndexError('IndexError')
		else:
			pass
#		except ValueError:
#			print('数据不合法，请重新输入')
#		except IndexError:
#			print("输入的日期不对，请重新输入")
		self.x=int(x)
		self.y=int(y)
		self.z=int(z)
		pass
	
	def days(self):
		'''判断是否闰年'''
		m1 = isPrime.PrimeYear(self.x)
		m = m1.isYear()
		'''查出对应天数'''
		n = theDays.months[self.y-1] + self.z
		'''计算总天数'''
		if self.y>2:
			day=n+m
		else:
			day=n
		return day
		pass


if __name__ == "__main__":
	while True:
		try:
			x = input("请输入年份: ")
			y = input("请输入月度: ")
			z = input("请输入天数: ")
			f = theDays(x,y,z)
			if  (f.days()) > 0:
				print (f.days())
				break
		except ValueError:
			print('数据不合法，请重新输入')
			pass
		except IndexError:
			print('输入的日期不对，请重新输入')
			pass
