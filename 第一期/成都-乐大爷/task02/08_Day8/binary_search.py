# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
二分查找：是对有序序列进行查找，
1）获取要查找的数据
2）将序列分为2部分，目标数据（g）分别与中间的数据（m）进行比较，m < g:在右半部分查找
3）将目标数据所在的部分再分为2块，中间的数与目标数据进行比较
4）直到找到或找不到为止
"""

def binary_search(seq, query):
    # 序列的起始索引
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2    # //为整除
        val = seq[mid]
        if val == query:
            return mid
        elif val < query:
            start = mid + 1
        else:
            end = mid - 1
        
    return None

def first_binary_search(seq, query):
    start, end = 0, len(seq) - 1

    # 实现first优先：找到中位数与目标数对比，中位数前一位数与目标数对比
    # 问题：mid==0放在后一个条件进行，会有溢出吗？
    while start <= end:
        mid = start + (end - start) // 2
        if (mid == 0 and seq[mid] == query) or (seq[mid] == query and seq[mid-1] < query):
            return mid
        elif seq[mid] < query:
            start = mid + 1
        else:
            end = mid - 1

    return None

def last_binary_search(seq, query):
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if (seq[mid] == query and mid == len(seq) - 1) or (seq[mid] == query and seq[mid+1] > query):
            return mid
        elif seq[mid] <= query: 
            start = mid + 1
        else:
            end = mid - 1

        print(mid)
    return None


if __name__ == "__main__":
    print("二分查找示例")

    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    print(seq)
    # print("---------二分查找--------")
    # print("找到第一次出现的位置：", 5, " 索引是： ", first_binary_search(seq, 5))

    print("---------二分查找--------")
    print("找到最后一次出现的位置：", 0, " 索引是： ", last_binary_search(seq, 0))

    # print("---------二分查找--------")
    # print("找到：", 13, " 索引是： ", binary_search(seq, 13))

    # print("---------二分查找--------")
    # print("找到：", 1, " 索引是： ", binary_search(seq, 1))

    # print("---------二分查找--------")
    # print("找到：", 25, " 索引是： ", binary_search(seq, 25))
