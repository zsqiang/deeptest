#coding=utf-8
import time

from   checkip import *

def Time(func):

    def wap(args):
        print time.time()

        ret = func(args)
        return ret
    return wap

@Time
def api_test(file_dir):

    with open(file_dir) as f:
        for ip in f:
            ip=ip.strip()

            result=permisscheck(ip)

            report= "ip:%s==============result:%d"%(ip,result)
            with open("report.txt","a") as f:
                strtime=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                f.write(strtime+" -- "+report+"\n")

# strtime=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
# print strtime

