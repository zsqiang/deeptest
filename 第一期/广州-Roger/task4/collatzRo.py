#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 19:33:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,isNum

class collatzRo():
	"""docstring for collatzRo"""
	def __init__(self, a):
		self.a = a
		pass

	def collatz(self):
		if self.a % 2 ==0:
			b = self.a / 2
			print (int(b))
			return b
		else:
			b = self.a *3 + 1
			print (int(b))
			return b

if __name__ == '__main__':
	while True:
		a = input ("please enter a number:")
		try:
			int(a)
			break
		except ValueError:
			print("请输入正整数")
	while True:
		a = collatzRo(int(a)).collatz()
		if a == 1:
			break
