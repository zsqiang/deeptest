#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-24 20:46:44
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os
import unicodedata

class isNum():
	"""判断是否为正数"""
	def __init__(self):
		pass

	def is_number(self,s):
		try:
			x = float(s)
			if x>0:
				return True
			else:
				return False
		except ValueError:
			pass

		try:
			unicodedata.numeric(s)
			return True
		except (TypeError, ValueError):
			pass

		return False

if __name__ == "__main__":
	f=isNum()
	print(f.is_number(-1.5))
	print(f.is_number('1e3'))
	print(f.is_number('sd'))
