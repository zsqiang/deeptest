#--coding:utf-8--
#关于set
##set：其元素无序 不可重复.和dict的key类似.只能是放入不可变对象

if __name__=="__main__":
    set_1=set("deep")
    #无序 不可重复.放入重复的元素会忽略
    print(set_1)

    #常用list创建set
    set_2=set(["aa","aa","b","c"])
    ##  set里面传入的是一个list-可变对象,但真正放到set里面的不是set 而是 "aa" "b"这些字符串
    ##  猜测可能是因为set只接受一个参数,去掉列表括号变为多个参数而出错--可变为用元组括起来成为一个参数
    ## 如放入一个元素：set("aa") 放入多个元素则上面等价于 set(("aa","bb","b","c"))--其实放入到set的还是"aa"这些字符串,不是list或tuple
    print(set_2)

    #函数：len()
    print(len(set_2))

    #方法之增 删
    ##增加一个元素add() 
    set_2.add("d")
    print(set_2)
    ##增加多个元素 以list作为参数
    set_2.update(['d','e'])
    print(set_2)
    ##删除一个元素
    set_2.remove("d")
    print(set_2)

    #set和高中数学集合概念类似.有并集 交集的方法
    print(set_1.union(set_2))
    print(set_1.intersection(set_2))