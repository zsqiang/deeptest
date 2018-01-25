# -*- coding:utf-8 -*-

__author__ = 'catleer'

# isdisjoint(other):判断2个集合中，是否有元素一致，若有，则返回false
set1 = set([1,2,3])
set2 = set([5,6,7])
set3 = set([3,4,5])
set4 = set([])
print(set1.isdisjoint(set2))    # 返回true
print(set1.isdisjoint(set3))    # 返回false
print(set1.isdisjoint(set4))    # 返回true

# issubset(other):set<=other,判断set中的所有元素是否在other中
print(set1.issubset(set3))
print(set1.issubset(set2))      # 返回false
set5 = set([1,2,3,4,5])
print(set1.issubset(set5))      # 返回true

# issuperset(other) :set>=other,判断other中的所有元素是否在set中
# union(*others) ：并集
print(set1.union(set2))

# intersection(*others) ：交集
print(set1.intersection(set3))

# 好头疼，把数学还给老师想不起名词了
# difference(*others) ：返回一个新的集合，集合元素为set中不在other中的值
# symmetric_difference(other) ：返回set和other中不相同的值，即交集剩下的部分
print(set1.symmetric_difference(set3))

# set的方法
# copy()
# update(*others) : 将others中的元素加到set中
set1.update(set2, set3)   
set2.update(['s', 'd'], {'a': 97, 'b': 98}) # 字典把键值加到set中了
print(set1)
print(set2)

# intersection_update(*others)：更新set,只保留set和other中相同的元素
# difference_update(*others) ：更新set，只保留set中没在other中出现过的元素
set1.difference_update(set2)
print(set1)

# symmetric_difference_update(other) ：更新set，保留set和other中都没有同时出现的元素

# add()\remove()\discard()\pop()\clear()
# discard():移除元素，如果元素存在
# remove():移除元素，若元素不存在，则报错：KeyError
# pop():移除元素，并返回元素，若set为空，则报错：KeyError