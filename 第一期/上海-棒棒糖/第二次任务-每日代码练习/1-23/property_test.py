class Student(object):
    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise  ValueError('score must between 0 ~ 100!')
        self._score=value

s=Student()
a=int(input('请输入一个成绩:'))
s.set_score(a)
print(s.get_score())

'''把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值
'''

class Student1(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('成绩必须是数字')
        if value<0 or value>100:
            raise ValueError('成绩只能在0-100之间')
        self._score=value

b=Student1()
a=int(input('请输入一个成绩:'))
b.score=a  #实际转化为s.set_score(60)
print(b.score)#实际转化为s.get_score()