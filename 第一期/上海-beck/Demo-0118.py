# -*- coding:utf-8 -*-
import calendar
import os
#from datetime import date, datetime, time
import time

import datetime

import pytz as pytz

__author__ = 'beck'

# def Walk_dir(target_dir):
#     walk_result = os.walk(target_dir)
#     print(type(walk_result))
#
#     for root,dirs,files in walk_result:
#         print("-",root)
#         for dirone in  dirs:
#             print(" --",dirone)
#         for file in  files:
#             print(" --",file)
#
# if __name__ == '__main__':
#     print("获取当前工作目录：")
#     print(os.getcwd())
#     print("获取当前目录：")
#     print(os.curdir)
#     #os.mkdir("Test For Python")
#     #os.rename("Test For Python","Test001")
#     #os.removedirs("Test001")
#     print("改变文件目录：")
#     os.chdir("C:")
#     print(os.getcwd())
#
#     path = __file__
#     print("当前文件路径：%s"% path)
#     #是目录则返回Ture 不是返回Flase
#     print("文件是否为目录:%s"%os.path.isdir(path))
#     #是文件则返回True 不是返回Flase
#     print("是否为文件：%s"%os.path.isfile(path))
#     #判断目录或者文件是否存在
#     print("文件或者目录是否存在：%s" %os.path.exists(path))
#     #获取到文件大小
#     print("获取到文件大小：%s" %os.path.getsize(path))
#     #获取到文件的绝对路径
#     print("文件绝对路径 %s" % os.path.abspath(path))
#     #将目录路径规范化，用于跨平台
#     print("文件路径规范化：%s" % os.path.normpath(path))
#     #文件名和目录分割
#     print("文件名和目录进行分割：",end="")
#     print(os.path.split(path))
#     #文件名和扩展名分割
#     print("文件名和扩展名分割：",end="")
#     print(os.path.splitext(path))
#     #获取文件名称
#     print(os.path.basename(path))
#     #获取文件名所在目录
#     print(os.path.dirname(path))
#     target_dir = os.curdir
#     Walk_dir(target_dir)

#19月号练习
#关于时间和日期的练习
if __name__ == '__main__':
#     today = date.today()
#     print(today)
#     print("今天的日期: %s-%s-%s" %(today.day,today.month,today.year))
#     #0-6分别表示为周一到周日
#     week_num = today.weekday()
#     print("今天weekda是 %s"% week_num)
#     weekdays = ("Monday", "Tuesday", "Wednesday",
#                 "Thursday", "Friday", "Saturday", "Sunday")
#     print("今天weekda是 %s"% weekdays[week_num])
#     print("-"*30)
#     #输出现在时间
#     today_now = datetime.now()
#     print(today_now)
#     #构造一个时间
#     mytime = time(hour=20,minute=30,second=40,microsecond=567756)
#     print(mytime)
#     #构造一个年月日
#     myyear= datetime(year=2018,month=11,day=18,hour=20,minute=31,second=29)
#     print(myyear)
    #打印当前时间
    localtime = time.asctime(time.localtime())
    print(localtime)

    # print("24小时制的时间:",time.strftime("%Y-%m-%d %H-%M-%S %A",time.localtime()))
    # print("12小时制的时间:",time.strftime("%Y-%m-%d %I-%M-%S %a",time.localtime()))
    # print("带有a.m或者p.m的时间：",time.strftime("%Y-%m-%d %H-%M-%S %A %p"),time.localtime())
    # print("带有时区的时间输出：",time.strftime("%Y-%m-%d %H-%M-%S %a %p %z"),time.localtime)
    # print("时间信息：",time.strftime("%j",time.localtime()))
    # print("相应的日期和时间表示：",time.strftime("%c",time.localtime()))
    # print("一年中的第几个星期：",time.strftime("%U",time.localtime()))
    # print("一年中的第几个星期：",time.strftime("%W",time.localtime()))
    # print("今天是星期几：",time.strftime("%w"),time.localtime())
    # print("相应的日期表示：",time.strftime("%x"),time.localtime())
    # print("相应的时间表示：",time.strftime("%X"),time.localtime())
    # print("输出时间戳：",time.time())
    # print("将struct_time转换为时间戳：",time.mktime(time.localtime()))

    #calendar模块
    # print(calendar.weekday(2018,1,15))
    # #cal = calendar.month(2018,1)
    # #print("打印出2018年1月日历：")
    # #print(cal)
    # print("start: %s"% time.ctime())
    # time.sleep(5)
    # print("end: %s"% time.ctime())

    now = datetime.datetime.now()
    yestoday = now - datetime.timedelta(days=1)
    print(yestoday)
    tommrow = now  + datetime.timedelta(days=1)
    print(tommrow)
    new_year = now + datetime.timedelta(days=365)
    print(new_year)

    print( pytz.country_timezones("cn"))
    tz = pytz.timezone('Asia/Shanghai')
    print(datetime.datetime.now(tz))