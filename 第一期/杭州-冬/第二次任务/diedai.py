#--coding:utf-8--

#迭代含义：可以通过for in循环来从头至尾循环访问其中元素的形式 就叫迭代。 可用于迭代的对象常叫 可迭代对象。所谓遍历 就是访问其中每个元素
## 用instance()判断目标对象是否为某种类型.这里判断是否为 可迭代对象
from collections import Iterable
from collections import Iterator
list_1=[0,1,2]
print(isinstance(list_1,Iterable))
#判断是否为迭代器
print(isinstance(list_1,Iterator))

#迭代器：一个对象作为参数可以用于next()函数且返回下一个值的对象
#迭代器的两个基本方法 Iter() next() #其实我觉得这里叫函数更恰当
#list、tuple等可用于for循环遍历 为可迭代对象但不是迭代器
##不过我们可以把可迭代对象 改造成迭代器 用iter()
it_list=iter(list_1)
#对改造完成的迭代器 上next()

print("iterator第一个元素 %d" % next(it_list))
print("iterator第二个元素 %d" % next(it_list))
print("iterator第三个元素 %d" % next(it_list))

#对于迭代器 仍然可用for in循环来一次性从头开始访问所有元素.但迭代器元素可能有无穷多个
it_list=iter(list_1)
for i in it_list:
     print(i)

#Iterable不一定是Iterator. Itrrator一定是Iterable