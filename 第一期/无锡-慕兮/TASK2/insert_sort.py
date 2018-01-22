# -*- coding:utf-8 -*-
__author__ = "Lakisha"

import random

'''
公众号：开源优测
'''

#随机生成1-1000之间的无序序列整数数据
def generator():
    data_list = []
    for i in range(0, 10):
        data_list.append(random.randint(1, 1000))
    return data_list

def insert_sort(data_list):
    #序列长度
    length = len(data_list)
    for i in range(1, length):
        key = data_list[i]
        j = i -1
        while j >= 0:
            #比较，进行插入排序
            if data_list[j] > key:
                data_list[j+1] = data_list[j]
                data_list[j] = key
            j = j -1
    return data_list

if __name__ == "__main__":
    print("开源优测-积微速成计划基本功")

    #生成随机无需数据
    queue = generator()

    #打印无序数列
    print(queue)

    #插入排序
    length = len(queue)
    sorted_data = insert_sort(queue)

    #打印排序结果
    print(sorted_data)