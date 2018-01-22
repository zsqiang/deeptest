# -*- coding:utf-8 -*-

__author__ = 'luoquan'

class woshibaba:
    def __init__(self):
        print('我是一个父亲')
    def eye(self,color):
        print('my eyes is',color)
    def hobby(self,sport):
        print('my love is',sport)

class son(woshibaba):  ###我操我括号里面的没写，那还继承个几把
    def __init__(self):
        print('我是一个儿子')
    def blood_type(self):
        print('A')
    #重写hobby
    def hobby(self):
        print('我喜欢打篮球！！')
if __name__ =="__main__":
    daddy = woshibaba()
    daddy.eye('yellow')
    daddy.hobby(__author__)

    son1 = son()
    son1.eye('白的，吓人不')
    son1.hobby()