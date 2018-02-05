#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 20:43:22
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os

class displayObj():
    def __init__(self):
        pass

    def display(self,a,str=''):
        print ('Object:')
        keynum = 0
        for key,value in a.items():
            for i in range(len(str)):
                if str[i] == key:
                    value = value +1
            print('{0:2d} {1}'.format(value,key))
            keynum = int(value) + int(keynum)
        print ('total num :{0}'.format(keynum))

if __name__ == '__main__':
    dict = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'level':12}
    str = ['rope','level','level']
    displayObj().display(dict)
    displayObj().display(dict,str)