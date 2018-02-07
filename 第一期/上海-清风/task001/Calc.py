#   coding=utf-8

__author__ = "上海-清风"

class Calc:
    # 初始化
    def __init__(self,a, b):
        if type(a) and type(b) == int:
            self.a = a
            self.b = b
        else:
            print "输入参数必须为整数类型！"
    # 加法
    def __add__(self):
        try:
            self.result = self.a + self.b
            print "%s + %s = %s" % (self.a,self.b,self.result)
        except Exception:
            print("请输入正确的参数！")
    # 减法
    def __sub__(self):
        try:
            self.result = self.a - self.b
            print "%s - %s = %s" % (self.a,self.b,self.result)
        except Exception:
            print("请输入正确的参数！")
    # 乘法
    def mul(self):
        try:
            self.result = self.a * self.b
            print "%s * %s = %s" % (self.a,self.b,self.result)
        except Exception:
            print("请输入正确的参数！")
    # 除法
    def div(self):
        try:
            if self.b != 0:
                self.result = self.a / self.b
                print "%s / %s = %s" % (self.a, self.b, round(self.result,2))
            else:
                print("0不能为除数！")
        except Exception:
            print("请输入正确的参数！")
    def mothed(self):
        self.__add__()
        self.__sub__()
        self.mul()
        self.div()


if __name__ == '__main__':
    in1 = raw_input("请输入第一个参数：")
    in2 = raw_input("请输入第二个参数：")

    calc = Calc(in1,in2)
    calc.mothed()
