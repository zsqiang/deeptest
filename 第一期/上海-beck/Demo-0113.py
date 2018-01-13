# -*- coding:utf-8 -*-

__author__ = 'beck'

if __name__ == '__main__':
    tuple1=(u"test",u"开源优测",'122','784','wyue','Runoob', 1997, 2000)
    tuple2=(1,2,3,4,5,6,7,8,9,0)
    tuple3 = ('Google', 'Runoob', 1997, 2000);

    print(len(tuple1))
    print(min(tuple2))
    print(max(tuple2))
    list1=[u"开源优测","122","784","wyue"]
    print(tuple(list1))

    element = tuple1[2]
    print(element)
    element = tuple1[-2]
    print(element)
    element = tuple1[3:5] #不包括第5个元素
    print(element)
    element = tuple1[4:] #包括第4个元素
    print(element)

    #将2个元组的元素进行拼接
    print(u"元组合并或连接操作示例：")
    tuple4 = tuple1 + tuple2
    print(tuple4)

    #将某个元素加入到元组中
    print(u"将testtuple元素加入到tuple2元组第4个位置中：")
    tuple2 = tuple2[:4] + ('testtuple',) + tuple2[4:]
    print(tuple2)

    #删除元组
    tuple5 =(u"test",u"开源优测","122","784","wyue","Runoob")
    print(tuple5)
    del  tuple5
    #print(tuple5)

    tuple6 = (u"test", u"开源优测", "345", "784", "wyue")
    tuple7 = tuple6 + tuple2 # 从左往右进行合并计算
    print(tuple7)

    tuple8 = tuple6 * 2
    print(tuple8)
    result =  u"test" in tuple8 #判断是否在当前数组里面
    print(result)

    #修改元组中元素  非法操作不允许
   # tuple8[2] = 100
   #   print(tuple8)

    print(u"列表处理内置函数list的示例：")
    list_demo = [100,22,23,8,12,98,28]
    list_demo_one = (18,26,33,45,5,"test","string","list")
    print(len(list_demo))
    print(min(list_demo))
    print(max(list_demo))
    list_demo_two = list(list_demo_one)
    print(list_demo_two)

    print(u"LIST代码示例和相关例子：")
    list_one = [11,2,31,4,5,"test","string","one","s","s"]
    list_two = [62,7,8,91,10,"tet","ing","two"]
    #在list_one后面添加一个元素
    list_one.append("testone")
    print(list_one)
    #统计s出现的次数
    countone = list_one.count("s")
    print(countone)
    #后面添加一个列表
    list_one.extend(list_two)
    print(list_one)
    #查询字符并返回索引
    index_num = list_one.index(5)
    print(index_num)
    #插入某个元素
    list_two.insert(3,"testtow")
    print(list_two)
    #移除列表中最后一个元素
    print(list_two.pop())
    print(list_two)
    #移除第一个匹配到元素
    list_one.remove('s')
    print(list_one)
    #对列表进行排序
    list_three = [12,4,6,23,56,18,28,100,1829,167]
    list_three.sort()#默认为升序排序
    print(list_three)
    list_four = ["test","j","xmi54","ab5c","qwr"]
    list_four.sort() #字母按照abc的顺序排序，升序
    print(list_four)
    #sort的两个参数
    list_three.sort(reverse = True) #实现sort的降序
    print(list_three)
    list_four.sort(key=len,reverse=True) #实现sort的长度并降序排序
    print(list_four)
    #对列表进行反转
    list_two.reverse()
    print(list_two)
    #复制列表
    list_five = list_four.copy()
    print(list_five)
    #清空列表
    list_five.clear()
    print(list_five)

    #对列表进行取值相关操作
    list_six = [1,2,3,4,5,6,"test","string","one","two"]
    print(list_six)
    elementone = list_six[2]
    print(elementone)

    elementone = list_six[-3]
    print(elementone)

    elementone = list_six[1:3]
    print(elementone)

    elementone = list_six[:3]
    print(elementone)

    elementone = list_six[6:]
    print(elementone)

    list_six[5] = "test list for update"
    print(list_six)