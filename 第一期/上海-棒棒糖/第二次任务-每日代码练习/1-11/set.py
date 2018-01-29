#set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
set_source = set([1, 1, 2, 3, 4, 5, 6, 7])
set_demo = set('google')
set_list = set(['qwe', 'wer', 2, 2, 4, 5, 6, 7])
print(set_source)
print(set_demo)
print(set_list)

#add增加
set_demo.add(9)
print(set_demo)
#update 新增多个值
list_demo=['a','b','b']
set_demo.update(list_demo)
print(set_demo)
#删除
set_demo.remove(9)
print(set_demo)

