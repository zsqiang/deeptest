#--coding:utf-8-
#本折是关于日期时间处理.在py的datetime包中.常见的三个处理类:date time dattime
from datetime import date
from datetime import time
from datetime import datetime

if __name__=="__main__":
    #date类提供日期处理
    ##其类方法常有 today()
    ##其类属性有 max min等   实例属性有 year month day
    ##实例方法如 weekday() isoweekday() replace()

    #得到datetime允许的最大的日期和最小的日期
    print(date.max)
    print(date.min)
    #得到今天日期——年月日
    today_date=date.today()     #一个date对象
    print("今天日期是 %s" % today_date)

    #根据实例属性得到单独的年月日
    print("今天面月日分别是 %s %s %s" %(today_date.year,today_date.month,today_date.day))
    #根据实例方法算出今天星期几--返回对应的整数序号
    print(today_date.weekday())     #0-6
    print(today_date.isoweekday())  #1-7

    #将当前日期替换成目标日期
    print(today_date.replace(2002,12,12))

    #替换成string形式的日期
    print(today_date.ctime())

    #time属性方法和date很类似
    #构造一个time对象--hour<24 min<60 sec<60  microsec<1000000毫秒
    t=time(12,13,14,999)

    print("系统允许最大time %s" %t.min)
    print("系统允许最小time %s" %t.max)

    #获取单独的 时 分 秒 毫秒
    print("hour %s" % t.hour)
    print("minute %s" % t.minute)
    print("second %s" % t.second)
    print("microsecond %s" % t.microsecond)

    #替换成指定time
    t.replace(22) #可接受 小时 分 秒 毫米4个参数
    #生成string的time
    t.isoformat()