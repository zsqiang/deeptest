#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 15:08:38
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,random
import math

print (random.randrange(1, 3, 2))

m = [1,2,3,4,5]
# print(m[0:3:2])
# print(m[5::-1])

list_2d = [ ['x' for i in range(5)] for i in range(5)]
list_2d[0].append(3)
list_2d[0].append(5)
list_2d[2].append(7)
# print (list_2d)

x='abc'
y='abc'
print ((x>y)-(x<y))

str = "this is string example....wow!!!"
print (str.replace("is", "was", 1))

str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(20))
print ("str.zfill : ",str.zfill(50))