class Student (object):
    __slots__ = ('name','age')
'''    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
'''

s=Student()
s.name='棒棒糖'
print(s.name)
s.age=20
print(s.age)

s.score=19
print(s.score)