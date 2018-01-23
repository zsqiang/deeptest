#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    插入一个元素后，不改变列表原来的排列顺序，将新列表输出
'''
l = [1, 4, 6, 8, 10, 14]
length = len(l)
a = int(input("请输入要插入的数字："))
print(type(a))
for i in range(0, length-1):
    if l[i] < a < l[i+1]:
        # l[i+1] = a
        l.insert(i+1, a)
    if l[i] == a:
        l.insert(i+1, a)
        break
print("插入元素后新的列表为：", l)
