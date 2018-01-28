# -*- coding:utf-8 -*-
__author__ = "Lakisha"

from collections import deque

import heapq

def search(lines, pattern, history=5):
    '''
    对一系列的文本行做简单的文本匹配操作，当发现有匹配时
    就输出当前的匹配行，以及最后检查过的N行文本
    :param lines: 文本行
    :param pattern: 文本匹配
    :param history: 保存行数
    :return: 
    '''
    previous_lines = deque(maxlen=history)
    #deque(maxlen=N)创建了一个固定长度的队列。当有新纪录加入而队列已满时，
    # 会自动移除最老的那条记录
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == "__main__":
    with open("test.xml") as f:
        for line, previous_lines in search(f, "year", 5):
            for pline in previous_lines:
                print(pline, end="--")
            print(line, end=" ")
            print("-"*20)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 23]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    portfolio = [
        {"name": "IBM", "shares": 100, "price": 91.1},
        {"name": "AAPL", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 200, "price": 21.09},
        {"name": "HPQ", "shares": 35, "price": 31.75},
        {"name": "YHOO", "shares": 45, "price": 16.35}
    ]
    cheap = heapq.nsmallest(1, portfolio, key=lambda s: s["price"])
    print(cheap)
    expensive = heapq.nlargest(1, portfolio, key=lambda price:price["price"])
    print(expensive)