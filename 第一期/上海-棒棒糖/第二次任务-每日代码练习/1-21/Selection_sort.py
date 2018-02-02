__author__='棒棒糖'
import random
#随机生成1-1000之间无序的10个整数
def generator():
    random_data=[]
    for i in range(0,10):
        random_data.append(random.randint(1,1000))
    return random_data
#选择排序
def select_sort(data_list):
    length=len(data_list)
    for i in range(0,length):
        min=i
        for j in range(i + 1, length):
            if data_list[j]<data_list[min]:
                min=j
        data_list[min],data_list[i]=data_list[i],data_list[min]
    return data_list

if __name__=='__main__':
    random_data=generator()
    print(random_data)
    length=len(random_data)
    sorted_data=select_sort(random_data)
    print(sorted_data)