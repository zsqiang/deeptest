
#元组使用()，元素不可修改
#列表使用[]，元素可以修改
#字典使用{}

__author__='棒棒糖'
if __name__=='__main__':
    tuple_demo=(1,2,3,4,5,6,7,8,9,0)
    #计算元素个数
    print(len(tuple_demo))
    #返回最大的元素
    print(max(tuple_demo))
    #返回最小的元素
    print(min(tuple_demo))
    #列表转换成元组
    list_demo=[1,2,3,4,5,6]
    tuplel=tuple(list_demo)
    print(tuplel)

    #切片
    data_demo=("DeepTest", "appium", "testingunion.com", "hello","python3")
    e=data_demo[1]
    f=data_demo[-2]#从后往前
    g=data_demo[1:]
    h=data_demo[1:4]#不包括4
    print(e)
    print(f)
    print(g)
    print(h)

    #合并
    print('两个元组用+合并')
    tup1=('DeepTest',"appium")
    tup2=('hello','python','testinguion.com')
    print(tup1)
    print(tup2)
    print(tup1+tup2)

    #运算
    print('元组的计算')
    tup1=('deeptest','开源优测')
    tup2=(0,1,2,3,4)
    print(len(tup1))
    print(tup1+tup2)
    print(tup2*2)
    print(5 in tup2)
    for t in tup2:
        print(t)

    #使用del删除整个元组，里面的元素不可变。
    print('删除')
    tup1 = ('DeepTest', "appium")
    del tup1
    print(tup1)



