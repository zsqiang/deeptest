#coding=utf-8
import re
d={}
with open("user_ip_agent20160202.txt","r") as f:
    for line in f:
        #截取
        line=line.strip().split(",")
        ua=",".join(line[:-1])
        s=int(line[-1])
        u=re.search("zh-[cnCNtw]+;\s(.+)\sBuild",ua)

        if u:
            p=u.groups()[0]
            if not d.get(p):
                d[p]=s
            else:
                d[p]=d[p]+s

dd=sorted(d.iteritems(),key=lambda e:e[1],reverse=True)
# print dd
with open("phones.txt","a") as f:
    for i in range(10):
        # print dd[i]
        f.write(dd[i][0]+"............"+str(dd[i][1])+"\n")


#test
if __name__ == '__main__':
    ua = "中国移动+zh-C; +cc Build"
    u = re.search("zh-[cnCNtw]+;\s(.+)\sBuild", ua)
    print  u.groups()