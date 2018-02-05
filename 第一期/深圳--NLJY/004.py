'''
list_demo = [1,2,3,4,5,6,7,8,9,0]
print('内置函数处理list示例')
print(len(list_demo))   # 列表中元素的长度
print(max(list_demo)) # 最大元素
print(min(list_demo)) # 最小元素
print(tuple(list_demo)) # 列表转换为元组
'''
print('list方法代码示例')
list1 = [1,2,3,4,5,6,7,8,93,3,33,2,1,222]
list2 = [3,7,8,4,2]
list1.append(100)   # 列表中添加一个元素
print(list1)
list1.insert(1,100) # 列表中添加一个元素，指定位置处添加
print(list1)
print(list1.count(1)) # 统计1在列表list1中出现的次数
print(list2[3]) # 通过索引查询元素
print(list2.index(2)) # 通过元素返回 索引
print(list1.extend(list2)) #
print(list1+list2) # 两个列表连接
print(list1.pop()) # 删除最后一个元素
print(list1.remove(222)) # 删除具体的某个元素
del list1[1]    # 删除列表里具体的元素
print(list1)
list2.reverse() # 把列表反向 不能把这个式子赋给一个变量 赋给变量打印出来的就是none
print(list2)
list2.sort() # 对list2进行排序
print(list2)
a =list2.copy() # 把list2复制给a
print(a)
list2.clear() # 清空list2
print(list2)
# 有返回值的 如 list1.count(1),可以直接print(list1.count(1))
# 没有返回值的list1.append(100) 需要再次print(list1)   主要是看有没有返回值

