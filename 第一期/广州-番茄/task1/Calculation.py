#coding=utf-8

class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a=int(input("请输入一个整数："))
        self.b=int(input("请输入一个整数："))
        if self.b==0:
            print("不能为0")
            self.b=input("请输入一个整数：")
        else:
            self.b=b

    # 加法
    def __add__(self):
        add=self.a+self.b
        print(add)
    
    # 减法
    def __sub__(self):
        pass
    
    # 乘法
    def mul(self):
        pass

    # 除法
    def div(self):
        pass
Calc_obj=Calc(3,4)
Calc_obj.__add__()
