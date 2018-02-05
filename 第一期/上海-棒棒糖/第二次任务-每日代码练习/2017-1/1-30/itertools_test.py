'''
import itertools
natuals=itertools.count(1)
for n in natuals:
    print(n)
'''
'''

import itertools
cs=itertools.cycle('ABC')
for c in cs:
    print(c)
    
import itertools
ns=itertools.repeat('ABC',3)
for n in ns:
    print(n)
    
import itertools
natuals=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns)) #返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
'''
import itertools
for c in itertools.chain('ABC','XYZ'):
    print(c)

for key,group in itertools.groupby('AAAABBBBCCCCAAA'):
    print(key,list(group))

