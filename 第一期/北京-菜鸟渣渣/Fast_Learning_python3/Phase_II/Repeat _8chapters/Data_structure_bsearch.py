'''
概述

二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好。

其缺点是要求待查表为有序表，且插入删除困难。因此，折半查找方法适用于不经常变动而查找频繁的有序列表。

首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；

否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。

重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。


算法复杂度

二分查找的基本思想是将n个元素分成大致相等的两部分，取a[n/2]与x做比较;

如果x=a[n/2],则找到x,算法中止;

如果x<a[n/2],则只要在数组a的左半部分继续搜索x;

如果x>a[n/2],则只要在数组a的右半部搜索x.

时间复杂度无非就是while循环的次数！
'''

# 二分查找算法
# seq   待查序列
# query 要查找的目标
def binary_search(seq, query):
    # start为起始索引
    # end  为结束索引
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2  # // 整除
        val = seq[mid]
        if val == query:
            # 在seq中找到目标query
            # 返回对应的索引值
            return mid
        elif val < query:
            # 目标值大于中间值
            # 说明目标值在mid - end之间
            start = mid + 1
        else:
            # 目标值小于于中间值
            # 说明目标值在start - mid之间
            end = mid - 1

    # 目标值不存在于seq中，返回None
    return None

if __name__ == "__main__":

    print("二分查找示例")

    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    print(seq)
    print("---------二分查找--------")
    print("找到：", 5, " 索引是： ", binary_search(seq, 5))

    print("---------二分查找--------")
    print("找到：", 4, " 索引是： ", binary_search(seq, 4))

    print("---------二分查找--------")
    print("找到：", 13, " 索引是： ", binary_search(seq, 13))

    print("---------二分查找--------")
    print("找到：", 1, " 索引是： ", binary_search(seq, 1))

    print("---------二分查找--------")
    print("找到：", 25, " 索引是： ", binary_search(seq, 25))




