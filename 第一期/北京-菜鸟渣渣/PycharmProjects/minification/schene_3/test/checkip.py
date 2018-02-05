# coding=utf-8

import  time
#demo1
'''
def checkIP(ip):


    ips = ip.split(".")

    L = len(ips)
    flag = False
    if L == 4:
        for ip in ips:
            if ip.isdigit() and 0 <= int(ip) <= 255:
                flag = True
            else:
                flag = False
                break
        return flag

    else:

        return flag

# permission

def permission(ip):
    with open("ips.txt",'r') as f:
        files=f.readlines()
        ips=[]
        for ip1 in files:
            ips.append(ip1.strip())
        if checkIP(ip):
            if  ip is not  ips:
                return "{'msg':%s,'code':200}"%ip
            else:
                return  "{'msg':%s,'code':404}"%ip
        else:
            return "not ip"

def runtime():
    print(time.time())
    time.sleep(2)
    result=permission("127.0.0.1")
    print result
    print(time.time())

runtime()
'''

def checkIP():
    def _wrap(func):
        def __wrap(ip):

            ips = ip.split(".")

            L = len(ips)
            flag = False
            if L == 4:
                for ip2 in ips:
                    if ip2.isdigit() and 0 <= int(ip2) <= 255:
                        flag = True
                    else:
                        flag = False
                        break
            if flag:
                ret=func(ip)
            else:
                return 4031
            return  ret
        return __wrap
    return  _wrap

# permission
@checkIP()
def permission(ip):
    with open("ips.txt",'r') as f:
        files=f.readlines()
        ips=[]

        for ip1 in files:
            ips.append(ip1.strip())
        print ips
        if  ip not in  ips:
            return "{'msg':%s,'code':200}"%ip
        else:
            return  "{'msg':%s,'code':404}"%ip



ip="127.0.0.1"
print permission(ip)