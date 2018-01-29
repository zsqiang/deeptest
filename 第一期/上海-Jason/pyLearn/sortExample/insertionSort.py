# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
插入排序

什么是插入排序？
    插入排序的基本操作是讲一个数据插入到已经排序好的有序序列中，从而获得一个新的有序序列。
插入排序适合什么样的场景？
    适合数据量相对较小的排序需求场景。其时间复杂度为：O(n^2)，是一种稳定的排序方法。

PS，个人觉得比较猥琐，算法和冒泡/沉底类似。
'''

import random


def generator():
    random_data = []
    for i in range(0,10):
        random_data.append(random.randint(1,1000))
    return random_data

def insertion_sort(data_list):
    lenght = len(data_list)
    for i in range(1,lenght):
        #print(data_list)
        key = data_list[i]
        j = i - 1
        while j >= 0:
            if data_list[j] > key:
                data_list[j+1] = data_list[j]
                data_list[j] = key
            j = j - 1
    return data_list

if __name__ == "__main__":
    random_data = generator()
    print(random_data)
    sorted_data = insertion_sort(random_data)
    print(sorted_data)