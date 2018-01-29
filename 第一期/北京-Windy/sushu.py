#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


l = [1, 2, 'v', 'o']
s = ','.join(str(n) for n in l)
print(s)


'''
    求100之内的素数
'''


def sushu():
    count = 0
    for i in range(1, 100):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
                count += 1
    print("1到100之间共有%d个素数" % count)


if __name__ == '__main__':
    sushu()