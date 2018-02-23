# -*- coding:utf-8 -*-

__author__ = 'catleer'

"练习类"
"""
1.Python中的类有什么特性？
封装、继承、多态
2.封装是什么？
类名.方法的调用方式，实际上就是一种封装。封装主要是为了保护隐私
3.继承是什么？
子类可以继承父类全部的特性（私有特性除外），可以进行重写。
4.多态是什么？
多态依赖于继承，一个类能抽象成多种子类。
多态性：感觉是实例变量的作用，定义在方法中的变量，只作用于当前实例，使一个方法能展现多种形态。
5.静态语言和动态语言？？
鸭子类型是啥？怎么用？
"""
import module_package
module_package.check()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print("你家小宠物的名字是{}".format(self.name))

class Dog(Animal):
    # def __init__(self, name):
    #     Animal.__init__(self,name)
    pass

class Cat(Animal):
    pass

def run_once(animal):
    animal.run()
    print("wow")

dog = Dog('kk')
run_once(dog)

cat = Cat('kitty')
run_once(cat)