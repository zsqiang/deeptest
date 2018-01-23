#--coding:utf-8--
#关于函数

#求序列的和
def summ(seq):
    sum=0
    for i in seq:
        sum=sum+i
    return sum

#给一个数,算其乘法表 如九九乘法表
#   x为要算哪个数字的乘法表
def mult(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print("%s * %s=%d"%(j,i,i*j) )

if __name__=="__main__":
    #求和
    sum_1=summ([1,2,3,4,5])
    print(sum_1)

    #打印九九乘法表
    mult(9)