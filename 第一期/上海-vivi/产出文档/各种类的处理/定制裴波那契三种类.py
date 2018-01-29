###定制类
#以裴波那契数列为列，写一个Fib类， 然后作用于for循环，用_iter_，该方法返回一个迭代对象:

#实现方法一：
__iter__:

class Fib(object):

    def __init__(self):
        self.a, self.b = 0,     #初始化两个计数器a,b

    def __iter__(self):  # 实例本身就是一个迭代对象，故返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:  # 退出循环的条件
            raise StopIteration()
        return self.a       #返回下一个值


for n in Fib():
    print(n)



#实现方法二：
__getitem__()

class Fib2(object):

	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

f = Fib2()
print(f[0])
print(f[9])



#实现方法三：
__getitem__() + isinstance(n, slice)

class Fib3(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib3()

print(f[1: 5])
print(f[:10])
print(f[:10:2])
#执行结果：
[1, 2, 3, 5]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#结果显示该切片并没有对step 进行处理


总结：这里列举了三种裴波那契数列的写法，第一种只能实现打印结果，第二种只能实现按照下标取出元素，第三种通过判断传入的值是int类型还是slice类型来实现可切片打印数列的效果

