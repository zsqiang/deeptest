#coding=utf-8


def checkIp(ip):
    ips = ip.split(".")
    L = len(ips)
    loop = 0
    if L == 4:
        for i in ips:
            if i.isdigit() and 0 <= int(i) <= 255:
                loop += 1
            else:
                break
    if loop == 4:
        result = "%s is legal ip" % ip
    else:
        result = "%s is illlegal ip" % ip
    print result


checkIp("127.*.0.1")
