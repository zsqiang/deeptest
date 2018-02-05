#coding=utf-8

from __future__ import print_function

if __name__ == "__main__":
    tuple_1 = (0,4,3,2,5,6,7)
    list_1 = ['a','b','c']
    dict_1 = {"key1":"one","key2":"two","key3":"three"}

    print("遍历打印元组")
    for i in tuple_1:
        print(i,end=',')
    print('') #换行

    print("遍历打印列表")
    for j in list_1:
        print(j,end=',')
    print('')

    print("遍历打印字典(方式一)")
    for (key,value) in dict_1.items():
        print("%s:%s"%(key,value))
    print('')

    print("遍历打印字段（方式二）")
    for key in dict_1:
        print("%s:%s"%(key,dict_1[key]))
    print('')

    print("rang for 循环实例")
    for i in range(5):
        print(i, end=',')
