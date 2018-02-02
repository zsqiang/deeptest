#!/usr/bin/env  python
# -*- coding: UTF-8 -*-

#
# def numb(numbers):
#     for i in range(6):
#         numbers.append(int(input('输入一个数字:\n')))


def numb():
    array = [int(i) for i in input("请输入6个数字：").split(' ')]
    return array


p = 0


def max_arr(array):
    print(array)
    max = 0
    for i in range(1, len(array)-1):
        p = i
        if array[p] > array[max]:
            max = p
    k = max
    array[0], array[k] = array[k], array[0]


def min_arr(array):
    min = 0
    for i in range(1, len(array)-1):
        p = i
        if array[p] < array[min]:
            min = p
    l = min
    array[5], array[l] = array[l], array[5]


def outp(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')


if __name__ == '__main__':
    array = numb()
    max_arr(array)
    min_arr(array)
    print("计算结果为：")
    outp(array)
