# -* coding:utf-8 *-
__author__ = 'nancy'

import sys

# 斐波那契数列
# 当前项为前面两项之和
def fibonacci(n):
    a, b, count = 0, 1, 0

    while True:
        if count > n:
            return
        yield a
        a, b = b, a+b
        count = count + 1

if __name__ == "__main__":
    seq_tuple = (1, 2, 3, 4, 5)
    seq_it = iter(seq_tuple)
    seq_it2 = iter(seq_tuple)

    print("1: %s" % next(seq_it))
    print("2: %s" % next(seq_it))
    print("3: %s" % next(seq_it))

    for i in seq_it:
        print(i, end=',')
    print('\n')

    f = fibonacci(10)
    while True:
        try:
            print(next(f), end=' ')
        except StopAsyncIteration: # 要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代
            sys.exit(0)

