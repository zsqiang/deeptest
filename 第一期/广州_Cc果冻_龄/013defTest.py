#coding=utf-8


def sum_tuple(seq):
    sum = 0
    for i in tuple_1:
        sum = sum + i
    return sum


def string_1(str1,str2,str3):   
    return str1+str2+str3  

if __name__ == "__main__":
    
    tuple_1 = (1,5,4,8,4)
    print("元组传参，求和实例")
    sum = sum_tuple(tuple_1)
    print("和为：%d"%sum)

    str1="one"
    str2="two"
    str3="three"
    
    print("字符串传参")
    print(string_1(str1,str2,str3))