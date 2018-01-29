#coding=utf-8

# from checkip import  *
from checkip_decorate import checkip, permissioncheck

import  time

def Time():
    def wrap(fun):
        def _wrap(ip):
            print time.ctime()
            ret = fun(ip)

            print time.ctime()
            print ret
        return  _wrap
    return  wrap


@Time()
def Check(ip):
    # ip="127.0.0.1"
    # if checkip(ip):
    p= permissioncheck(ip)
    print p.keys()
    print p.values()
    if p.get("code"):
        k=p['code']
    return k
        # print p.get("code")
        # print p.has_key("code")
        # print p["code"]

with open("ip.txt") as f:
    for ip in f:
        ip =ip.strip()
        Check(ip)

#decorate 装饰器
'''
def Time(fun):
    print time.ctime()
    k=fun()
    print k
    time.sleep(10)
    print time.ctime()
Time(Check)
'''