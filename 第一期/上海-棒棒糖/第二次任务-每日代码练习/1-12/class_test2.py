
class A:
    def __init__(self):
        print('aaa')
        #self.name = "aaa"

    def __funca(self,a):
        print("function a : %s" %a)



class B(A):
    #def __init__(self):
       # print('bbb')
        #self.name = "bbb"

    def funcb(self,b):
        print("function b : %s" %b)



b = B()
#print(b.name)
b.funcb(798)
#b.funca(698)