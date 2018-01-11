__author__='棒棒糖'
if __name__=='__main__':
    list_demo=[1,2,3,4,5,6,9,7,8,9,0]
    print('内置函数处理list示例')
    print(len(list_demo))
    print(max(list_demo))
    print(min(list_demo))
    print(tuple(list_demo))

    #list方法
    print("list方法代码示例： ")
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = [7, 8, 9, 0, 10, 11]
    #最后追加
    list1.append(100)
    print(list1)
    #在下标处增加
    list1.insert(1, 100)
    print(list1)
    #统计某个元素出现的个数
    print(list1.count(1))
    #通过索引查询元素
    print(list2[3])
    #index, 返回第一个2的索引
    print(list1.index(2))
    #两个列表追加
    print(list1.extend(list2))
    print(list2+list1)
    #删除元素
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = ['加勒比海盗','骇客帝国','第一滴血']
    print('删除元素')
    # pop：删除最后一个元素
    list1.pop()
    print(list1)
    # remove：根据元素的值进行删除
    print(list2)
    list2.remove('第一滴血')
    print(list2)
    # del ：根据下标进行删除
    del list1[1]
    print(list1)
    #把列表反向
    list2 = ['加勒比海盗', '骇客帝国', '第一滴血']
    list2.reverse()
    print(list2)
    #排序
    list1 = [5, 8, 7, 2, 2, 3, 3, 3, 4, 5, 6]
    list1.sort()
    print(list1)
    #拷贝
    list3=list1.copy()
    print(list3)
    #清空
    list1.clear()
    print(list1)

'''
总结：
有返回值如list1.count(1)，可以直接print(list1.count(1))
无返回值的如list1.append(100)，需要再次print(list1)
'''
if __name__=='__main__':
    #切片
    print("列表切片操作示例!")
    list2 = ['加勒比海盗', '骇客帝国', '第一滴血','无极','星球大战']
    print(list2[1])
    print(list2[-2])
    print(list2[1:4])

    #修改
    print("修改操作示例!")
    list2 = ['加勒比海盗', '骇客帝国', '第一滴血', '无极', '星球大战']
    list2[0]="棒棒糖碰一个"
    print(list2)