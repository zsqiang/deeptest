# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
概述
    选择排序是一种简单直观的排序算法。
    它的工作原理是每一个从待排序的数据元素中选出最小（或者最大）的一个元素，存放在序列的起始位置，
    直到全部待排序的数据元素排完。
基本过程
    n个记录的文件的直接选择排序可经过n-1趟直接选择排序得到有序结果：
    1.在未排序序列中招傲最小（大）元素，存放到排序序列的起始位置。
    2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3.以此类推，直到所有元素均排序完毕。
'''
import random

def generator():
    random_data = []
    for i in range(1,10):
        random_data.append(random.randint(1,1000))
    return random_data

def selection_sort(data_list):
    lengh = len(data_list)

    for i in range(0,lengh):
        minn = i
        #查找最小元素
        for j in range(i+1,lengh):
            if data_list[j] < data_list[minn]:
                minn = j
        #互换
        data_list[minn],data_list[i] = data_list[i],data_list[minn]
    return data_list

if __name__ == "__main__":
    random_data = generator()
    print(random_data)
    sorted_data = selection_sort(random_data)
    print(sorted_data)
