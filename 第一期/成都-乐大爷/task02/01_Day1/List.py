# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
参考资料：http://www.runoob.com/python3/python3-list.html
序列都可以进行的操作包括索引，切片，加，乘，检查成员
"""
# 访问列表元素
# 更新列表元素
# 删除列表元素

list1 = [ i for i in range(10)]
print(list1[0:4], "    ", list1[3])
list1[3] = 'she'
print(list1)
del list1[3]
print(list1)

# 切片-- [start:end:step]
print(list1[-3])    # 倒数第3个元素
print(list1[::-1])  # 反转排序
print(list1[1::3])

# 列表函数
# len()\max()\min()\list(seq)

# 列表方法
# list.append(obj)：在列表末尾添加新的对象
# list.count(obj)：统计某个元素在列表中出现的次数
# list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list2 = ['a', 'b', 'c']
list1.extend(list2)
print(list1)

# list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)：将对象插入列表
# list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list1.pop(-2))

# list.remove(obj):移除列表中某个值的第一个匹配项
# list.reverse()：反向列表中元素
# list.sort([func])：对原列表进行排序
# list.clear()：清空列表.列表依然存在，只是为空
# list.copy()：复制列表

