# sum = 0
# for index in range(1,100):
#     sum = sum +index
# print(sum) # 注意 print()的位置  如果不缩进就是打印总的和，如果缩进就是计算每一个加的和
#
'''
import random
# random.randint(10,100) # 0到1之间的随机数[0,1)
a = random.randint(10,100)  # 10到100之间的随机数
print(a)
'''
def zhan(a):
    a,b,count = 0,1,0
    while True:
        if count > n:
            return
        a,b =b,a+b
        count = count +1

f = zhan(10)
while True:
    try:
        print(next(f),end ='')
