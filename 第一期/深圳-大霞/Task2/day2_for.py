"""
在Python中for循环可以遍历任何序列，例如元组、列表、字符串、字典、集合等等
for 变量 in 序列:
    # 代码块
else:

    # 代码块
    # 通常情况下，我们不用else
"""
if __name__=="__main__":
    tuple1=(1,2,3,4,5,6,7,8,9,0)
    for t in tuple1:
        print(t,end=" ")
    print(" ")
    list1=[1,2,3,4,5,6,7,8,9,0]
    for l in list1:
        print(l,end=" ")
    print(" ")
    #for遍历字典
    dict1={"Deeptest":"开源优测","python":"快学python"}
    for (key,value) in dict1.items():
        print("%s:%s"% (key,value))
    """
    结合range()函数使用 本节说明下如何结合range函数来使用。
    range(start, end, step)
    功能说明：以指定步长生成一个指定范围的数值序列
    参数说明： start: 数值序列的起始数值（默认为0） end： 数值序列的终止数值 step ： 数值序列中数值的间距（默认为1）
    注：range生成的序列半闭半开区间
    """
    for i in range(5):
        print(i,end=',')#0,1,2,3,4
    print(" ")#换行
    # 指定范围生成序列进行遍历
    for i in range(3,10):
        print(i,end=',')#3,4,5,6,7,8,9,
    print(" ")  # 换行
    # 带步长方式生成序列进行遍历
    for i in range(2,10,2):
        print(i,end=',')#2,4,6,8
    print(' ')
    #嵌套循环
    #九九乘法表
    for i in range(1,10):
        for j in range(i,10):
            print("%d * %d = %2d"% (i,j,i*j),end='  ')
        print(' ')
    #while和for循环  九九乘法表实例
    n=1
    while n<=9:
        for m in range(n,10):
            print("%d * %d =%2d"% (n,m,n*m),end="  ")
        print(' ')
        n=n+1
