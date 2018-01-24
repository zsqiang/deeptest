# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
条件语句
if语法：判断
if...else
if...elif...elif...else
"""
def juge_data(a, b):
    if a == b:
        print("你输入了2个相等的数喔！")
    elif a > b:
        print("你输入的第一个数大于第二个数喔！")
    else:
        print("你输入的第一个数小于第二个数喔！")

flag = 1
try:
    a = int(input("请输入一个数字："))
except:
    print("输入的不是数字")
    flag = 0
try:
    b = int(input("请输入一个数字："))
except:
    print("输入的不是数字")
    flag = 0

if flag == 1:
    juge_data(a, b)
else:
    print("请重新执行程序进行数据比较！")





# isinstance(a,int)

