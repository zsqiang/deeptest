"""
Tuple元组：特点是，元组中的元素不可修改
Python中常用的内置函数有：
len
用于计算元组元素的个数
max
返回元组中元素最大值
min
返回元组中元素最小值
tuple
将列表转换成元组
"""
if __name__=="__main__":
    tuple_demo=(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    #计算tuple_demo中元素个数
    print(len(tuple_demo))
    #返回元组中的最大元素
    print("元组中的最大元素：",max(tuple_demo))
    #返回元组中的最小元素
    print("返回元素中的最小元素：",min(tuple_demo))
    #将list转换成元组
    list_demo=[1,2,3,4,5]
    tuple1=tuple(list_demo)
    print("将数组转换为元组显示",tuple1)
    """
    切片
    因为元组也是一个序列，所以我们可以使用Python的切片机制来访问元组中指定位置的元素，也可以截取其中的一段元素
    """
    print("元组的切片实例")
    data_demo = (u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3")
    #读取倒数第二个hello
    e=data_demo[-2]
    print("读取倒数第二个元素：",e)
    e1=data_demo[0]
    print("读取元组第一个元素：",e1)
    # 切片，截取第2-4个元素
    e2=data_demo[2:4]
    print("截取元组第二到第四个元素：",e2)

    # 合并:元组的元素的特性：不可修改。但我们可以对元组进行合并或是连接生成新的元组
    tup1 = (u"DeepTest", u"appium")
    tup2 = (u"testingunion.com", u"hello", u"python3")
    tup3=tup1+tup2
    print("合并组成新的元组tup3：",tup3)
    #元组的元素的特性：不可修改。意味着我们不可以删除单个元素，但可以把元组给删除，示例如下：
    tup1 = (u"DeepTest", u"appium")
    print("tup1:",tup1)
    # del tup1
    # print("tup1:", tup1)
    """
    元组运算：
    元组和字符串一样可以使用+或*进行运算，经过运算后可以生成一个新的元组
    """
    tup1 = ("DeepTest", "开源优测")
    tup2 = (1, 2, 3, 4)
    print("计算元组的长度：",len(tup1))
    tup3=tup1 + tup2
    print("两个元组的和：",tup3)
    tup4=tup1 * 2
    print("元组复制：",tup4)
    #判断元素是否在元组中，是则返回True，否则返回false
    isTrue=5 in tup2
    print("元素5是否包含在元组中：",isTrue)
    #遍历元组元素
    for i in tup2:
        print(i,end=" ")
    #将列表转换成元组
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple1 = tuple(list_demo)
    print(tuple1)
    #将元组转换成列表
    str=list(tup1)
    print(str)