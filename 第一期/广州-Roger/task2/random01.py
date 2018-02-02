#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-24 20:18:08
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import random,triangggle

a=[]
for i in range(1,4):
	a.append(random.randint(10, 20))

x,y,z = a
q = triangggle.Trianggle(x, y, z)
print (x,y,z,q.triangggle())
