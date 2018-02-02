# x = 1.68
# y  = 10
# print(int(x))
# print(float(y))
# print(complex(x)) # 将x,y(下面一个) 转换为复数，实部为x，虚部为y
# print(complex(y))

import math
import cmath
import random
x = -100
y = 2.0
print(abs(x))   # 返回x的绝对值
print(max(x,y)) # 返回x,y中的最大值(最小值)
print(min(x,y))
print(pow(y,3)) # 计算y的三次方
print(math.sqrt(y)) # 返回平方根(2的平方根)

a = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(a)) # 从列表中随机选取一个数
print(random.randrange(2,100,5))    # 在指定的范围内，按照5递增取随机数
print(random.random())    # 在(0,1)之间生成一个随机数

# 三角函数
print(cmath.acos(x))
print(cmath.sin(x))
print(cmath.cos(x))
print(cmath.pi) # 返回π
