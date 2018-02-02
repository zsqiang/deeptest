#coding=utf-8
import random

#随机生成100个10到1000的整数
def data():
     random_data = []
     for i in range(0,100):
         random_data.append(random.randint(10,1000))
     return random_data

#冒泡排序
def mysort(data_list):
    for i in range(0,len(data_list)):
        for j in range(i + 1,len(data_list)):
            if data_list[i] > data_list[j]:
                data_list[i],data_list[j] = data_list[j],data_list[i]
    return data_list    

if __name__ == "__main__":
    
    random_data = data()

    print("打印100个10到1000之间的整数：")
    print(random_data) 

    data_sort = mysort(random_data)
    print("升序打印:")
    print(data_sort)