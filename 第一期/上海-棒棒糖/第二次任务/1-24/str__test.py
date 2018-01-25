class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
   # __repr__ = __str__


#
s=Student('Michael')
print(s)


