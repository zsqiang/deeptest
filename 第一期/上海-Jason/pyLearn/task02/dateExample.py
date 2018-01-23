# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
概述
    在Python中，date、time、datetime类提供了一系列处理日期、时间和时间间隔的函数。
    在Python里，我们大致可以把其实现日期时间类分为5个：
        date            仅用于日期处理（年、月、日）
        time            仅用于时间处理（时、分、秒、毫秒）
        datetime        可以处理日期和时间的组合（年月日、时分秒毫秒）
        timedelta       日期时间处理，可以用于时间运算等
        tzinfo          用于时区处理
    
'''

from datetime import date
from datetime import time
from datetime import datetime

if __name__ == "__main__":
    #获取今天的日期
    today = date.today()
    print("今天是：%s"%today)#今天是：2018-01-23

    #把今天的日期年月日分开，重新格式化一下
    print("今天是%s年%s月%s日"%(today.year,today.month,today.day))#今天是2018年1月23日

    #看下今天是星期几
    #星期             序号
    #Monday             0
    #Tuesday            1
    #Wednesday          2
    #Thursday           3
    #Friday             4
    #Saturday           5
    #Sunday             6
    #weekday会获取到对应的序号，请根据序号对上上述表
    weekday_num = today.weekday()
    print("今天weekday是：%s"%weekday_num)

    #打印可读性更好的星期几
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print("今天weekday是：%s"%weekdays[weekday_num])

    #打印现在的时间
    today_now = datetime.now()
    print("现在是：%s"%today_now)#现在是：2018-01-23 13:59:25.718721

    #用time来构造个时间出来
    t = time(hour=12,minute=20,second=30,microsecond=200)
    print("我们自己构造的时间是：%s"%t)#我们自己构造的时间是：12:20:30.000200
    t = time(hour=12, minute=20)
    print("我们自己构造的时间是：%s" % t)  # 我们自己构造的时间是：12:20:00

    #用datetime构造日期时间
    d = datetime(year=2018,month=1,day=23,hour=14,minute=9,second=20,microsecond=500)
    print("我们构造的日期时间是：%s" % d)  # 我们构造的日期时间是：2018-01-23 14:09:20.000500
    d = datetime(year=2008,month=8,day=8)
    print("我们构造的日期时间是：%s"%d)#我们构造的日期时间是：2008-08-08 00:00:00