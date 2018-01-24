# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
四则运算：计算任意2个数据的加减法
问题：set\get的用法
特殊方法预览：可查看《流畅的Python》1.3章
"""

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


if __name__ == '__main__':
    
    a = int(input("#:"))
    b = int(input("#:"))
    calc = Calc(a, b)
    print(Calc(a, b).add())
    
    calc.set(a, 3)  
    print(calc.add())