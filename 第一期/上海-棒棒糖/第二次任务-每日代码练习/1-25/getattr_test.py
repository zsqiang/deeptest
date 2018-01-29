class Student():
    def __init__(self):
        self.name='棒棒糖'
    def __getattr__(self, attr):
        if attr=='score':  #返回属性
            return 85
        if attr=='age':   #返回函数
            return lambda:25
        #raise ArithmeticError('\'Student\'object has no attribute \'%s\'' % attr)

s=Student()
print(s.name)
print(s.score)
print(s.age())
print(s.abc)    #如果没有raise ArithmeticError，任意调用都会返回None

class Clain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, path):
        return Clain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__

a=Clain().status.user.timeline.list
print(a)

