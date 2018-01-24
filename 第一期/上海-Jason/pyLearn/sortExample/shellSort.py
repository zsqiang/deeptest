# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
概述
    希尔排序（shell's Sort）是插入排序的一种，
    又称“缩小增量排序”（Diminishing Increment Sort），是直接插入排序算法的一种更高效的改进版本。
    希尔排序是非稳定排序算法，由D.L.Shell与1959年提出。
    希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
    随着增量的逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分为一组，算法便终止。
基本过程
    希尔排序属于插入类排序，是将整个有序序列分割成若干小的子序列分别进行插入排序。
    排序过程：
    1.先取一个正整数d1<n，把所有序号相隔d1的数组元素放一组，组内进行直接插入排序；
    2.然后取d2<d1，重复上述分组和排序操作；
    3.直至di=i，即所有记录放进一个组中排序为止。
时间成本
    希尔排序是按照不同步长对元素进行插入排序，
    当刚开始元素很无序的时候，步长最大，所以插入排序的元素个数很少，速度很快；
    当元素基本有序了，步长很小，插入排序对于有序的序列效率很高。
    所以，希尔排序的时间复杂度会比O(n^2)好一些。
'''
import random

def generator():
    random_data = []
    for i in range(0,10):
        random_data.append(random.randint(1,1000))
    return random_data

def shell_sort(data_list):
    #序列长度
    lengh = len(data_list)
    #步长
    step = 2
    #分组
    group = int(lengh/step)
    print("group:",group)
    while group > 0:
        #遍历分组，对所有分组进行排序
        for i in range(0,group):
            j = i + group
            #对分组进行排序
            while j < lengh:
                k = j - group
                key = data_list[j]
                while k >= 0:
                    if data_list[k] > key:
                        data_list[k + group] = data_list[k]
                        data_list[k] = key
                    k = k - group
                j = j + group
        group = int(group/step)
    return data_list

if __name__ == "__main__":
    random_data = generator()
    print(random_data)
    sorted_data = shell_sort(random_data)
    print(sorted_data)
