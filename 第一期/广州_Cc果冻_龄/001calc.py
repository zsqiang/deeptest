class Calc:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):  
        return self.a + self.b

    def sub(self):
        if(self.a > self.b):
            return self.a - self.b
        elif (self.a < self.b):
            return self.b - self.a

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


if __name__=="__main__":
    C = Calc(2,3)
    
    print "The two number add:",C.add()
    print "The two number sub:",C.sub()
    print "The two number mul:",C.mul()
    print "The two number div:",C.div()





        

