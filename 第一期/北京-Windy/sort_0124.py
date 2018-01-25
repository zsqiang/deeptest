#! /usr/bin/env python
# -*- coding: UTF-8 -*-

'''
    将连续输入的三个数字排序后输出
'''


def sort():
    l = [int(i) for i in input("请输入三个连续的数字：").split(' ')]
    print("输入的列表为：", l)
    leng = len(l)
    for i in range(0, leng):
        for j in range(i, leng):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    print("排序后的列表为：", l)


if __name__ == '__main__':
    sort()