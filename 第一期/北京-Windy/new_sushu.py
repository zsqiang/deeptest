#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
import math


def sushu():

    '''
    判断101-200之间有多少个素数，并将其输出
    '''

    count = 0
    for i in range(100, 201):
        for j in range(2, int(math.sqrt(i)-1)):
            if i % j == 0 and i % 2 != 0 and i % 5 != 0 :
                print('%d' % i, end=' ')
                count += 1
                if count % 4 ==0:
                    print(end='\n')
    print(end='\n')
    print("101-200之间共有%d个素数" % count)


def new_sushu():
    cou = 0
    for i in range(100, 202):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=' ')
            cou += 1
            if cou % 4 == 0:
                print(end='\n')
    print('\n')
    print("101-200之间共有%d个素数" % cou)


if __name__ == '__main__':
    sushu()
    new_sushu()