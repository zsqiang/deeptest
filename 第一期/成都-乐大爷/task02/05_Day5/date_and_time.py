# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
Python中处理日期的模块和函数有：
date：用于日期处理（年、月、日）
time： 用于时间处理（时、分、秒、毫秒）
datetime：用于处理日期和时间的组合
timedelta：日期时间处理，可用于时间运算
tzinfo：用于时区处理
"""

from datetime import date
from datetime import time
from datetime import datetime

def date_exc():
    today = date.today()
    print("今天是 %s" % today)

    # 把今天的日期重新格式化一下
    print("今天是 %s 年 %s 月 %s 日" % (today.year, today.month, today.day), end="")

    # 星期对应 Monday-0,...,Sunday-6
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")  
    weekday_num = today.weekday()
    print(", %s " % weekdays[weekday_num])

    # 查看现在的时间
    today_now = datetime.now()
    print("现在是 %s" % today_now)

    # 用time来构造时间
    t = time(hour=12, minute=20, second=30, microsecond=200)
    print("我们自己造的时间是 %s" % t)

    # 用datetime构造日期时间
    d = datetime(year=2008, month=8, day=8, hour=8, minute=8, second=8)
    print("我们自己造的日期时间 %s" % d)

import time
# 对时间进行格式化处理：strftime函数
def time_turn():
    localtime = time.asctime(time.localtime())
    print("当前默认日期时间格式：%s" % localtime)
    print(type(localtime))

    # 格式化为：年-月-日 时：分：秒 星期几
    print("24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))

    print("12小时制缩写格式：", time.strftime("%Y-%m-%d %I:%M:%S %a", time.localtime()))

     # 带a.m. 或 p.m. 标识时间格式  %p
    print("带a.m或p.m 24小时制全格式：", 
        time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))
    
    # 把时区也带上看看 %z
    print("带时区的全格式：", 
        time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))
    
    # 格式乱排下试试
    print("随意排格式：", 
        time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))


# date_exc()
time_turn()

"""
time.strftime()  datetime.strptime()
"""