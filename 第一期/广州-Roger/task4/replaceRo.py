#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 19:33:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re,pyperclip
import isNum

class replaceRo():
    def __init__(self):
        pass

    def replace(self,a,b,c):
        list = a
        for i in range(len(b)):
            list = re.split(b[i],list,1)
            list = list[0] + c[i] + list[1]
        return list

if __name__ == '__main__':
    a = 'the panda walked to the park.A nearby panda was gone.'
    b = ['panda','park','panda']
    c = ['dog','home','cat']
    f = replaceRo()
    pwd = f.replace(a,b,c)
    print(pwd)