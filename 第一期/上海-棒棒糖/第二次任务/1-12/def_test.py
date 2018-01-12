def sum(a,b):
    c=a+b
    return c
if __name__=="__main__":
    print("函数调用，计算a+b的和")
    c=sum(5,6)
    print(c)

#九九乘法表
__author__='棒棒糖'
def multi():
    data=[]
    for i in range(1,10):
        line=[]
        for j in range(i,10):
            line.append('%d*%d=%d'%(i,j,i*j))
        data.append(line)
    return data
print('九九乘法表')
data=multi()
for d in data:
    print(d)

#元组传递
def sum_tuple(seq):
    sum=0
    for s in  seq:
        sum+=s
    return sum
print('元组传参，求和')
tuple_1=(1,89,4,2,57,82)
print(tuple_1)
sum=sum_tuple(tuple_1)
print('和为:%d'%sum)

#字符串传递
def str_join(str1,str2,str3):
    return str1+str2+str3
str1='棒棒糖'
str2='碰'
str3='一个'
str_j=str_join(str1,str2,str3)
print(str_j)