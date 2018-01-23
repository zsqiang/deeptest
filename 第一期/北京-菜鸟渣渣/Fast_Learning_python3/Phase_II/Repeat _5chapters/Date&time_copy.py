# coding=utf-8

from datetime import datetime
from datetime import date
from  datetime import time
from  datetime import timedelta
from datetime import tzinfo

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

if __name__ == "__main__":

    today=datetime.today()
    today.strftime("%Y-%m-%d %H:%M:%S")
    print(today)

    '''
    Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。

    Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
    
    时间间隔是以秒为单位的浮点小数。
    
    每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
    
    Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:
    '''
    print(help(time))