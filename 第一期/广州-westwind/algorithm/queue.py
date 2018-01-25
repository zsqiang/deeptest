#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 23:57
# @Author  : caijiangchun
# @Site    : 
# @File    : queue.py
# @Software: PyCharm


class Queue():
    """
    队列，先进先出，注意溢出处理
    """

    def __init__(self, size = 30):

        #初始化队列的长度
        self.size = size

        #初始化队列列表
        self.queue = []

        #初始化队列的前端，后端位置
        self.front = 0
        self.rear = -1

    #判断队列是否为空
    def is_empty(self):
        return self.rear ==0

    #判断队列是否满了
    def is_full(self):
        res = False
        if (self.rear - self.front + 1) == self.size:
            res = True

        return res

    #入队
    def add(self, obj):

        if self.is_full():
            raise Exception("queue is empty")
        else:
            self.queue.append(obj)
            self.rear += 1

    #出队
    def delete(self):

        if self.is_empty():
            raise Exception('queue is full')
        else:
            self.rear -= 1
            self.queue.pop()

    #队列头元素
    def first(self):
        if self.is_empty():
            raise Exception('queue is full')
        else:
            return self.queue[self.front]

    #队列尾元素
    def last(self):
        if self.is_empty():
            raise Exception('queue is full')
        else:
            return self.queue[self.rear]

    def show(self):

        print(self.queue)

class QueueFirst:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == "__main__":

    print("队列的实现：")

    #初始化长度为5队列
    queue_one = Queue(5)

    #先把1-5的数入队
    for index in range(1, 6):
        queue_one.add(index)

    #打印队列的数据
    queue_one.show()



    #打印下队列头
    print(queue_one.first())

    #打印下队列尾
    print(queue_one.last())

    #出个队试试
    queue_one.delete()
    #看出队是否成功
    queue_one.show()

    #再出队试试
    queue_one.delete()
    queue_one.show()

    #入队
    queue_one.add(8)
    queue_one.show()

    queue_two = QueueFirst()
    print(queue_two.size())
