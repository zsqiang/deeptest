#--coding:utf-8--
#本折是关于生成器：generator
#一个函数中若存在 yield.那它不在是一个普通函数.而是生成器

#定义函数：给一个n值,生成小于n的整数
def num(n):
    a=0 #定义生成整数初始值
    while a<n:
        yield a #把要返回的值放在yield
        a=a+1

    return 'gone'

#定义一个genarator函数示例其如何执行
def carry():
    print(0)
    yield 1
    print(2)
    yield 2


if __name__=='__main__':
    x=num(7)    #生成0-6的整数
    while True:
        #此处没有捕获错误 会抛出
        print(next(x))  #要执行generator函数语句时,必须next()才会执行,遇到yeild暂停,下次执行next()从暂停处继续执行
                        #若不断执行next(),就不断计算返回值 直到最后一个满足要求的值,在执行抛出stopIteration错误

    #由于生成器可以执行next()并返回值.所以生成器 也可看做一个不单纯的迭代器.只不过这个迭代器是一个功能强大的函数

    r=carry()   #最好把上面错误捕获后再执行这个,否则试了下会妨碍该行
    #print(next(r))   试试没有该行或再写一行