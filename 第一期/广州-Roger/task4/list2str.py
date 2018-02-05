#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 20:12:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,isNum

class List2str():
	def __init__(self):
		pass

	def list2str(self,a):
		lnum = len(a)
		str = ''
		for i in range (lnum-1):
			str1 = a[i]+','
			str = str + str1
		strp = str + 'and ' + a[lnum-1]
		return strp

if __name__ == '__main__':
	spam = ['apple','banana','tofu','cat']
	f =List2str()
	str = f.list2str(spam)
	print (str)

