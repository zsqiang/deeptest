"""
while循环
break
break语句用于控制跳出for或while循环体
continue
continue语句用于跳出当前循环块中剩余的代码语句，继续下一次循环执行。
"""
if __name__=="__main__":
    print("计算0-100所有的偶数和")
    n=100
    index=0
    sum=0
    while index<=n:
        sum=sum+index
        index=index+2
    print("0-100间偶数和= %d"% sum)