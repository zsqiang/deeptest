#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 19:33:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re,pyperclip
import isNum

class stripRo():
    def __init__(self):
        pass

    def strip(self,a,b):
        pwd1Reg = re.compile(b + r'$')
        pwd2Reg = re.compile(r'^' + b)
        for i in range(len(a)):
            if re.search(pwd1Reg,a) == None and re.search(pwd2Reg,a) == None:
                print("strip1是{0}".format(a))
                break
            else:
                a = re.sub(pwd1Reg,'',a)
                a = re.sub(pwd2Reg,'',a)
                print("strip2是{0}".format(a))
        print("the result is {0}".format(a))
        return a

if __name__ == '__main__':
    text = str(pyperclip.paste())
    text1 = '0'
    f = stripRo()
    pwd = f.strip(text,text1)
    print(pwd)