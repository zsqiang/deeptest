# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
队列：先进先出，在队头进行删除，在队尾进行插入
空队列时不能进行删除操作，且有对应的提示信息
"""

class Queue:

    # 初始化队列长度
    def __init__(self, size=30):
        self.size = size
        self.queue = []
        self.front = 0
        self.rear = -1

    # 判断队列是否为空
    def is_empty(self):
        return self.rear == 0

    # 判断队列是否满了
    def is_full(self):
        res = False
        if (self.rear - self.front + 1) == self.size:
            res = True

        return res  
    
    # 插入
    def add(self, obj):
        if self.is_full():            
            raise Exception("队列已满，无法插入")        
        else:
            self.queue.append(obj)
            self.rear += 1

    # 出队，删除
    def delete(self):
        if self.is_empty():            
            raise Exception("队列是空的，没有数据可出")        
        else:
            self.rear -= 1
            self.queue.pop(0) 

       # 队列头元素
    def first(self):
        if self.is_empty():            
            raise Exception("队列是空的啦……")    
        else:            
            return self.queue[self.front]    
            
    # 队列尾元素
    def last(self):
        if self.is_empty():            
            raise Exception("队列是空的啦……")        
        else:            
            return self.queue[self.rear] 

    # 打印队列
    def show(self):
        print(self.queue)


if __name__ == "__main__":

    queue = Queue(10)

    # 出队
    # queue.delete()

    # 插入队列

    for index in range(10,20):
        queue.add(index)
    queue.show()

    # queue.add(20)

    # 出队
    queue.delete()
    queue.show()
    print(queue.first())
    queue.add(20)
    print(queue.last())

    
