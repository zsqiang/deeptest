#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


def array():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                s += a[i][j]
    print(s)


def arr():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = 0
    for i in range(3):
        s += a[i][i]
    print(s)


if __name__ == '__main__':
    array()
    arr()