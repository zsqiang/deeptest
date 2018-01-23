# -*- coding:utf-8 -*-
__author__ = "huohuo"

import random

"""
冒泡排序原理：比较相邻元素，如果第一个比第二个大就交换，对每一对相邻元素做同样工作，
最后的元素是最大的元素。重复比较除了最后一个，直至没有数据需要对比
"""

# 随机生成无序序列

def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data

# 冒泡排序
def bubble_sort(data_list):
    # 序列长度
    lenght = len(data_list)

    for i in range(0, lenght):
        for j in range(i + 1, lenght):
            if data_list[i] > data_list[j]:
                data_list[i], data_list[j] = data_list[j], data_list[i]

    return data_list

if __name__ == "__main__":
    print("开源优测-积微速成计划基本功-冒泡排序")

    # 生成无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    sorted_data = bubble_sort(random_data)

    # 打印排序结果
    print(sorted_data)