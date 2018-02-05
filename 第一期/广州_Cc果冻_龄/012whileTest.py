#coding=utf-8

from __future__ import print_function
if __name__ == "__main__":

    print("九九乘法表实例")
    n = 1

    while n <= 9:
        for m in range(n,10):
            print("%d * %d = %2d" %(n,m,n*m),end = "  ")
        print("") #换行
        n = n + 1