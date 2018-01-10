#coding=utf-8
'''
Created on 2018年1月9日
实现一个四则运算的类，要求实现任意两个数的加减乘除运算
@author: 33
'''

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b
    
    def mul(self):
        return self.a*self.b
    
    def div(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
                print("除数不能为0")

def test(calc):
    add = calc.add()
    sub = calc.sub()
    mul = calc.mul()
    div = calc.div()
    print("两数之和为:%d"%add)
    print("两数之差为：%d"%sub)
    print("两数之积为：%d"%mul)
    print("两数之商为：%d"%div)
    
if __name__ == '__main__':
    a=int(raw_input("请输入第一个数字："))
    b=int(raw_input("请输入第二个数字："))
    
    calc = Calc(a,b)
    test(calc)