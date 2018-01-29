#--coding:utf-8--
#head_fist的练习,该折主要：怎么用list处理数据

#创建一个电影列表，包含电影名字
movies=["西游记","东游记","你的名字"]
#在每个电影名后面加一个数字,表示该电影何时发行
movies.insert(1,1996)
movies.insert(3,1997)
movies.insert(5,2016)
#处理每个列表项目 如打印
print(movies[4])
#若有100个元素 不必写100行print处理每个元素 可用迭代实现
for m in movies:    #for循环把可迭代对象里面的每一个元素赋值给-循环变量m.再执行缩进语句
    print(m)        #或者用while循环
#把主角作为一个列表存到一个电影列表,配角作为一个列表嵌套到主角列表
movies_xiyouji=["西游记",1996,"去西天取经降妖除魔",["六小龄童","牛魔王",["农夫","渔夫"]]]
print(movies_xiyouji[3][2][0]) #访问嵌套列表里的元元素
print("for处理嵌套列表----")
#再用for处理每个列表项--打印
for i in movies_xiyouji:
    if isinstance(i,list): #isinstance() 判断目标是否为指定类型对象. 
        for j in i:         #进入第二层list
            if isinstance(j,list):
                for k in j:     #进入第三层list 
                    print(k)
            else:
                print(j)
    else:
        print(i)

#上面两个for if是逻辑一样的重复,定义一个函数 使其反复调用,减少代码量
print("定义函数 递归反复调用-----")
def movies_print(a_list):
    for a_item in a_list:
        if isinstance(a_item,list):
            movies_print(a_item)
        else:
            print(a_item)

movies_print(movies_xiyouji)

#现在还要求每发现一个嵌套列表就缩进一个

##增加一个参数in_table,控制是否缩进及缩进多少
def movies_printin(a_list,in_table=0):
    for a_item in a_list:
        if isinstance(a_item,list):
            movies_printin(a_item,in_table+1)
        else:
            for i in range(in_table):
                print("\t",end='')
            print(a_item)

movies_printin(movies_xiyouji)
