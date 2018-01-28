#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-23 17:33:47
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,time
import re

# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xyz");

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) ', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


localtime = time.localtime()
print ("本地时间为 :", localtime)