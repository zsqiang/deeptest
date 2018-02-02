#coding=utf-8

if __name__ == "__main__":

    tuple1 = (1,2,3,4,5,6)
    tuple2 = ('a','b','c','d')
    list1 = [1,2,3,4,5,6,7]

    print("tuple1元组个数：")
    print(len(tuple1))

    print("tuple1元组最大值：")
    print(max(tuple1))

    print("tuple1元组最小值：")
    print(min(tuple1))

    print("tuple1和tuple2合并：")
    print(tuple1+tuple2)

    print("将列表转换成元组")
    print(tuple(list1))

    print("读取第二个元素")
    print(tuple1[1])

    print("读取倒数第二个元素")
    print(tuple1[-2])

    print("截取第二个元素开始的所有元素")
    print(tuple1[1:])

    print("截取第二到第四个元素")
    print(tuple1[1:4])


        