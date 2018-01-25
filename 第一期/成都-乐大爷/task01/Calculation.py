# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
四则运算：计算任意2个数据的加减法
特殊方法预览：可查看《流畅的Python》1.3章
"""

class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set(self, a, b):
        """重设参数值"""
        self.a = a
        self.b = b

    def add(self):
        """加法"""
        return self.a + self.b

    def sub(self):
        """减法"""
        return self.a - self.b

    def mul(self):
        """乘法"""
        return self.a * self.b

    def div(self):
        """除法"""
        if self.b != 0:
            # 保留到小数点后2位
            return round(self.a / self.b, 2)
        raise "除数为0，为非法数值，请更正！"



if __name__ == '__main__':
    
    a = int(input("#:"))
    b = int(input("#:"))
    calc = Calc(a, b)
    print(Calc(a, b).add())
    
    calc.set(a, 3)  
    print(calc.add())