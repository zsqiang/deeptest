# -*- coding:utf-8 -*-

__author__ = 'catleer'



"""
for语法：循环 break continue
循环：while do...while
"""
# 99乘法表

for i in range(1,10):
    for j in range(1, i+1):
        # print('{}*{}={}\t'.format(i,j,i*j),end="")
        print('%d*%d=%d\t' % (i, j, i * j), end='')

    print()
