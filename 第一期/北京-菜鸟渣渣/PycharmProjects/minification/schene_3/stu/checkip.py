# coding=utf-8

def checkip(func):
    def wrap(args):
        ips = args.split(".")
        L = len(ips)
        flag = False
        if L == 4:
            for i in ips:
                if i.isdigit() and 0 <= int() <= 255:
                    flag = True
                else:
                    flag = False

        else:
            pass
        if flag:
            ret = func(args)

        else:
            ret = 4031
        return ret

    return wrap

@checkip
def permisscheck(ip):
    with open("ips.txt", "r") as f:
        IP = []
        for i in f:
            i = i.strip()
            if i:
                IP.append(i)
    if ip in IP:
        return 403
    else:
        return 200



        # ip="127.0.0.10"
        # print permisscheck(ip)
        # checkip(ip)
