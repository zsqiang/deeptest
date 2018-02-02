#求素数
#方法1
def is_prime(n):
    if n<2:
        return False
    m = 2
    while m < n:
        if n % m == 0:
            return False
        m = m + 1
    return True

print(list(filter(is_prime, range(1, 101))))

#方法2 没有看懂
'''
lambda匿名函数
def f(x):
    return x**2
    print f(4)
Python中使用lambda的话，写成这样
g = lambda x : x**2
print g(4)
'''
#先构造一个从3开始的奇数序列：
def _odd_iter():
    n=1
    while True:
        n-n+2
        yield n

#定义一个筛选函数
def _not_divisible(n):
    return lambda x : x%n>0
#定义一个生成器，不断返回下一个素数
#先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列
def primes():
    yield 2
    it = _odd_iter()#初始序列
    while True:
        n=next(it) # next() 返回迭代器的下一个项目
        yield n
        it = filter(_not_divisible(n),it)

    for n in primes():
        if n <1000:
            print(n)
        else:
            break
a=primes()
print(a)



