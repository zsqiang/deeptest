###返回函数

###装饰器（Decorator）
在代码运行期间动态增加功能的方式叫装饰器，其实本质上decorator就是一个返回函数的高阶函数

###偏函数
functools.partial 帮助我们创建一个偏函数
import functools

int2 = functools.partial(int, base=2)
int2 = functools.partial(int, base=10)

print('1000000=', int2('1000000'))
print('1010101=', int2('1010101'))