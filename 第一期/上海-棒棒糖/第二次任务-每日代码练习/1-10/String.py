__author__=u'棒棒糖'
if __name__=="__main__":
    t=('1','2','3','4','5','a','b','ef')
    f='rgtr*retr*retg*ret/fdg'
    #join以指定的字符串将元组、列表中的所有的元素合并为一个新的字符串。
    #用-将t中元素合并成一个新的字符串
    str_demo='-'.join(t)
    print(str_demo)
    #将f用*进行切割
    str_set=f.split('*')
    print(str_set)
    #查看t
    print(t)
    # 将f中元素合并成一个新的字符串
    print(''.join(t))

'''
find(str, beg=0, end=len(string)), 查找str是否包含在字符串中，若指定了beg和end，则在beg和end范围中查找，
        若找到则返回开始的索引值，否则返回 - 1
index   同find方法，不同的是，index若未查找到，抛出一个异常信息，而不是返回 - 1
rfind   同find方法，不过rfind是从右边往左边查找
rindex  同index方法，不过rindex是从右边往左边查找
repalce 将字符串中指定的子串替换成目标字符串，如果指定了替换次数，则替换不超过指定的次数
'''

__author__=u'棒棒糖'
if __name__=='__main__':
    source_str=u"it' my book,please show it ,wa ka ka ka yo yo yo !"
    #c从左往右查找yo
    print(u'从左往右查找 yo')
    print(source_str.find('yo'))
    print(source_str.index('yo'))
    #替换所有的 yo为ha
    des_str=source_str.replace('yo','ha')
    print(des_str)
    #替换两次yo
    des_str=source_str.replace('yo','ha',2)
    print(des_str)

'''
去字符串前后空格
lstrip 去除字符串左边的空格

rstrip 去除字符串右边的空格

strip  去除字符串左右两边的空格
'''
if __name__=='__main__':
    demo_str='   我的前  后  和中间  都有空格 '
    print(demo_str)
    #去除前面的空格
    lstr=demo_str.lstrip()
    print(lstr)
    #去除后面的空格
    rstr=demo_str.rstrip()
    print(rstr)
    #去除所有空格
    str=demo_str.strip()
    print(str)
'''
    isalnum 判断字符串是否由字母或数字组成，是则返回true, 否则为false

    isalpha 判断字符串是否都是字母，是则返回true, 否则为false

    isdigit 判断字符串是否都是数字，是则返回true, 否则为false

    islower 判断字符串是否都是小写，是则返回true, 否则为false

    isnumeric 判断字符串是否都是数字，是则返回true, 否则为false

    isspace 判断字符串是否都是空格，是则返回true, 否则为false

    isupper 判断字符串是否都是大写，是则返回true, 否则为false
'''
if __name__=='__main__':
    str_1='14897445614'
    str_2='sdfdsfvDSGFD'
    str_3='12346dsfgdsSDGF'
    str_4='fsfd'
    str_5='ASDSAD'
    str_6='    '
    str_7='sd  f  '
    # isalnum 判断字符串是否由字母或数字组成，是则返回true, 否则为false
    print('判断字符串是否由字母或数字组成')
    print(str_3.isalnum())
    print(str_1.isalnum())

    #isalpha  判断字符串是否都是字母，是则返回true, 否则为false
    print('判断字符串是否都是字母')
    print(str_2.isalpha())
    print(str_3.isalpha())

    #isdigit 判断字符串是否都是数字，是则返回true, 否则为false
    print('判断字符串是否都是数字')
    print(str_1.isdigit())
    print(str_3.isdigit())

    #islower 判断字符串是否都是小写，是则返回true, 否则为false
    print('判断字符串是否都是小写')
    print(str_2.islower())
    print(str_4.islower())

    #isnumeric 判断字符串是否都是数字，是则返回true, 否则为false
    print('判断字符串是否都是数字')
    print(str_1.isnumeric())
    print(str_3.isnumeric())
    #isspace 判断字符串是否都是空格，是则返回true, 否则为false
    print('判断字符串是否都是空格')
    print(str_1.isspace())
    print(str_6.isspace())

    #isupper 判断字符串是否都是大写，是则返回true, 否则为false
    print('判断字符串是否都是大写')
    print(str_5.isupper())
    print(str_2.isupper())