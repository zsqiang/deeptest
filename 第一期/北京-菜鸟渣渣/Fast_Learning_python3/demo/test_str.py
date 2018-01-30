class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print('Student object (name: %s) '% self.name)

    __repr__ = __str__


print(Student('VV'))