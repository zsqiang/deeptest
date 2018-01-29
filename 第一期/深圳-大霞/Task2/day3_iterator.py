"""
迭代器
迭代是Python最强大的功能特色，是遍历访问序列元素的一种方式
可以记住当前遍历位置
只能往前遍历，不能后退
从序列的第一个元素开始访问，直至所有元素被访问完
有两个基本方法: iter() 和 next()
字符串、列表或元组对象可以用于创建迭代器
"""
import sys
if __name__=="__main__":
    seq_tuple=(1,2,3,4,5)
    #创建迭代器
    seq_it=iter(seq_tuple)

    print("访问打印第一个元素：%s"% next(seq_it))
    print("访问打印第二个元素：%s" % next(seq_it))
    print("访问打印第三个元素：%s" % next(seq_it))

    #for循环遍历迭代器
    print("for循环遍历迭代器")
    for_it=iter(seq_tuple)
    for i in for_it:
        print(i,end=' ')

    print("\nwhile循环遍历迭代器")
    while_it=iter(seq_tuple)
    while True:
        try:
            print(next(while_it),end=' ')
        except StopAsyncIteration:
            sys.exit()
