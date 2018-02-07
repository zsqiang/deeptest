#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 19:33:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re,pyperclip
import isNum

class findfile():
    def __init__(self):
        pass

    def getfile(self,a,b,c):
        flist = os.listdir(a)
        pwd1Reg = re.compile(b)
        pwd2Reg = re.compile(r'.' + c.upper() + r'$')
        rlist = []
        for i in range(len(flist)):
            if re.search(pwd1Reg,flist[i].upper()) == None or re.search(pwd2Reg,flist[i].upper()) == None:
                print('not found')
            else:
                rlist.append(flist[i])
        return rlist

if __name__ == '__main__':
    path = 'D:/github/deeptest/第一期/广州-Roger/task2'
    b = '01'
    c = 'py'
    f = findfile()
    pwd = f.getfile(path,b,c)
    print(pwd)