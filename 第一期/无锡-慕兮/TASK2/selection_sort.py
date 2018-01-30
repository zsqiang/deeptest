# -*- coding:utf-8 -*-
__author__ = "Lakisha"

import random


def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))
    return random_data


def select_sort(queue):
    length = len(queue)
    for i in range(0, length):
        min = i
        for j in range(i + 1, length):
            if queue[j] < queue[min]:
                min = j
        queue[min], queue[i] = queue[i], queue[min]
    return queue

if __name__ == "__main__":
    print("开源优测-积微速成计划基本功")

    #生成随机无需数据
    queue = generator()

    #打印无序数列
    print(queue)

    #插入排序
    length = len(queue)
    sorted_data = select_sort(queue)

    #打印排序结果
    print(sorted_data)