#!/usr/bin/env python
#__author__ = '北京-Windy'
class Arithmetic:
    #初始化
    def __init__(self,a,b):
        self.a=a
        self.b=b

    #加法
    def __add__(self):
        #print(type(self.a))
        if type(self.a)  in (float,int) or type(self.b)  in (float,int) :
            return self.a + self.b
        else :
            print('请输入正确的数字！')

    #减法
    def __sub__(self):
        if type(self.a)  in (float,int) or type(self.b)  in (float,int) :
            return self.a - self.b

        else:
            print('请输入正确的数字！')

    #乘法
    def __mul__(self):
        if type(self.a)  in (float,int) or type(self.b)  in (float,int):
            return self.a * self.b
        else:
            print('请输入正确的数字！')

    #除法
    def __div__(self):
        if type(self.a)  in (float,int) or type(self.b) in (float,int) :
            return self.a / self.b
        if self.b==0:
            print("除数不能为0！")
        else:
            print('请输入正确的数字！')



if __name__=='__main__':

    print("请输入两个数字：")
    a,b=map(int,input().strip().split(' '))
    print(a,b)
    art = Arithmetic(a,b)
    print("请输入您要执行的运算法则：+、-、*、/")
    choice=input()
    if choice=='+':
        print(a,'+',b,'=',art.__add__())
    elif choice=='-':
        print(a,'-',b,'=',art.__sub__())
    elif choice=='*':
        print(a,'*',b,'=',art.__mul__())
    elif choice=='/':
        print(a, '/', b, '=', art.__div__())
    else:
        print("请输入正确的运算符")
