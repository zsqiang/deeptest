# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
概述
    冒泡排序（Bubble Sort）是一个计算机科学领域的较简单的排序算法。
    它依次比较相邻的两个元素，如果他们的顺序错误就把他们交换过来。
算法原理
    1.比较相邻的元素。如果第一个比第二个大，就互换位置。
    2.对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。最后的元素就是最大的数。
    3.针对所有元素重复以上的步骤，除了最后一个。
    4.持续每次对越来越少的元素重复上面的步骤，知道没有任何一对数字需要比较。
'''
import random

#随机生成10个1-1000之间无序序列整数数据
def generator():
    random_data = []
    for i in range(0,10):
        random_data.append(random.randint(1,1000))
    return random_data

#冒泡排序
def bubble_sort(data_list):
    lenght = len(data_list)

    for i in range(0,lenght):
        for j in range(i+1,lenght):
            if data_list[i] > data_list[j]:
                data_list[i],data_list[j] = data_list[j],data_list[i]
    return data_list

if __name__ == "__main__":
    #生成随机数
    random_data = generator()
    print(random_data)

    #排序并打印结果
    sorted_data = bubble_sort(random_data)
    print(sorted_data)