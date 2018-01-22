# -*- coding:utf-8 -*-
__author__ = "huohuo"

import random
"""
快速排序通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另一部分小，然后再按此方
法对两部分数据分别进行快速排序。
快速排序是一种不稳定的排序算法，多个相同的值的相对位置会在算法结束时产生变动。
"""

# 随机生成1-1000之间无序序列整数数据
def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data

# 快速排序
def quick_sort(data_list, start, end):
    # 判断是否需要进行排序
    if start >= end:
        return data_list

    # 设置排序基准值，这里设为第一个元素值
    base = data_list[start]
    left = start
    right = end 
    while left < right:
        # 对data_list从右往左找第一个比base小的数的索引位置
        while left < right and data_list[right] >= base:
            right = right - 1

        # 对data_list从左往右找第一个比base大的数的索引位置
        while left < right and data_list[left] <= base:
            left = left + 1
        
        # 交换数据初步排序
        data_list[left], data_list[right] = data_list[right], data_list[left]

    # 把找到比base小的数据与base交换位置
    data_list[start], data_list[left] = data_list[left], data_list[start]

    # 进入下一轮排序
    quick_sort(data_list, start, left - 1)

    quick_sort(data_list, right + 1, end)

    return data_list

if __name__ == "__main__":
    print("开源计划-积微速成计划基本功-快速排序")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    length = len(random_data)
    sorted_data = quick_sort(random_data, 0, length - 1)

    # 打印排序结果
    print(sorted_data)