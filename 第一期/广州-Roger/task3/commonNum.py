#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-25 15:18:47
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,isNum,math

class comDivisor():
	"""最大公约数"""
	def __init__(self):
		pass

	def divisor(self,m,n):
		if m>n:
			m,n = n,m
		else:
			pass
		for i in range(m,1,-1):
			if ((m % i == 0) and (n % i == 0)):
				print('{0}和{1}的最大公约数为{2}'.format(m,n,i))
				return i
				break
			else:
				pass
		else:
			print('{0}和{1}没有最大公约数'.format(m,n))
			i = 1
			return i


class comMultiple():
	"""最小公倍数"""
	def __init__(self):
		pass

	def multiple(self,m,n):
		if m>n:
			m,n = n,m
		else:
			pass
		x = comDivisor().divisor(m,n)
		i = int(m*n/x)
		print('{0}和{1}的最小公倍数为{2}'.format(m,n,i))
		return i

if __name__ == "__main__":
	while True:
		try:
			x = input("请输入数字1: ")
			y = input("请输入数字2: ")
			f = isNum.isNum()
			if f.is_number(x) == False or f.is_number(y) == False:
				raise ValueError('')
			else:
				num1 = int(x)
				num2 = int(y)
#				com1 = comDivisor().divisor(num1,num2)
				com2 = comMultiple().multiple(num1,num2)
				break
		except ValueError:
			print("Oops!  数据不合法，请重新输入")