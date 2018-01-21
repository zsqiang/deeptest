#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 14:38:32
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os

a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
 
a = '7+1'
print (a)
b=eval(a)
print (b)
 
print (r'\n')
print (R'\n')
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
print ("我叫 %4s 今年 %04d 岁!" % ('小明', 10))
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)