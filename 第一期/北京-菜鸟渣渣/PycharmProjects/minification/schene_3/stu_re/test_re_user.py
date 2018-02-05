#coding=utf-8
import re

p={}
phones=[]
with open("user_ip_agent20160202.txt") as f:
    for line in f:
        # print line

        ua= " ".join(line.strip().split(",")[:-1])
        s=int(line.strip().split(",")[-1])
        # print s
        # u = re.search("zh-[cnCNtw]+;\s(.+)\sBuild", ua)
        u=re.search("zh-[cnCNtw]+;\s(.+)\sBuild",ua)
        # print u.groups()
        # '''
        if u:
            phone=u.groups()[0]
            if not p.get(phone):
                p[phone] = s
            else:
                p[phone]=s+p[phone]

                phones.append(phone)
print  phones

for k , v in p.iteritems():
    print k,v

sorts=sorted(p.iteritems(),key=lambda  e:e[1] ,reverse=True)

print  sorts
index=0
for i in sorts:
    index+=1
    print  i
    if index ==5:
        break