# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    def product_rule(x,y):
        return x*y
    return reduce(product_rule,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')  #利用 index() 函数确定字符串 S 中 ‘.’的位置
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1)+reduce(fn,s2)/10**len(s2) #m**n 这个表达的就是 m 的 n 次方。
print('str2float(\'123.456\') =', str2float('123.456'))





