# coding=utf-8

def checkip():

    def _wrap(func):
        def __wrap(ip):
            ips = ip.split(".")
            L = len(ips)
            loop = 0
            if L == 4:
                for i in ips:
                    if i.isdigit() and 0 <= int(i) <= 255:
                        loop += 1
                    else:
                        break
            if loop==4:
                ret = func(ip)
            else:
                ret ={"code":4031,"msg":"illagel"}
            return  ret
        return __wrap
    return _wrap

@checkip()
def permissioncheck(ip="127.1.0.111"):
    f=open("ips.txt","r")
    files=f.readlines()
    # print  files
    f.close()
    ips=[]
    for i in files:

        if i:
            ips.append(i.strip())

    if ip in ips:
        return  {"code":403,"msg":"permission "}
    else:
        return  {"code":200,"msg":"OK "}

'''
if __name__ == '__main__':

    ip="127.0.0.1"
    if checkip(ip):
        p= permissioncheck(ip)
        print p.keys()
        print p.values()
        print p.get("code")
        print p.has_key("code")
        print p["code"]
'''