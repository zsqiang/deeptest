# -*- coding:utf-8 -*-
__author__ = 'nancy'

from datetime import datetime,timedelta
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
if __name__ == "__main__":
    t1 = datetime.now()
    nextD = t1 + timedelta(days = 1)
    print("next day is: %s" % nextD)

    nextS = t1 + timedelta(seconds = 10)
    print("next day is: %s" % nextS)

    space = nextS  - nextD
    print(space)

    print(timedelta.max)
    print(timedelta.min)
    print(timedelta.resolution)

    print(timedelta(microseconds=10));