#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


class Student:

    def __init__(self, name, num, score=[]):
        self.name = name
        self.num = num
        self.score = score

    def input_stu(self):
        for i in range(5):
            self.name = input("请输入学生%d的姓名：" % i+1)
            self.num = input("请输入学生%d的学号：" % i+1)
        for i in range(3):
            self.score.append(input("学生的分数为："))
        return self.name, self.num, self.score

    def output_stu(self):
        print(self.name)
        print(self.num)
        print(self.score)


if __name__ == '__main__':

    stu = Student()
    stu.input_stu()
    stu.output_stu()