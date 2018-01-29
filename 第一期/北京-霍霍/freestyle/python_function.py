# -*- coding:utf-8 -*-
__author__ = "huohuo"

"""
1、abs() 绝对值或复数的模
2、all() 接受一个迭代器，如果所有元素都为真，则True，否则False
3、any() 接受一个迭代器，如果有一个元素为真，则True,否则False
4、ascii() 调用对象的__repr__()方法，获得该方法的返回值
5、bin() 将十进制转换为二进制


1 .abs()	               2 .dict()	                3.help()	                   4 .min()	             5 .setattr()
6 .all()	               7 .dir()	                    8.hex()	                       9 .next()	         10.slice()
11.any()	               12.divmod()	               13.id()	                       14.object()	         15.sorted()
16.ascii()	               17.enumerate()	           18.input()	                   19.oct()	             20.staticmethod()
21.bin()	               22.eval()	               23.int()	                       24.open()	         25.str()
26.bool()	               27.exec()	               28.isinstance()	               29.ord()	             30.sum()
31.bytearray()	           32.filter()	               33.issubclass()	               34.pow()	             35.super()
36.bytes()	               37.float()	               38.iter()	                   39.print()	         40.tuple()
41.callable()	           42.format()	               43.len()	                       44.property()	     45.type()
46.chr()	               47.frozenset()	           48.list()	                   49.range()	         50.vars()
51.classmethod()           52.getattr()	               53.locals()	                   54.repr()	         55.zip()
56.compile()	           57.globals()                58.map()	                       59.reversed()	      60. __import__()
61.complex()	           62.hasattr()                63.max()	                       64.round()	 
66.delattr()	           67.hash()	               68.memoryview()	               69.set()

"""

if __name__ == "__main__":
    # 绝对值或复数的模
    print(abs(-6))
    # 接受一个迭代器，所有元素为真，返回True
    print(all([1, 0, 3,6]))
    # 接受一个迭代器，有一个元素为真，返回True
    print(any([0, 0, 0, []]))
    # 调用对象的__repr__()方法，获得返回值
    print(ascii([1, 2, 3, 1, 22, 123]))
    # 将十进制转换成二进制
    print(bin(10))
    # 将十进制转换为八进制
    print(oct(7))
    # 将十进制转换为十六进制
    print(hex(15))
    # 测试一个对象是True还是False
    print(bool([]))
    # 将一个字符串转换成字节类型
    s = "apple"
    v = bytes(s, encoding = "utf-8")
    print(v)
    # 将字符类型/数值类型转换为字符串类型
    s = 100
    print(type(s))
    s = str(s)
    print(type(s))
    # 判断对象是否可以被调用，能被调用的就是一个callables对象，比如函数
    print(callable(str))
    # 查看十进制对应的ASCII字符
    print(chr(29))
    # 查看某个ascii对应的十进制数
    print(ord('a'))

    # classmethod（）用来指定一个方法为类的方法，由类直接调用执行，只有一个cls参数，执行类的方法时，
    # 自动调用该方法的类赋值给cls.没有此参数指定的类的方法为实例方法

    # complie() 将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译
    # compile(source, filename, mode, flags = 0, dont_inherit = False, optimize = -1)
    # 将source编译为代码或AST（abstract syntax trees）对象。代码对象能通过exec语句来执行或者eval()进行求值
    # filename-代码文件名，如果不是从文件读取就传递一些可辨认的值。model-指定编译代码的种类，如：exec,eval,single
    # flag、dont_inherit-可选参数
    s = "print('helloworld')"
    r = compile(s, "<string>", "exec")
    print(r)

    # 创建一个值为real + imag * j 的复数或者转化一个字符串或数为复数，如果第一个参数是字符串，则不需要指定第二个参数
    print(complex("123"))

    # delattr() 删除对象的属性
    # dict()创建数据字典
    print(dict())

    # dir()不带参数时返回当前范围内的变量，方法和定义的类型列表，带参数时返回参数的属性，方法列表
    print(dir())

     # divmod()分别取商和余数
    print(divmod(10, 3))

     # enumerate()返回一个可以枚举的对象，该对象的next()方法将返回一个元组
    s = ["a", "b", "c"]
    for i, v in enumerate(s, 1):
        print(i, v)

    # eval() 1、将字符串str当成有效的表达式来求值并返回计算结果2、取出字符串中的内容
    s = "1 + 3 + 5"
    print(eval(s))

    # exec() 执行字符串或complie方法编译过的字符串，没有返回值

    # filter() 过滤器，构造一个序列，等价于[item for item in iterables if function(item)],在函数中设定过滤条件
    # 逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据。
    def uno(x):
        return x > 10
        v = filter(uno, [1, 11, 2, 45, 7, 6, 13])
    print(v)

    # float()将一个字符串或整数转换成浮点数
    print(float(11))

    # format() 格式化输出字符串，format(value,format_spec)实质上是调用了value的__format__(format_spec)方法
    print("i am {0}, age{1}".format("tom", 18))

    # forzenset()创建一个不可修改的集合
    # frozenset([iterable])  set 和 frozenset最本质的区别是前者是可变的，后者是不可变的。当集合对象会被改变时（如删除、添加）
    # 只能用set，一般来说使用frozenset的地方都可以使用set.参数iterable:可迭代对象。

    # getattr()获取对象的属性
    # getattr(object, name[, defalut])
    # 获取对象object名为name的特性，如果object不包含名为name的特性，将会抛出AttributeError异常；如果不包含名为name的特性，
    # 且提供default参数，将返回default。参数object:对象，参数name:对象的特性名，参数default:缺省返回值

    # globals()返回一个描述当前全局变量的字典
    a = "apple"
    print(globals())

    # hasattr(),hasattr(object,name)判断对象object是否包含名为name的特
    # 性(hasattr是通过调用getattr(object, name))是否抛出异常来实现的
    print(hasattr(dict, "get"))

    # hash() 哈希值注意：可哈希的即不可变数据类型，不可哈希即可变数据类型
    # 如果对象object为哈希表类型，返回对象object的哈希值。哈希值为整数，在字典查找中，哈希值用于快递比价字典的
    # 键，两个数值如果相等则哈希值也相等

    # help()调用内建的帮助系统，如果不包含参数，交互式帮助系统将在控制台启动。如果参数为字串，则可以是模块、类、方法等名称
    # 并且帮助页面将会在控制台打印。参数也可以为任意对象。

    # id() 返回对象的内存地址
    a = 1
    print(id(a))

    # input()获取用户输入内容
    print(input("aaa"))

    # int() 将一个字符串或数值转换为一个普通整数int([x[,radix]])
    # 如果参数是字符串，那么它可能包含符号和小数点。参数radix表示转换的基数（默认是10进制)。它可以是
    # [2, 36]范围内的值，或者0。如果是0，系统将根据字符串内容来解析。
    # 如果提供了参数radix,但参数x并不是一个字符串，将抛出TypeError异常
    # 否则，参数x必须是数值(普通整数，长整数，浮点数)。通过舍去小数点来转换浮点数。如果超出了普通整数的表示范围，
    # 一个长整数被返回。如果没有提供参数，函数返回0

    l = "123"
    print(type(l))
    m = int(s)
    print(type(m))

    # isinstance（） 检查对象是否是类的对象，返回True或False,isinstance(obj,cls)
    # 检查obj是否是类cls的对象，返回True或者False
    #class Foo(object):
    #    pass
    #obj = Foo()
    #print(isinstance(obj, Foo))

    # issubclass() 检查一个类是否是另一个类的子类，返回True或者False,,issubclass(sub,super)
    # 检查sub类是否是super类的派生类（子类），返回True或False

    class Foo(object):
        pass
    class Bar(Foo):
        pass
    print(issubclass(Bar, Foo))

    # iter(),iter(o[, sentinel])
    #返回一个iterator对象，该函数对于第一个参数的解析依赖于第二个参数。如果没有提供第二个参数，参数o必须是一个集合对象，
    #支持遍历功能（__iter__()方法）或支持序列功能（__getitem__()方法）
    #参数为整数，从零开始，如果不支持这两种功能，将触发TypeError异常。如果提供了第二个参数，参数o必须是一个可调用对象，在这种
    #情况下创建一个iterator对象，每次调用iterator的next（）方法

    # len() 返回对象长度，参数可以是序列类型（字符串，元组或列表）或映射类型（字典）
    n = "ajljflsjsjd"
    print(len(n))

    # list()列表构造函数
    # locals( ) 打印当前可用的局部变量的字典

    # map(),map(function, iterable,...)对于参数iterable中的每个元素都应用function函数，并将结果作为列表返回。
    # 如果有多个iterable参数，那么fuction函数必须接收多个参数，这些iterable中相同索引处的元素将并行的作为function
    # 函数的参数。如果一个iterable中元素的个数比其他少，那么将用None来扩展改iterable使元素个数一致。如果有多个iterable
    # 且function为None,map()将返回由元组组成的列表，每个元组包含所有iterable中对应索引处值。

    li1 = [1, 2, 3]
    data1 = map([lambda x :x*100, li1])
    print(type(data1))
    data2 = list(data1)
    print(data2)

    # max() 返回给定元素里的最大值

    # meoryview()
    # min() 返回给定元素里的最小值
    # next()返回一个可迭代数据结构中的下一项
    # object(),获取一个新的，无特性对象。Object是所有类的基类，他提供的方法将在所有的类型实例中共享
    # open()打开文件 open(filename[, mode[,bufsize]] )filename表示文件的路径，mode表示打开的模式，
    # bufsize表示文件缓冲区的大小。0表示不缓冲；1表示行缓冲

    # pow(x,y,z) 幂函数，表示取x的y次幂，z表示对第三个参数取余
    s3 = pow(2, 8,)
    print(s3)
    s4 = pow(2, 8, 5)
    print(s4)

    # print()输出函数
    # property()
    # range() 根据需要生成一个指定范围的数字，可以提供你需要的控制来迭代指定的次数
    # repr() 将任意值转换为字符串
    # reversed() 反转，逆序对象
    # round(x [, n])对参数x的第n+1位小数进行四舍五入
    # set()将对象转换为集合
    # setattr() 与getattr()相对应

    # slice() 切片 
    s5 = ["a", "b""c", "d"]
    print(slice(1, 3, s5))
   
    # sorted() 排序
    # sum() 求和
    # tuple() 元组构造函数
    # type() 显示对象所属的类型
    # zip() 将对象逐一配对






    
