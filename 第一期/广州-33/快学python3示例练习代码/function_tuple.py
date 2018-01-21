# coding=utf-8
# 函数参数的传递示例，本示例的函数参数为不可变参数——元组，定义一个为元组求和的函数


def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum + s
    return sum


if __name__ == "__main__":
    tuple_demo = (1, 3, 99, 2, 30, 4)
    print(tuple_demo)

    sum = sum_tuple(tuple_demo)
    print("元组的和为: %d" % sum)