#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 18:03:18
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("新的字典为 : %s" %  str(dict))

dict = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" %  str(dict))


dict = {'Name': 'Runoob', 'Age': 27}
print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))
print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
print ("新字典为：", dict)
print ("Value : %s" %  dict.items())
pop_obj=dict.pop('Name1','无')
print (pop_obj)
print ("新字典为：", dict)