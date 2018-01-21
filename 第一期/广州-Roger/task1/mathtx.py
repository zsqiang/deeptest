#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-08 15:47:25
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : 01

import os

# 加法
def add(i,f,j):
	print (i," ",f," ",j," = ",mi+mj)

# 减法
def sub(i,f,j):
	print (i," ",f," ",j," = ",mi-mj)

# 乘法
def mul(i,f,j):
	print (i," ",f," ",j," =  %.4f" % (mi*mj))

# 除法
def div(i,f,j):
	if mj == 0:
		print("division,the second num can not be 0")
	else:
		print (i," ",f," ",j," = %.4f" % (mi/mj))

if __name__ == '__main__':
	i = input("please input the first num:")
	f = input("please input the Calculate Method:")
	j = input("please input the second num:")
	mi = float(i)
	mj = float(j)
	if f == '+':
		add(i,f,j)
	elif f == '-':
		sub(i,f,j)
	elif f == '*':
		mul(i,f,j)
	elif f == '/':
		div(i,f,j)
	else:
		print("Calculate Method Error")