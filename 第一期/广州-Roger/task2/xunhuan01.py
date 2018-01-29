#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 18:33:13
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


def fab(n):
    if n<1:
        print('输入有误！')
        return -1    
    if n==1 or n==2:
        return 1    
    else:
        return fab(n-1)+fab(n-2)

a = fab(int(input()))
print (a)