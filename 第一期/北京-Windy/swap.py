#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


if __name__ == '__main__':
    n = int(input("整数n为："))
    m = int(input("整数m为："))

    def move(array, n, m):
        array_end = array[n - 1]
        for i in range(n - 1, -1, -1):
            array[i] = array[i - 1]
        array[0] = array_end
        m -= 1
        if m > 0:
            move(array, n, m)

    # number = []
    # for i in range(n):
    #     number.append(int(input("请输入一个数字：")))
    number = [int(i) for i in input('请输入一串数字：').split(' ')]
    print("原始列表为：", number)

    move(number, n, m)
    print("移动之后的列表为：", number)