#! /usr/bin/env python
# -*- coding: UTF-8 -*-

'''
    将一个数组逆序输出
'''

l = []
l = [i for i in input("输入一个列表:").split(' ')]
l.reverse()
print(l)

'''
    计算1-100的和
'''

s = [i for i in range(1, 101)]
count = 0
for i in range(100):
    count += s[i]
print("1-100的和为：", count)

tep = 0
for i in range(1, 101):
    tep += i
print("1-100的和为：", tep)
