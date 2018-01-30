#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-25 11:20:05
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,math,isNum

class PrimeNum():
	"""判断是否为质数"""
	def __init__(self, num):
		self.num = num

	def isNum(self):
		num1 = int(math.sqrt(self.num))
		print (num1)
		x = 0
		for i in range(2,num1+1):
			if self.num % i ==0:
				print("{0}不是质数".format(self.num))
				break
			else:
				pass
		else:
			print("{0}是质数".format(self.num))


class PrimeYear():
	"""判断是否为闰年"""
	def __init__(self, num):
		self.num = num

	def isYear(self):
		if (self.num % 4) == 0 and (self.num % 100) != 0 \
		or (self.num % 400) == 0:
			print("{0}是闰年".format(self.num))
			return 1
		else:
			print("{0}不是闰年".format(self.num))
			return 0

if __name__ == "__main__":
	while True:
		try:
			x = input("请输入年份: ")
			y = input("请输入数字: ")
			f = isNum.isNum()
			if f.is_number(x) == False or f.is_number(y) == False:
				raise ValueError('')
			else:
				num1 = int(x)
				num2 = int(y)
				year = PrimeYear(num1)
				num = PrimeNum(num2)
				year.isYear()
#				print ('m={0}'.format(year.isYear()))
				num.isNum()
				break
		except ValueError:
			print("Oops!  数据不合法，请重新输入")