# coding = utf - 8

# version 1:

# coding=utf-8
def CheckIp1(ip):
    # ip = "127.0.0.1002"
    ips = ip.split(".")
    L = len(ips)
    loop = 0
    if L == 4:
        for i in ips:
            if i.isdigit():
                if 0 <= int(i) <= 255:
                    loop = loop + 1
                    # print ip
                else:
                    break
            else:
                break
    else:
        pass

    if loop == 4:
        print ip + "  is legal ip"
    else:
        print ip + " is illegal ip"


# version 2
def CheckIp(ip):
    # ip = "127.0.0.100"
    ips = ip.split(".")
    L = len(ips)
    # loop = 0
    flag = False
    if L == 4:
        for i in ips:
            if i.isdigit() and 0 <= int(i) <= 255:
                # loop += 1
                flag = True
            else:
                flag = False
                break

    # result = "%s  is legal ip" % ip if loop == 4 else "%s is illegal ip" % ip
    result = "%s  is legal ip >>>" % ip +  str(flag) if flag else "%s is illegal ip >>>" % ip  +str(flag)
    print result

    '''
    if loop == 4:
        print  "%s  is legal ip" % ip
    else:
        print  "%s is illegal ip" % ip
    '''


# ip = "127.0.0.265"
'''
flag1="Y"
while flag1=="Y" or flag1 =="y":

    ip=raw_input("please input an ip :" )
    CheckIp(ip)
    flag1 = raw_input("Continu ? please input Y:")
'''

f = open("ips.txt", "r",)
files = f.readlines()
f.close()
for ip in files:
    ip = ip.strip()
    CheckIp(ip)



