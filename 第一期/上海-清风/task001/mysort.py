#   coding=utf-8

__author__ = "上海-清风"

import random

class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end,count):
        self.start = start
        self.end = end
        self.count = count

    # 实现排序，内部函数
    def __mysort__(self):
        rad = [random.randint(self.start,self.end) for a in range(self.count)]
        for x in range(len(rad)):
            for y in range(x+1,len(rad)):
                if rad[x]>rad[y]:
                    rad[x],rad[y] = rad[y],rad[x]

        print(rad)

# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10, 1000, 100)

    # 打印排序后的结果
    sorted_data.__mysort__()