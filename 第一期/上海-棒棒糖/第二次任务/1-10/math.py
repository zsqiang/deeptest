__author__='棒棒糖'

import math
import random
import cmath

if __name__=='__main__':.
    x=-100
    y=1.9
    print('常用数学函数')
    #返回x的绝对值
    print(abs(x))
    #返回最大值
    print(max(x,y))
    #返回最小值
    print(min(x,y))
    #计算y2次方
    print(pow(y,2))
    #返回平方根
    print(math.sqrt(y))

    print('常用随机函数')
    a=[1,2,3,4,5,6,7,8,9,0]
    #从列表中随机选择一个数
    print(random.choice(a))
    #从指定的范围2,100按5递增中随机选择一个数
    print(random.randrange(2,100,5))
    #生成一个随机数在(0,1)之间
    print(random.random())
    print('常用三角函数')
    #反余弦弧度值
    print(cmath.acos(x))
    #正余弦弧度值
    print(cmath.sin(x))
    #余弦弧度值
    print(cmath.cos(x))
    print('数学常量')
    print(cmath.pi)
