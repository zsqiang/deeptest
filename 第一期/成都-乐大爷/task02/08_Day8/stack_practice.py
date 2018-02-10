# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
堆栈：先进后出
堆栈的操作：入栈和出栈，在栈顶（TOP）对数据进行插入和删除
入栈规则（PUSH）：
1.当栈顶TOP>=n时，再进行入栈操作时，会给出向上溢出信息（入栈前会先检查栈是否已满）
2.栈顶向上移一位:TOP = TOP + 1
3.S(TOP) = X,结束（X为新进栈元素）

出栈规则（POP）：
1.当栈为空，即TOP<=0,则给出向下溢出信息（出栈前会先检查栈是否为空）
2.X = S(TOP),(出栈后的元素赋值给X)
3.TOP=TOP-1， 结束（栈指针减1，指向栈顶）

"""

class Stack:
    def __init__(self, size=30):
        self.size = size
        self.stack = []
        self.top = -1

    # 设置堆栈大小
    def set_size(self, size):
        self.size = size

    # 判断堆栈是否为空
    def is_empty(self):
        res = False
        if self.top == -1:
            res = True

        return res

    # 判断堆栈是否满了
    def is_full(self):
        res = False
        if self.top + 1 == self.size:
            res = True

        return res

    # 打印堆栈里的所以内容
    def show(self):
        print(self.stack)

    def push(self, obj):
        if self.is_full():
            raise Exception("堆栈满啦。。。")
        else:
            self.stack.append(obj)
            self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("堆栈是空的。。。")
        else:
            self.top -= 1
            return self.stack.pop()

if __name__ == "__main__":
    print("堆栈实现示例")

    stack = Stack(5)

    for index in range(1,6):
        stack.push(index)

    stack.show()

    data = stack.pop()
    print(data)
    stack.show()

    for input in range(1,6):
        data = stack.pop()
        print(data)