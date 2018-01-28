# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
参考资料：http://www.runoob.com/python3/python3-dictionary.html
字典:可变容器模型，且可存储任意类型对象。
{key: value}:key值必须唯一。
字典特性的说明：
1.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住；
2.键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""
# 创建字典
dict1 = {'a': 97, 'b': 98}
print(dict1['a'])

# 修改字典
dict1['a'] = 'A'
print(dict1)

# 删除字典
del dict1['a']  # 删除字典键
print(dict1)
dict1.clear()   # 清空字典
print(dict1)

# 字典内置函数
# len()\str(dict)\type(variable)
dict2 = {'a': 97, 'b': 98, 'c': 99}
print(len(dict2))
print(str(dict2))
print(type(dict2))

# 字典的方法
# dict.clear()：删除字典内所有元素
# dict.copy()：返回一个字典的浅复制，深复制父元素、浅复制子元素
# dict.fromkeys()：创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
seq = ['a', 'b', 'c']
dict3 = dict.fromkeys(seq)
print(dict3)
dict4 = dict.fromkeys(seq, [97, 98, 99])
print(dict4)

# dict.get(key, default=None):返回指定键的值，如果值不在字典中返回default值
print(dict3.get('d', 100))

# dict.items():以列表返回可遍历的(键, 值) 元组数组
print(dict4.items())

# dict.keys():以列表返回一个字典所有的键
print(dict4.keys())

# dict.setdefault(key, default=None):和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
print(dict3.setdefault('d', 100))
print(dict3)

# dict.update(dict2):把字典dict2的键/值对更新到dict里
dict_n = {'bec': ['vantage', 'high'], 'cet': ['cet-4', 'cet-6']}
dict_o = {'info': ['name', 'age']}
dict_n.update(dict_o)
print(dict_n)

# dict.values():以列表返回字典中的所有值
# pop(key[,default]):删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# popitem():随机返回并删除字典中的一对键和值(一般删除末尾对)。
l = dict_n.popitem()
print(l)
print(dict_n)