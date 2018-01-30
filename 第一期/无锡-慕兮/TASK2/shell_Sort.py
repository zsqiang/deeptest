# -*- coding:utf-8 -*-
__author__ = ""

import random
'''
公众号：开源优测
'''

#随机生成1-10之间无序序列整数数据
def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))
    return random_data

#希尔排序
def shell_sort(data_list):
    # 序列长度
    length = len(data_list)
    # 步长，这个数据大家可以修改下，查看排序过程
    step = 2
    # 分组
    group = int(length / step)
    print("group:", group)
    while group > 0:
        #遍历分组，对所有分组进行排序
        for i in range(0, group):
            j = i + group
            #对分组进行排序
            while j < length:
                k = j - group
                key = data_list[j]
                while k >= 0:
                    if data_list[k] >key:
                        data_list[k + group] = data_list[k]
                        data_list[k] = key
                    k = k - group
                j = j + group
        group = int(group / step)
    return data_list

if __name__ == "__main__":
    print("开源优测-积微速成计划基本功")

    #生成随机无序数据
    random_data = generator()

    #打印无序数据
    print(random_data)

    #排序
    length = len(random_data)
    sorted_data = shell_sort(random_data)

    #打印排序结果
    print(sorted_data)