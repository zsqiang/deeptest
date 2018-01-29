"""
set集合是Python的基本数据类型，它有可变集合(set()) 和不可变集合(frozenset)两种
set和dict类似，其主要特性是：
其存储的元素是无序的
其存储的元素是不重复
"""
if __name__=="__main__":
    print("set集合无序、不重复")
    set1=set("DeepTest DeepTest")#创建一个集合
    print(set1)#无序、不重复{'s', 'T', 'p', 'e', 'D', ' ', 't'}
    """
    set集合的方法：
    add新增一个元素到set中，不会添加重复元素
    remove从set中删除指定的元素
    clear清空set集合
    update用于新增多个元素值，参数为list
    issubset 用法 s1.issubset(s2), 判断s1中的每个元素是否都在s2中，即s1<-s2
    issuperset 用法 s1.issuperset(s2), 判断s2中的每个元素是否都在s1中,即s1>=s2
    union并集，返回两个集合的并集
    intersection交集，返回两个集合的交集
    difference 用法 s1.difference(s2)， 返回s1中有s2中没的元素
    """
    set_source=set([1,1,2,3,4,5,6,7])
    set_demo=set([1,1,2,3,4,5,6,7])
    print("原始数据：",end="")
    print(set_demo)
    #add后新增元素
    set_demo.add(9)
    set_demo.add(1)
    print("add后的set数据：",set_demo)
    #remove删除元素
    set_demo.remove(9)
    print("删除后的set数据：",set_demo)
    #update新增多个元素
    list_demo=['a','b','c']
    set_demo.update(list_demo)
    print(set_demo)