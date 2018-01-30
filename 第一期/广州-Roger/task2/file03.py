#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-23 16:42:14
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,sys

eachline='123,23,12,2,123a'
rep_word='123'
new_word='abc'

s=eachline.count(rep_word)
p=eachline.replace(rep_word, new_word)
print(s)
print(p)

print(os.access("D:/github/deeptest/第一期/广州-Roger/task2", os.F_OK))

f=os.open('abc.txt', os.O_RDWR|os.O_CREAT )
f2=os.open('dict01.py', os.O_RDWR|os.O_CREAT )
fd2 = f2
print(os.read(fd2, 100))
os.dup2(f, fd2)
os.lseek(fd2, 0, 0)
print(os.read(fd2, 100))

os.close(f)