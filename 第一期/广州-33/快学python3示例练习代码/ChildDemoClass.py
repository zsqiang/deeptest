# coding=utf-8
# 类继承的示例


class DemoClass:
    def __init__(self):
        print("初始化")

    def output(self, text):
        print(text)

    def output_none(self):
        print("我不能传入参数")


class ChildDemoClass(DemoClass):
    def __init__(self):
        print("我是子类")

    def output_none(self):
        print("我是子类不能传参的方法")


if __name__ == "__main__":
    # 创建一个类对象
    demo_obj = DemoClass()

    # 调用output
    demo_obj.output("我是参数")

    # 调用output_none
    demo_obj.output_none()

    print("-----------------------------------")
    # 创建子类的对象
    child_demo_obj = ChildDemoClass()

    # 调用output, 调用的是父类的方法
    child_demo_obj.output("我是参数")

    # 调用output_none, 调用的是自己的方法，即重写后的方法
    child_demo_obj.output_none()