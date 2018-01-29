#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 20:02:11
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re
from datetime import date

vec = [2, 4, 6]
a = [3*x for x in vec]
print (a)

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1+v2)

a=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print (a)

now=date.today()
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
