"""
在Python中用elif替代了else i
if 条件:
    # 代码块
elif 条件:
    # 代码块
else:
    # 代码块
"""
if __name__=="__main__":
    print("if条件语句练习")
    var1=int(input("请输入一个整数："))
    if var1>0 and var1<10:
        print("你输入了一个大于0小于10的整数")
    elif var1>=10:
        print("你输入一个大于等于10的整数")
    elif var1==0:
        print("你输入了一个0")
    else:
        print("你输入了一个负数")
"""
if 条件:    
    # 代码块
    if 条件:                
        # 代码块  
    elif 条件:              
        # 代码块      
    else:    
        # 代码块
elif 条件:     
    # 代码块
    # 这里也可以嵌套if
else:      
    # 代码块
    # 这里也可以嵌套if
"""
"""
运算符：
<、<=、>、>=、==、!=、in（是否存在）
"""