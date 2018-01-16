import random

__author__ =u"大霞"

#自定义函数
def sum(a, b):
    c = a + b
    print(u"sum的值是: %d" % (c))
    return c
#四则运算加减乘除
if __name__ == "__main__":
    a=20
    b=2
    print(a+b)
    print(a*b)
    print(a/b)
    print(a-b)
    #调用自定义函数方法
    c=sum(a,b)



#随机生成100个10至1000之间的数，对100个数进行排序，禁止使用Python自带的排序函数，要实现自己的排序函数
#data = random.randint(10,1000)
num=0
data=[]
while(num<10):
    randomNum=random.randint(10,100)
 #   print(randomNum,end=',')
    num=num+1
    data.append(randomNum)
#print('')


print(data)

#冒泡排序，还不理解python的冒泡排序
for i in range(len(data)):
    for j in range(i):
        if data[j] > data[i]:
            data[j],data[i]=data[i],data[j]
print(data)


