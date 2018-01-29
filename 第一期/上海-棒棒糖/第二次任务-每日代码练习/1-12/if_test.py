__author__='棒棒糖'
if __name__=="__main__":
    var1=int(input('请输入一个整数：'))
    if var1>0 and var1<10:
        print('你输入的是一个大于0，小于10的数')
    elif var1>=10:
        print('你输入的是一个大于等于10的数')
    else:
        print("你输入一个负数")


