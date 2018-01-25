# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
数据类型：Python标准库-内置类型-数据类型
int\float\complex
参考资料：http://www.runoob.com/python3/python3-number.html
1.整形的位运算：或、异或、与、左移、右移、非
2.
"""
import math


x = 1.1111
y = 2
a =-10
print(math.trunc(x))    # 去掉小数部分，保留整数
print(round(x,2))       # 保留小数点的位数
print(math.floor(x))    # 向下取整
print(math.ceil(x))     # 向上取整
print(math.exp(y))      # 返回e的y次幂
print(math.fabs(a))     # 返回a的绝对值，同内置函数abs()
print(math.log(y))      
print(max(1,4,5,8,10,3)) # 返回给定参数的最大值
print(math.modf(x))     # 返回x的小数部分和整数部分，整数部分以浮点型表示

# 随机函数
import random

print(random.choice((1,4,5,62,2,3)))    # 返回序列中随机的一个值

# 三角函数

import cmath

b = 100
print(cmath.acos(b))    # 返回b的反余弦弧度值
print(math.hypot(2,3))  # 返回欧几里德范数sqrt(x*x + y*y)。