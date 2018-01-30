#示例

class DemoClass1:
    #__init__默认执行
    def __init__(self):
        print('初始化')
    #需要传入参数，且返回值
    def output(self,text):
        print(text)
    def output_none(self):
        print('不传参数')

deo_obj1=DemoClass1()
deo_obj1.output('我是参数')
deo_obj1.output_none()
print('-'*50)

#继承
class DemoClass2:
    def __init__(self):
        print('初始化')
    def output(self,text):
        print(text)
    def output_none(self):
        print('不传参数的方法')

        #继承父类
class ChildDemoClass(DemoClass2):
    def __int__(self):
        print('需要爸爸买橘子')
    #重写父类中的方法
    def output_none(self,a):
        print('我是被重写的方法，可以传参')
        print(a)

demo_obj2 = DemoClass2()
demo_obj2.output('我是参数')
demo_obj2.output_none()

print('-'*50)
child_demo_obj=ChildDemoClass()
child_demo_obj.output('我是儿子传的参')
child_demo_obj.output_none('我是儿子调用重写的方法传的参')
