#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-23 15:59:35
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,glob

#检索指定路径下后缀是 py 的所有文件：

#设置路径
path = 'D:/github/deeptest/第一期/广州-Roger/task2'
ls=[]

def getFile(path,ls):
	filelist = os.listdir(path)
	print(filelist)
	for x in range(len(filelist)):
		if filelist[x][filelist[x].rfind('.')+1:].upper()=='PY':
			pass
		else:
			print(filelist[x])


getFile(path, ls)

'''
os.chdir(path)
a = glob.glob('*.py')
print (a)
'''