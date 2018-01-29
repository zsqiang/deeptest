__author__="大霞"
#日期和时间处理
#JSON解析
"""
在python中， date、time、datetime类提供了一系列处理日期、时间和时间间隔的函数
date--可以处理日期（年、月、日）
time--可以处理时间（时、分、秒、毫秒）
datetime--可以处理日期和时间的组合（年、月、日、时、分、秒、毫秒）
timedelta--日期时间处理，可以用于时间运算等
tzinfo--时区处理
"""
from datetime import date
from datetime import time
from datetime import datetime
import time
if __name__=="__main__":
    today=date.today()
    print("今天是：%s"% today)
    #把今天的日期分开显示
    print("今天是：%s %s %s"%(today.day,today.month,today.year))
    date_time_now=datetime.now()
    print(date_time_now)#获取当前日期和时间
    time_now=datetime.now().time()#获取当前时间
    print(time_now)
    # #用time函数来构造时间
    # t=datetime.time(hour=12,minute=20,second=22,microsecond=21)
    # print(t)
    #构造个日期时间
    d=datetime(year=2018,month=2,day=14,hour=10,minute=3,second=14)
    print(d)

    #格式化日期时间：strftime函数
    """
    strftime函数，格式化日期时间的符号：
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
    """
    #先查看当前默认格式化显示的时间
    localtime=time.asctime(time.localtime())
    print("当前默认日期时间格式是：%s"% localtime)
    # 格式化为： 年-月-日 时:分:秒 星期几
    print("24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %A",time.localtime()))
    print("12小时制缩写格式：", time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime()))
    #带a.m 或p.m标识时间%p
    print("带a.m 或p.m24小时制全格式：",time.strftime("%Y-%m-%d %H:%M:%S %p %A",time.localtime()))
    # 把时区也带上看看 %z
    print("带时区的全格式：",
          time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))
    # 格式乱排下试试
    print("随意排格式：",
          time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))