# -*- coding:utf-8 -*-
__author__ = 'nancy'

import time

if __name__ == "__main__":
    loc = time.asctime(time.localtime())
    print(loc)

    print("24: ",time.strftime("%Y-%m-%d %H;%M:%S %A", time.localtime()))
    print("12: ",time.strftime("%Y-%m-%d %I;%M:%S %A", time.localtime()))
    print("AM/PM: ",time.strftime("%Y-%m-%d %p %I;%M:%S %A ", time.localtime()))
    print("tz: ",time.strftime("%Y-%m-%d %p %I;%M:%S %A %z", time.localtime()))