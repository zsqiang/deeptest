#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 12:30:50
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os

class tableData():
    def __init__(self,table):
        self.table = table
        self.l = len(table)
        list1 = []
        self.list2 = []
        self.list3 = []
        
        for i in range(self.l-1):
            if len(self.table[i]) >= len(self.table[i+1]):
                self.m =len(self.table[i])
            else:
                self.m = len(self.table[i+1])

        for j in range(self.m):
            for i in range(self.l):
                list1.append(len(self.table[i][j]))
            a = max(list1)
            self.list2.append(a)
            list1 = []

        for i in range(self.l):
            for j in range(self.m):
                list1.append(len(self.table[i][j]))
            a = max(list1)
            self.list3.append(a)
            list1 = []

    def tablerow(self):
        for j in range(self.m):
            for i in range(self.l):
                print('{0}'.format(self.table[i][j].rjust(self.list2[j],'0')),end=' ')
            print()

    def tablecolnum(self):
        for j in range(self.m):
            for i in range(self.l):
                print('{0}'.format(self.table[i][j].rjust(self.list3[i],'0')),end=' ')
            print()

if __name__ == '__main__':
    table = [['apples','oranges','cherries','banana'],
                  ['alice','judy','roger','fay'],
                  ['dogs','cats','moose','goose']]
    f = tableData(table)
    f.tablecolnum()

        