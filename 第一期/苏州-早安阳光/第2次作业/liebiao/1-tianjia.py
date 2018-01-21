'''
Created on 2018年1月21日

@author: 早安阳光
'''
number = [1,2,3,4,5,6]
# append() 添加元素
number.append(7)
print(number)
# extend() 向列表末尾添加多个元素
number.extend([8,9])
print(number)
# insert() 向列表某一个位置添加元素
number.insert(0, 0)
print(number)
number.append(11)
print(number)
number.insert(-1, 10)
print(number)


