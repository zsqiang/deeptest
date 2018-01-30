#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
'''
    计算一个数字的平方，如果大于50就退出
'''


def square(a):
    return a * a


again = 1
while again:
    a = int(input("请输入一个数："))
    tep = square(a)
    if tep > 50:
        again = False
    else:
        print(tep)