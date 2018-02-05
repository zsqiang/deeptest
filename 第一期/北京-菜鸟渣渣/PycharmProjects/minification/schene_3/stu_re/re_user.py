# coding=utf-8

import re

p = {}
phones = []
with open("user_ip_agent20160202.txt") as f:
    for line in f:
        ua = " ".join(line.strip().split(",")[:-1])
        s = int(line.strip().split(",")[-1])

        u = re.search("zh-[cnCNtw]+;\s(.+)\sBuild", ua)
        print u
        if u:
            phone = u.groups()[0]

            if not p.get(phone):
                p[phone] = s
            else:
                p[phone] = s + p[phone]

                phones.append(phone)
print len(p)

for k,v in p.iteritems():
    print k,v

print "---------->"
print  "=================="*50

s1=dict(p.iteritems())
print type(s1)
print s1
ss=sorted(s1.items(),key=lambda e:e[0],reverse=True)

print  ss

