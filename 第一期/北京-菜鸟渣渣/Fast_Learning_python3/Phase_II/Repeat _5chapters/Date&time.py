# coding=utf-8

'''
在python中， date、time、datetime类提供了一系列处理日期、时间和时间间隔的函数。

在Python里我们大致可以把其实现日期时间类分为5个：

date
仅用于日期处理（年、月、日）

time
仅用于时间处理（时、分、秒、毫秒）

datetime
可以处理日期和时间的组合（年、月、日、时、分、秒、毫秒）

timedelta
日期时间处理，可以用于时间运算等

tzinfo
用于时区处理
'''

from  datetime import date
from datetime import datetime
from datetime import time
from  datetime import timedelta
from datetime import tzinfo

if __name__ == "__main__":
    print("----------------日期时间处理-------------------")
    today = date.today()
    d = date(year=2007, month=12, day=12)
    print("今天是:%s" % d)
    print("今天是:%s" % today)

    # 把今天的日期年月日分开，重新格式化下一下
    print("今天是 %s %s %s" % (today.day, today.month, today.year))

    weekday_num = today.weekday()
    '''
      # 看下今天是星期几
    # 星期几    序号
    # Monday     0
    # Tuesday    1
    # Wednesday  2
    # Thursday   3
    # Friday     4
    # Saturday   5
    # Sunday     6
    # weekday会获取到对应的序号，请根据序号对上上述表，来看是星期几
    '''
    print("今天是周 : %s" % (weekday_num + 1))
    weekdays = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")

    print("今天是 %s" % weekdays[weekday_num])

    # 查看现在的时间
    today_new = datetime.today()
    print("现在是 %s" % today_new)

    # time来构造时间
    t = time(hour=12, minute=20, second=30, microsecond=200)
    print("我们自己造的时间是 %s" % t)
    d = datetime(year=2008, month=8, day=8, hour=8, minute=8, second=8)
    print("我们自己造是日期时间 %s" % d)
    print("--------------格式化日期时间：strftime函数-----------------")
    '''
    大家是不是在各种网站、系统上见过不同格式的日期时间显示？那接下来我们也来做做日期时间的格式化。

我们需要用到strftime函数，先看一下可用于格式化日期时间的符号：
    
    %y  两位数的年份表示（00-99）
    %Y  四位数的年份表示（000-9999）
    %m  月份（01-12）
    %d  月内中的一天（0-31）
    %H  24小时制小时数（0-23）
    %I  12小时制小时数（01-12）
    %M  分钟数（00=59）
    %S  秒（00-59）
    %a  简写的星期名称
    %A  完整星期名称
    %b  简写的月份名称
    %B  完整的月份名称
    %c  相应的日期表示和时间表示
    %j  年内的一天（001-366）
    %p  A.M.或P.M.的等价符
    %U  一年中的星期数（00-53）星期天为星期的开始
    %w  星期（0-6），星期天为星期的开始
    %W  一年中的星期数（00-53）星期一为星期的开始
    %x  相应的日期表示
    %X  相应的时间表示
    %z  当前时区的名称
    %%  %号本身
    '''
    # 先看下当前默认格式化的时间
    localtime = time.asctime(time.localtime())
    print("当前默认日期时间格式: %s" % localtime)

    # 格式化为： 年-月-日 时:分:秒 星期几
    print("24小时制全格式 : ", time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
    # 带a.m. 或 p.m. 标识时间格式  %p
    print("带a.m或p.m 24小时制全格式：",
          time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))

    # 把时区也带上看看 %z
    print("带时区的全格式：",
          time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

    # 格式乱排下试试
    print("随意排格式：",
          time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))
