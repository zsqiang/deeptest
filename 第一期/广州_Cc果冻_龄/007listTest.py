#coding=utf-8

if __name__ == "__main__":
    
    list1 = [1,4,3,2,6,6]
    list2 = [3,9,7,6,5]

    print("list1列表个数")
    print(len(list1))

    print("list1列表最大值")
    print(max(list1))

    print("list1列表最小值")
    print(min(list1))

    print("list1列表追加一个元素100")
    list1.append(100)
    print(list1)

    print("将list1追加到list2中")
    list1.extend(list2)
    print(list1)

    print("统计6出现的次数")
    print(list1.count(6))

    print("返回第一个6的索引")
    print(list1.index(6))

    print("在第一个位置插入200")
    list1.insert(0,200)
    print(list1)

    print("剔除最后一个元素")
    list1.pop()
    print(list1)

    print("把列表反向一下")
    list1.reverse()
    print(list1)

    print("对列表进行反序")
    list1.sort()
    print(list1)
