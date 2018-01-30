
#coding=utf-8
def checkIp(ip):

    ips=ip.split(".")
    #print ips
    flag=False
    L=len(ips)
    if L==4:
        for i in ips:
            if i.isdigit() and  0<=int(i)<=255:
                flag=True
            else:
                flag=False
                break


    #result="%s ip is egal>>> "%ip +str(flag) if flag else "%s ip is illegal>>> "%ip+str(flag) 
    #return ip
    result= True if flag else False
    return result

#print checkIp("127.0.0.10")




#权限读取方案
def permissioncheck(input_ip="127.0.0.1"):
    #文本读取
    file=open("ips.txt",'r')
    files=file.readlines()
    flag1=True
    ips=[]
    #while flag1:
	    
    #input_ip = raw_input("please input a ip :")
    for ip in files:
        if ip:
            Cip = checkIp(ip.strip())
            ips.append(ip.strip())
    if input_ip in ips:
        return {"ip": input_ip, "code": 200}
    else:
        return {"ip": input_ip, "code": 403}

    print ips
						 
    file.close()
    
ip="127.0.0.1"
if checkIp(ip):
    print permissioncheck(ip)


#权限读取方案1
'''
def permitIP1():
    #文本读取
    file=open("ips.txt",'r')
    files=file.readlines()
    flag1=True
    ips=[]
    while flag1:
        input_ip=raw_input("please input a ip :")
        for ip in files:
            Cip=checkIp(ip.strip())
            ips.append(Cip)
            #print Cip
            if Cip.strip()==input_ip:
                print {"ip":Cip,"code":200}
            else:
                print {"ip":Cip,"code":403}
        print ips
    file.close()
    
    
permitIP1()
'''
#方案1
'''
flag1=True
while flag1:
    ip=raw_input("please input a ip：")
    checkIp(ip)
    pps=raw_input("please input Y&y to continue :")
    if pps=='Y' or pps=='y':
        flag1=True
    else:
        break
'''
#方案2
'''
flag1='Y'
while flag1=='Y' or flag1=='y':
    ip=raw_input("please input a ip：")
    checkIp(ip)
    flag1=raw_input("please input Y&y to continue :")
'''
