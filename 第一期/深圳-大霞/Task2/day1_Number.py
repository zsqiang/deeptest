"""
Number
在Python中支持三种不同类型的数值类型：

整型(int)
通常称为整型或整数，为正数或负数，不带小数点。在Python3中，整型没有限制大小，即亦可做long类型使用，所以在Python3中无显性的long类型

浮点型(float)
即带小数点的数值，也可以用科学计数法表示:

1.2e2 = 1.2 * 10^2 = 1201.2e2=1.2∗10
2
 =120

复数(complex)
由实数部分和虚数部分构成，表达式方式为： a + bj 或 complex(a, b), 其中a为实数部分，b为虚数部分。
"""
if __name__=="__main__":
    print("Number数据类型转换")
    x=1.68
    y=10

    print("将x1.68转换成整数：",int(x))

    print("将y10转换成浮点数：",float(y))

    print("将x1.68y10转换成复数：",complex(x,y))

"""
常用数值函数
数学函数
主要进行各种数学计算，例如计算绝对值、幂运算、平方根等等，主要定义在math模块中

随机数函数
主要用于随机数的处理，例如生成随机数主要定义在random模块中

三角函数
主要用于将数值转换为对应的三角弧度值，主要定义在cmath模块中

数学常量
Python中内置定义的数学常量，比如π
"""
import math
import cmath
import random
numX=-100
numY=1.9

#求X的绝对值
print("返回numX的绝对值：",abs(numX))
#求最大值
print("返回numX、numY的最大值：",max(numX,numY))
#计算y^2
print("返回y的2次方值：",pow(numY,2))

#求y的平方根
print("返回y的平方根：",math.sqrt(numY))

#随机返回列表中的一个数值
a=[1,2,3,4,5,6,7,8,9,0]
print("返回列表中的一个随机数：",random.choice(a))
#从指定的范围(2-100按5递增的数据集)中随机选中一个
print("返回2-100按5递增的数据中的随机数：",random.randrange(2,100,5))
#随机生成一个0-1之间的随机数
print("返回0-1之间的随机数：",random.random())

print("常用的三角函数")
x=100
#返回反余弦弧度值
print("返回余弦弧度值：",cmath.acos(x))
#返回正弦弧度值
print("返回正弦弧度值：",cmath.sin(x))
#返回余弦弧度值
print("返回余弦弧度值：",cmath.cos(x))
# 返回数学常量π
print("返回数学常量π",cmath.pi)




