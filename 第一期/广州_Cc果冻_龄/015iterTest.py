#coding=utf-8
from __future__ import print_function
import sys

if __name__ == "__main__":
    seq_tuple = (1,2,3,4,5)
    seq_it = iter(seq_tuple)

    print("第一个元素：%s"%next(seq_it))
    print("第二个元素：%s"%next(seq_it))
    print("第三个元素：%s"%next(seq_it))

    for_it = iter(seq_tuple)
    print("\nfor循环遍历迭代器对象：")
    for x in for_it:
        print(x,end = ' ')
    
    while_it = iter(seq_tuple)
    print("\n\nwhile遍历迭代器对象")
    while True:
        try:
            print(next(while_it),end = ' ')
        except StopIteration:
            sys.exit()