# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
随机生成100个10至1000之间的数，对生成的100个数进行排序
禁止使用Python自带的排序函数，要自己实现排序函数
参考资料：经典排序算法集锦-http://www.cnblogs.com/kkun/archive/2011/11/23/2260312.html
冒泡排序的时间复杂度和空间复杂度：o(n*n)  o(1):运行过程中，数据的存储空间不会随着算法的不同而改变。
random.uniform(a,b):a<=N<=b的float型数据；
random.randint(a,b):a<=N<=b的int型数据；
random.randrange(a,b,step):(1,100,2)->奇数 (0,100,2)->偶数
"""

import random


class MySort:
    # 初始化
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.random_data = []
        # 生成器or列表推导式

        # self.random_data = [random.uniform(self.start, start.end) for i in range(self.count)]

    # 生成器
    def __generator(self):
        # 生成指定范围指定数量的随机数
        
        for i in range(0, self.count):
            self.random_data.append(random.uniform(self.start, self.end))

    

    def Sort_desc(self):
        """降序排序"""

        self.__generator()
        # 用冒泡排序来实现
        # 计算待排序数据长度
        n = len(self.random_data)

        for i in range(0, n):
            for j in range(1, n-i):
                if self.random_data[j-1] > self.random_data[j]:
                    self.random_data[j-1], self.random_data[j] = self.random_data[j], self.random_data[j-1]

        return self.random_data

# 使用示例
if __name__ == "__main__":
    sort_data = MySort(0, 100, 100)

    # 排序
    data = sort_data.Sort_desc()

    # print(len(data))
    print(data)

        