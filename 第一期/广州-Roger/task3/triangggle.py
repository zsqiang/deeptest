#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-24 18:59:31
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,math,isNum

class Trianggle():
 	"""三角形求面积"""
 	def __init__(self, a, b, c):
 		self.a = a
 		self.b = b
 		self.c = c

 	def triangggle(self):
 		p = (self.a+self.b+self.c)/2
 		area1 = p*(p-self.a)*(p-self.b)*(p-self.c)
 		area2 = math.sqrt(area1)
 		return area2


if __name__ == "__main__":

	while True:
		try:
			x = input("请输入第1个数: ")
			y = input("请输入第2个数: ")
			z = input("请输入第3个数: ")
			f = isNum.isNum()
			if f.is_number(x) == False or f.is_number(y) == \
			False or f.is_number(z) == False:
				raise ValueError('')
			elif int(x)+int(y)<=int(z) or int(x)+int(z)<=int(y) or \
			int(y)+int(z)<=int(x):
				print("Woos!  数据不能构成三角形，请重新输入")
			else:
				q = Trianggle(int(x), int(y), int(z))
				print (q.triangggle())
				break
		except ValueError:
			print("Oops!  数据不合法，请重新输入")
