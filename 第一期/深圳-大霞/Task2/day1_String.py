"""
在python3中，所有的字符串都是Unicode编码。
对于编程而言，大部分时间都是在做字符的处理，例如字符串连接、切割、转换、格式化等等。
字符串连接和切割
join
以指定的字符串将元组、列表中的所有的元素合并为一个新的字符串。
split
以指定的分隔符来截取字符串，返回一个list对象
"""
if __name__=="__main__":
    print("字符串连接和切割实例")
    t=('1','2','3','4','5','6','a','b',"efg")
    #用join将字符串连接成一个新的字符串
    str_demo='_'.join(t)#'_'连接字符
    print(str_demo)
    #将str_demo以_进行分割
    str_set=str_demo.split('_')#分割后生成一个列表
    print(str_set)
    #将t中元素合并成一个新的字符串
    str_demo_new=''.join(t)
    print(str_demo_new)
    """
    字符串查找和替换
    find
    find(str, beg=0, end=len(string)),查找str是否包含在字符串中，若指定了beg和end，则在beg和end范围中查找，若找到则返回开始的索引值，否则返回-1
    
    index
    同find方法，不同的是，index若未查找到，抛出一个异常信息，而不是返回-1
    
    rfind
    同find方法，不过rfind是从右边往左边查找。
    
    rindex
    同index方法，不过rindex是从右边往左边查找。
    
    repalce
    将字符串中指定的子串替换成目标字符串，如果指定了替换次数，则替换不超过指定的次数
    """
    source_str = "it's my book, please show it, wa ka ka, yo yo yo!"
    #从左往右查找
    print("从左往右查找yo：",source_str.find('yo'))
    print("从左往右查找yo：",source_str.index('yo'))
    #从右往左查找
    print("从右往左查找yo：",source_str.rfind('yo'))
    print("从右往左查找yo：",source_str.rindex('yo'))
    #替换所有的yo
    des_str=source_str.replace('yo','ha')
    print("替换所有的yo：",des_str)
    #替换两次yo
    des_str=source_str.replace('yo','ha',2)
    print(des_str)
    """
    去字符串前后空格
    lstrip
    去除字符串左边的空格
    
    rstrip
    去除字符串右边的空格
    
    strip
    去除字符串左右两边的空格，即把lstrip和rstrip都执行一遍
    """
    print("去除空格实例：")
    demo_str = "  我的前  后 和 中 间  都有空格  "
    # 去除左边空格
    lstr=demo_str.lstrip()
    print(lstr)
    #去除右边空格
    rstr=demo_str.rstrip()
    print(rstr)
    #去除左右两边的空格
    str=demo_str.strip()
    print(str)
    """
    判断字符串类型
    isalnum
    判断字符串是否由字母或数字组成，是则返回true,否则为false
    
    isalpha
    判断字符串是否都是字母，是则返回true,否则为false
    
    isdigit 判断字符串是否都是数字，是则返回true,否则为false
    
    islower 判断字符串是否都是小写，是则返回true,否则为false
    
    isnumeric 判断字符串是否都是数字，是则返回true,否则为false
    
    isspace 判断字符串是否都是空格，是则返回true,否则为false
    
    isupper 判断字符串是否都是大写，是则返回true,否则为false
    """
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "
    print("判断字符串是否都是有数字组成：",str_1.isdigit())
    print("判断字符串是否都是字母或者数字组成：",str_3.isalnum())
    print("判断字符串是否都是字母组成：",str_2.isalpha())
    print("判断字符串是否都是小写组成：",str_4.islower())
    str11='1234'
    str22='5678'
    str12=str11+str22+str_2
    print(str12)