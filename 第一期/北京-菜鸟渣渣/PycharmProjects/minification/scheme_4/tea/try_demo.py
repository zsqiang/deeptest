#coding=utf-8

import  re
try:
    a="jhjhj"
    u=re.search("\d",a).groups()

except   AttributeError as e:
    print e
print  'hello'
