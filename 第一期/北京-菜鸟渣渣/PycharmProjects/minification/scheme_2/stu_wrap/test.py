#coding=utf-8

from checkip import checkip, permissioncheck
import  time
def func(*args,**kwargs):
    print args,kwargs
func(1,2,3,4,5,6,7,a="A",b="B")

def Time():
    def wrap(fun):
        def _wrap():
            print  time.ctime()
            k=fun()
            time.sleep(2)
            print k
            print time.ctime()
        return _wrap
    return wrap
@Time()
def check():
    ip = "127.0.0.1"
    if checkip(ip):
        p = permissioncheck(ip)
        print p.keys()
        print p.values()
        return  p.get("code")



check()
