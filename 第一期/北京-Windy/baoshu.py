#!/usr/bin/env  python
# -*- coding: UTF-8 -*-

'''
    有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
    凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''


def leng(array):
    length = len(array)
    return length


if __name__ == '__main__':
    n = int(input("请输入总人数："))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n-1:
        if num[i] != 0:
            k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n:
                i = 0

    i = 0
    while num[i] == 0:
        i += 1
    print("最后留下的是原来的%d号那位" % num[i])
    array = input("请输入一个字符串：")
    lon = leng(array)
    print("字符串的长度为：%d" % lon)
