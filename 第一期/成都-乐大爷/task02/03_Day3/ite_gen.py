# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
生成器：生成器的结果是可迭代的，只能通过迭代返回具体的结果值，或者用next()函数调用。采用了yeild的函数，都是生成器。
迭代器：迭代器对象表示的是一个数据流，并不是可迭代对象就是迭代器，迭代器一定是可迭代的。
生成器->迭代器->可迭代的
"""

def triangle():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i-1] + L[i] for i in range(len(L) - 1)] + [1]

# n = 0
# for t in triangle():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# for i in range(10):
#     print(next(triangle()))
# 为什么这样无法输出想要的结果？因为每次调用的triangle()是一个单独的实例化对象。

# t = triangle()
# for i in range(10):
#     print(next(t))

# 迭代器怎么创建，用iter()
odd = iter([1,2,3,4])
for i in range(4):
    print(next(odd))


