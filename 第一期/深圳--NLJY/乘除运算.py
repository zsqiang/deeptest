class Calc:
    def __init__(self , a, b):
        a = int(input("请输入第一个整数："))
        self.F_nub = a
        b= int(input("请输入第二个整数:"))
        if b== 0:
            print("第二个数不可以为0")
            b= int(input("请输入第二个整数："))
        else:
            self.S_nub =b
# 加法
    def add(self):
        add = self.F_nub + self.S_nub
        print("加法结果是%d"%add)
# 减法
    def sub(self):
        if self.F_nub >self.S_nub:
            sub = self.F_nub - self.S_nub
        else:
            sub = self.S_nub - self.F_nub
        print("减法结果是%d"%sub)
# 乘法
    def mul(self):
        mul = self.F_nub * self.S_nub
        print("乘法的结果是%d"% mul)
# 除法
    def div(self):
        div = self.F_nub /self.S_nub
        print("除法的结果是%d"%div)   # 注意 print()的缩进问题
Calc = Calc(30,60)
Calc.add()
Calc.sub()
Calc.mul()
Calc.div()
