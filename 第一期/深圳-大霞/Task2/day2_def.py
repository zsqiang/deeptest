"""
函数
函数就是一种代码组织方式，让你可以实现单一、或关联功能的封装，以便高复用
"""

#求和函数
def sum(a, b):
    c = a + b
    return c
#乘法表函数
def multi():
    data=[]
    for i in range(1,10):
        line=[]
        for j in range(i,10):
            line.append("%d * %d =%2d"% (i,j,i*j))
        data.append(line)
    return  data
#元组参数传递求和
def sum_tuple(seq):
    sum=0
    for i in seq:
        sum=sum+i
    return sum
#字符串参数传递，字符串连接
def str_join(str1,str2,str3):
    return str1+str2+str3
#列表参数传递
def sum_list(seq):
    sum=0
    for i in seq:
        sum=sum+i
    return sum
if __name__=="__main__":
    print("调用定义的函数，计算和")
    c=sum(1,2)
    print(c)
    print("调用九九乘法表函数")
    data=multi()
    for d in data:
        print(d)

    #调用元组参数传递
    tuple1=(1,2,3,4,5,6)
    sum=sum_tuple(tuple1)
    print("和为：%d"% sum)

    #调用字符串参数传递
    str1="大家好"
    str2="我的公众号是"
    str3="hello world"
    str=str_join(str1,str2,str3)
    print(str)

    #调用列表
    list_demo=[1,2,3,4,5,6]
    sum=sum_list(list_demo)
    print("sum_list和为:%d"% sum)