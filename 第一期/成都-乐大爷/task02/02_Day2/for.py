# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
循环只有for和while 没有do...while
"""

# 杨辉三角形?递归？生成器？
def triangles():
    L = [1]
    while True:
        yield L        
        L = [1]+[L[i] + L[i+1] for i in range(len(L)-1)]+[1]

t = triangles()
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 15:
        break

        