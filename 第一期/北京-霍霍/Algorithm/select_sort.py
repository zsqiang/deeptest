# -*- coding:utf-8 -*-

__author__ = "huohuo"

import random

"""
选择排序工作原理是每一次从待排序列的数据元素中选出最小(或最大)元素，存放在起始位置，直至全部待排序数据元素排完。
"""

def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data

# 选择排序
def select_sort(data_list):
    length = len(data_list)

    for i  in range(0, length):
        min = i
        # 查找最小的元素
        for j in range(i+1, length):
            if data_list[j] < data_list[min]:
                # 找到最小的元素
                min = j

        # 交换位置
        data_list[min], data_list[i] = data_list[i] ,data_list[min]

    return data_list

if __name__ == "__main__":
   
   print("开源优测-积微速成计划基本功-选择排序")

   # 生成随机无序数据
   random_data = generator()

   # 打印无序数据
   print(random_data)

   # 插入排序
   lenght = len(random_data)
   sorted_data = select_sort(random_data)

   # 打印排序结果
   print(sorted_data)