#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-26 18:23:07
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os
from functools import reduce

def f(x, y):
	return x +y
a = reduce(f, [1, 2, 3, 4])
b = f(f(f(1, 2), 3), 4)

print (a,b)