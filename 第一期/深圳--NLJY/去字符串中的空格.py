print("去掉字符串前后的空格")
demo_str1 = '  前后有空  格的字符串  '
test1=demo_str1.lstrip() # 去掉前面的空格
print(test1)
test2 = demo_str1.rstrip() # 去掉后面的空格
print(test2)
test3 = demo_str1.strip() # 去掉两边的空格
print(test3)

demo_str2 ='123456789'
demo_str3 = 'abcdefHJK000'
demo_str4 = '12345abcABDCD'
demo_str5 = 'abcdef'
demo_str6 = 'ABCDEFJ'
demo_str7 = '   '
demo_str8 = '   abcdef'
# isalnum 判断是否为字母或数字
print(demo_str1.isalnum())
# isalpha 判断是否都是字母
print(test1.isalpha())
# isdigit 判断是否都是数字
print(test2.isdigit())
# islower 判断是否都是小写
# isupper  判断是否都是大写的
# issapce  判断是否都是空格
# 在字符串中查找字符 find(' ')
dict ={'deeptest':'开源优测','book':'python快速上手'}
print(len(dict))    # 输出字典的长度
str_d = str(dict)
print(str_d)    # 输出字典，以可打印的字符串输出字典
print(dict)
print(type(dict))
print(type(str_d))
