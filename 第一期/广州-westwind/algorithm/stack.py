#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 22:31
# @Author  : caijiangchun
# @Site    : 
# @File    : stack.py
# @Software: PyCharm


class Stack():
    #堆栈的示例

    def __init__(self, size = 30):

        # 初始化堆栈大小
        self.size = size
        # 初始化堆栈列表
        self.stack = []
        # 初始化堆栈默认top值
        self.top = -1

    #设置堆栈大小
    def set_size(self, size):

        self.size = size

    #判断堆栈是否满了
    def is_full(self):

        res = False
        if self.top + 1 == self.size:
            res = True

        return res

    #判断堆栈是否为空
    def is_empty(self):

        res = False
        if self.top == -1:
            res = True

        return res

    #打印堆栈里的所有内容
    def show(self):
        print(self.stack)

    #入栈
    def push(self, cls):
        if self.is_full():
            raise Exception("Stack is full")
        else:
            self.stack.append(cls)
            self.top += 1

    #出栈
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        else:
            self.top = self.top - 1
            return self.stack.pop()


if __name__ == "__main__":

    print("堆栈实现示例")
    # 初始一个长度为5的堆栈实例
    stack = Stack(5)

    # 入栈 整数1-5
    for index in range(1, 6):
        stack.push(index)

    # 打印下堆栈的内容
    stack.show()

    # 出栈
    count = 0
    while count < 5:
        data = stack.pop()
        count += 1
        print(data)

    # 打印下堆栈的内容，此时应该是[]
    stack.show()

