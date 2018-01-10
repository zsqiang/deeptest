import math
import random

import cmath

if __name__ == "__main__":
    x=1.68
    y=10

    print(int(x)) #将浮点数转换为整数

    print(float(y)) #将整数转换为浮点数

    print(complex(x,y)) #将x,y转换为复数，实数部分为x，虚数部分为y

    #数值函数实例
    xx=-100
    yy=1.9

    #返回xx的绝对值
    print(abs(xx))

    #返回最大值
    print(max(xx,yy))

    #返回最小值
    print(min(xx,yy))

    #返回平方根
    print(math.sqrt(yy))

    print(u"常用随机函数")
    a=[1,2,3,4,5,6,7,8,9,0]

    #从列表中随机选中一个
    print(random.choice(a))

    #从指定的范围（2-100按5递增的数据集）中随机选中一个
    print(random.randrange(2,100,5))

    #生成一个随机数，它在（0,1）之间
    print(random.random())

    xxx=100

    #返回xxx的反余弦弧度值
    print(cmath.acos(xxx))
    #返回xxx的正弦弧度值
    print(cmath.sin(xxx))
    #返回xxx的余弦弧度值
    print(cmath.cos(xxx))