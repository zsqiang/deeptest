#coding=utf-8

class DemoClass:
    def __init__(self):
        print("初始化")

    def output(self,text):
        print("我是父类参数")
    
    def output_none(self):
        print("我不能传入参数")

class ChildDemoClass(DemoClass):
    def __init__(self):
        print("我是子类初始化")
    
    def output(self,text):
        print("我是子类参数")

    def output_none(self):
        print("我是子类不能传参的方法")

if __name__ == "__main__":

    demo_obj = DemoClass()   
    demo_obj.output("我是参数")
    demo_obj.output_none()

    print("---------华丽丽的分割线----------")

    child_demo_obj = ChildDemoClass()
    child_demo_obj.output("我是参数")
    child_demo_obj.output_none()
