#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-23 14:47:44
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os

a='1/7\n'
s=repr(a)
print(a)
print(s)
'''
for x in range(1, 11):
     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     print(repr(x*x*x).rjust(4))

for x in range(1, 11):
     print('{0:2d} {1:3.1f} {2:4d}'.format(x, x*x, x*x*x))
'''
print('{0}网站 和 {1}'.format('Google', 'Baidu'))
print('{1}王者 和 {1}'.format('Google', 'Baidu'))
print('{name}网址：{site}'.format(name='百度', site='www.baidu.com'))

f=open('abc.txt','r+')
f.write("Python非常好")
r=f.read()
print(r)
f.close()