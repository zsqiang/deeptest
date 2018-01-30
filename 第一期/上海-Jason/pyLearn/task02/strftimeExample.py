# _*_ coding : utf-8 _*_
__author__ ="Jason"

'''
日期有很多种格式，格式间的转换需要用到strftime函数。
先看下可用于格式化日期时间的符号：
    %y          两位数的年份表示（00-99）
    %Y          四位数的年份表示（000-9999）
    %m          月份（01-12）
    %d          月内中的一天（0-31）
    %H          24小时制小时数（0-23）
    %I          12小时制小时数（01-12）
    %M          分钟数（00-59）
    %S          秒（00-59）
    %a          简写的星期名称（Mon）
    %A          完整的星期名称（Monday）
    %b          简写的月份名称（Jan）
    %B          完整的月份名称（January）
    %c          相应的日期表示和时间表示
    %j          年内的一天（001-366）
    %p          A.M或P.M的等价符
    %U          一年中的星期数（00-53），星期天为星期的开始
    %w          星期（0-6），星期天为星期的开始
    %x          相应的日期表示
    %X          相应的时间表示
    %z          当前时区的名称
    %%          %号本身
'''
import time

if __name__ == "__main__":
    #先看下当前默认格式化的时间
    localtime_now = time.asctime(time.localtime())
    print("当前默认日期时间格式：%s"%localtime_now)#当前默认日期时间格式：Tue Jan 23 14:32:21 2018

    #格式化为：年-月-日 时：分：秒 星期几
    print("24小时制全格式：",time.strftime("%y-%m-%d %H:%M:%S %A"))#23小时制全格式： 18-01-23 15:37:11 Tuesday
    print("12小时制缩写格式：", time.strftime("%Y-%m-%d %I:%M:%S %a"))  # 12小时制缩写格式： 2018-01-23 03:52:05 Tue
    print("24小时制全格式：", time.strftime("%y-%m-%d %H:%M:%S %A"),time.localtime())
    #24小时制全格式：
    #  18-01-23 15:38:47 Tuesday
    #  time.struct_time(tm_year=2018, tm_mon=1, tm_mday=23, tm_hour=15, tm_min=38, tm_sec=47, tm_wday=1, tm_yday=23, tm_isdst=0)

    #带上AM或PM标识时间格式
    print("24小时制带上AM或PM格式：",time.strftime("%Y-%m-%d %H:%M:%S %p %a"))
    #24小时制带上AM或PM格式： 2018-01-23 16:08:27 PM Tue

    #再带上时区
    print("12小时制带上AM或PM标识，并带上时区：",time.strftime("%Y-%m-%d %I:%M:%S %p %z %A %j %x %X"))
    #12小时制带上AM或PM标识，并带上时区： 2018-01-23 04:11:18 PM +0800 Tuesday 023 01/23/18 16:11:18

