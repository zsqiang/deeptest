# -*- coding:utf-8 -*-
import random
# 随机生成1-10之间无序序列整数数据
def generator():
    random_list=[]
    for i in range(10):
        random_list.append(random.randint(1,10))
    return random_list
# 选择排序
def select_sort(data):
    length = len(data)

    for i in range(0,length):
        min = i
        #查找最小的元素
        for j in  range(i+1,length):
            if data[j]<data[min]:
                #找到最小的元素
                min = j
        #交换位置
        data[min],data[i]=data[i],data[min]
    return data


if __name__ == "__main__":
    random_list = generator()
    print(random_list)

    new_list = select_sort(random_list)
    print(new_list)