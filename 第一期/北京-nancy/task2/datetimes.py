# -*- coding:utf-8 -*-
__author__ = 'nancy'


from datetime import date
from datetime import time
from datetime import datetime

if __name__ == "__main__":
    #date
    today = date.today()
    print("today is: %s" % today)
    print("today is: %s %s %s" % (today.day, today.month, today.year))

    week_num = today.weekday()
    print("today weekday is %s" % week_num)

    week_day = ("Mon", "Tus", "Wed", "Thy", "Fri", "Sat", "Sun")
    print("today weekday is %s" % week_day[week_num])

    #datetime
    now = datetime.now()
    print("now is: %s" % now)
    d = datetime(year=8888, month=8, day=8, hour=8, minute=8, second=8)
    print("creat time is: %s" % d)

    #time
    t = time(hour=1, minute=1, second=1, microsecond=111)
    print("creat time is: %s" % t)


