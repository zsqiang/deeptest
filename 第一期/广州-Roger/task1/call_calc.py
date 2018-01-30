#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 20:17:35
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,sys,random
sys.path.append('D:\\github\\deeptest\\第一期\\广州-Roger\\task2')
import triangggle,calc,isNum,isPrime


print (dir(isPrime.PrimeNum))
c = isPrime.PrimeNum(17)
c.isNum()

b = calc.Calc(2,3)
print (b.add())

a=[]
for i in range(1,4):
	a.append(random.randint(10, 20))

x,y,z = a
q = triangggle.Trianggle(x, y, z)
print (x,y,z,q.triangggle())
