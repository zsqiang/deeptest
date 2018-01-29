"""
列表
List（列表）是Python最常用的数据类型，它使用方括号[]来标识
list1 = [1, 2, 3, u"DeepTest", u"开源优测"]
"""
if __name__=="__main__":
    print("List列表实例")
    list_demo=[1,2,3,4,5,6]
    #python中的内置函数
    print("查看列表中元素的个数：",len(list_demo))
    print("返回列表中的最大元素：",max(list_demo))
    print("返回列表中的最小元素：",min(list_demo))

    #将list列表转换成元组
    tuple_demo=tuple(list_demo)
    print("将list列表转换成元组：",tuple_demo)
    """
    list的方法
    有大量的方法用于list的处理,下面我们看看示例：
    append(obj)
    在列表末尾添加新的对象
    count(obj)
    统计列表中某个元素出现的次数
    extend(seq)
    在列表末尾追加另外一个序列（即列表扩展）
    index(obj)
    返回列表中第一个匹配到的元素的索引
    insert(index, obj)
    将在列表指定位置插入一个对象
    pop(obj=list[-1])
    移除列表中的一个元素（默认最后一个），并返回该元素
    remove(obj)
    删除列表中第一个匹配到的元素
    reverse()
    将列表中元素反向
    sort([func])
    对列表中元素进行排序
    clear()
    清空列表中元素
    copy()
    复制列表
    """
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = [7, 8, 9, 0, 10, 11]
    #在列表后追加一个对象
    list1.append(100)
    print("在列表后追加一个对象：",list1)
    print("统计元素出现的次数：",list1.count(1))
    #在列表末尾追加另外一个序列
    list1.extend(list2)
    print("在列表后追加另外一个序列：",list1)
    #返回列表中第一个匹配到的元素的索引
    print("返回列表中第一个匹配到的元素的索引:",list1.index(2))
    # insert, 在列表第一个位置插入200
    list1.insert(0, 200)
    print("在列表第一个位置插入200",list1)
    #删除列表的最后一个元素
    list1.pop()
    print("删除列表的最后一个元素：",list1)
    #reverse 反向列表
    list1.reverse()
    print("反向列表：",list1)
    #sort 对列表进行排序
    list1.sort()
    print("对列表进行排序",list1)
    list3=list1.copy()
    print("复制显示列表：",list3)
    #清空列表
    list2.clear()
    print(list2)
    """
    list列表切片
    因为列表也是一个序列，所以我们可以使用Python的切片机制来访问元组中指定位置的元素，也可以截取其中的一段元素
    """
    data_demo = ["DeepTest", "appium", "testingunion.com", "hello", "python3"]
    # 读取第二个元素appium, 注意索引下标从0开始
    e=data_demo[1]
    print(e)
    # 读取倒数第二个hello
    e2=data_demo[-2]
    print(e2)
    # 切片，截取从第2个元素开始后的所有元素
    e3=data_demo[1:]
    print(e3)
    # 切片，截取第2-4个元素
    e4=data_demo[1:4]
    print(e4)
    """
    更新
    列表不同于元组，列表中的元素是可以进行修改或更新的，除了前提到的append、insert方法新增外，我们还可以对列表中原来的数据进行修改
    """
    print(data_demo)
    # 把hello改为hello word
    data_demo[3]="hello word"
    print(data_demo)
