# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
tuple为什么是不可变的？
参考资料：http://www.runoob.com/python3/python3-tuple.html
"""

# 创建元组
t1 = (10)   # 结果为整数
t2 = (10,)  # 结果为元组
t3 = ()     # 空元组

# 访问元组，下标或切片
tup1 = ('enhanced', 'deactivated', 2010, 2018)
tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("tup1[1]:", tup1[1])
print("tup2[1:4]:", tup2[1:4])      # 左闭右开

# 修改元组：当元组的元素是不能修改的，但是元素是可变的，则可修改可变的元素，但不会改变元组本身的地址
tup3 = (1, 2, ['A', 'B'])
tup4 = tup1 + tup2
tup3[2][1] = 'C'
print(tup3)
print(tup4)

# 删除元组：元组中的元素是不能被删除的，但能删除整个元组
del tup4

# 元组运算符： +、*、len()、迭代、

# 元组内置函数
# len():计算元组长度
# max():返回元组中元素的最大值
# min():返回元组中元素的最小值
# tuple(seq):列表转换为元组

list1 = [i for i in range(1,10)]
print(list1)
print(tuple(list1))

# 元素判断和遍历
result = 3 in tup2
print(result)