#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 20:15:37
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re,random,zipfile,sys

path = 'D:\\BaiduPanDownload\\PanData'
i = 0
l = []
for root, dirs, files in os.walk(path):
    for name in files:
        i = i + 1
        f = root + '\\' + name
        g = os.path.getsize(f)
        if g < 1024:
            print('{2}、{0}文件大小为：{1}b'.format(f,g,i))
            l.append(f)
        elif g< 1024*1024:
            g = g / 1024
            print('{2}、{0}文件大小为：{1:.2f}kb'.format(f,g,i))
            l.append(f)
        else:
            g = g / (1024 * 1024)
            print('{2}、{0}文件大小为：{1:.2f}mb'.format(f,g,i))
            l.append(f)

print(l)
x = int(input('请输入要删除的文件序号：'))
os.unlink(l[x-1])

'''
password = {'email':'123456',
                      'blog':'1qazXSW@',
                      'centos':'centos',
                      'card':'66666'}

if '66666' in password['card']:
    print(password['email'])


table = [['apples','oranges','cherries','banana'],['alice','judy','roger','fay'],['ddooggs','cats','moose','goose']]
l = len(table)
list1 = []
list2 = []
list3 = []

for i in range(l-1):
    if len(table[i]) >= len(table[i+1]):
        m =len(table[i])
    else:
        m = len(table[i+1])

for j in range(m):
    for i in range(l):
        list1.append(len(table[i][j]))
    a = max(list1)
    list2.append(a)
    list1 = []

for i in range(l):
    for j in range(m):
        list1.append(len(table[i][j]))
    a = max(list1)
    list3.append(a)
    list1 = []

for j in range(m):
    for i in range(l):
        print('{0}'.format(table[i][j].rjust(list3[i],'0')),end=' ')
    print()
'''