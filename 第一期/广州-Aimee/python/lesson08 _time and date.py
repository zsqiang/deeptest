#coding = utf-8

__author__ = 'Aimee'

from datetime import date
from datetime import time
from datetime import datetime


# if __name__ == "__main__":
#
#     #获取下今天的日期
#     today = date.today()
#     print("今天是 %s" %  today)
#
#     #把今天的日期年月日分开，重新格式化一下
#     print("今天是 %s %s %s" %(today.day,today.month,today.year))
#
#
#     weekday_num = today.weekday()
#     print("今天weekday是 %s" % weekday_num)
#
#     weekdays = ("Monday","  Tuesday","Wednesday",
#                 "Thursday", "Friday", "Saturday", "Sunday")
#     print("今天是 %s " % weekdays[weekday_num])
#
#     print("-" *30)
#
#
#     #看看现在的时间
#     today_now = datetime.now()
#     print('现在是 %s' % today_now)
#
#     #用time来构造个时间出来
#     t = time(hour=12,minute=20,second=30,microsecond=200)
#     print('我们自己构造的时间是 %s' %t)
#
#     #再构造日期时间格式出来试试
#     d = datetime(year=2018,month=1,day=21,hour=14,minute=21,second=45)
#     print('我们自己构造的日期时间 %s' % d)


#格式化日期时间：strftime函数
# %y  两位数的年份表示（00-99）
# %Y  四位数的年份表示（000-9999）
# %m  月份（01-12）
# %d  月内中的一天（0-31）
# %H  24小时制小时数（0-23）
# %I  12小时制小时数（01-12）
# %M  分钟数（00=59）
# %S  秒（00-59）
# %a  简写的星期名称
# %A  完整星期名称
# %b  简写的月份名称
# %B  完整的月份名称
# %c  相应的日期表示和时间表示
# %j  年内的一天（001-366）
# %p  A.M.或P.M.的等价符
# %U  一年中的星期数（00-53）星期天为星期的开始
# %w  星期（0-6），星期天为星期的开始
# %W  一年中的星期数（00-53）星期一为星期的开始
# %x  相应的日期表示
# %X  相应的时间表示
# %z  当前时区的名称
# %%  %号本身

import  time

# if __name__ =="__main__":
#
#     #先看下当前默认格式化的时间
#
#     localtime =time.asctime(time.localtime())
#     print('当前默认日期时间格式：%s' % localtime)
#
#     #格式化为：年月日 时分秒星期几
#     print("24小时制格式：",time.strftime("%Y-%m-%d %H:%M:%S %A",time.localtime()))
#     print("12小时制格式：",time.strftime("%Y-%m-%d %I:%M:%S %a",time.localtime()))
#
#     #带a.m,p.m 标识时间格式 %p
#     print('带a.m,p.m 24小时制全格式：', time.strftime("%Y-%m-%d %H:%M:%S %p %A",time.localtime()))
#
#     #把时区也带上 %z
#     print("带时区的全格式：",time.strftime("%Y-%m-%d %H:%M:%S %p %A %z",time.localtime()))
#
#


import calendar

cal = calendar.month(2018,1)
print('输出2018年1月份的日历：')
print(cal)





