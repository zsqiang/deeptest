#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


import random


def rand():
    s = [random.randint(10, 999) for _ in range(10)]
    return s


def sort_mp():
    s = rand()
    length = len(s)
    for i in range(0, length):
        for j in range(i+1, length):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]
    print("冒泡排序-从小到大的结果为：", s)


def sort_xz():
    s = rand()
    length = len(s)
    for i in range(0, length):
        m = i
        for j in range(i+1, length):
            if s[m] > s[j]:
                m = j
        s[i], s[m] = s[m], s[i]
    print("选择排序-从小到大的结果为：", s)


if __name__ == '__main__':
    sort_mp()
    sort_xz()