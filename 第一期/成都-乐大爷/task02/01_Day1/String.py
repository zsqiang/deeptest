# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
参考资料：http://www.runoob.com/python3/python3-string.html
字符串处理方式：
连接、切割、查找、替换、格式化
字符串相关的内建函数
"""

# 访问字符串中的值
var1 = "Hi,todayis wednesday"
var2 = "python"

print("var1的第一个字符：", var1[0])
print("var1的第3-9个字符：", var1[2:9]) # 左闭右开
print("var1+var2=", var1 + var2)

# 字符串格式化
str_a = 'haha'
str_b = 'hahahaha'
print("%s 2个 %s 4个" % (str_a, str_b))
print("2个：{}，4个：{}".format(str_a, str_b))

# 字符串内建函数
print(str_a.capitalize())       # 将字符串的首字符转换为大写
print(str_a.center(40, '*'))    # 填充字符串，使字符串居中，‘40’为长度，‘*’为要填充的字符
str_c = 'aabdceidkalmcekre;;fdkfririj'
print(str_c.count('a', 0, len(str_c)))         # 统计字符串中某个字符出现的次数

# decode和encode
# decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。该方法返回解码后的字符串。
str_d = "string 字符串学习"
str_utf8 = str_d.encode(encoding='utf_8')
str_gbk = str_d.encode(encoding='gbk')
print("输出str_utf-8编码：", str_utf8)
print("输出str_gbk编码：", str_gbk)

print("utf-8解码：", str_utf8.decode())      # 默认为utf-8
print("gbk解码：", str_gbk.decode('gbk'))

# endswith()和startswith()
# endswith():用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置

# 字符串查找和替换
# find(str, beg=0, end=len(string)):返回范围内第一次查找到字符串的位置，若没有则返回-1
str_e = 'follow the stock market'
print(str_e.find('o',4))

# index(str, beg=0, end=len(string)):跟find()方法一样，只不过如果str不在字符串中会报一个异常
print(str_e.index('ow',3))

# rfind(str, beg=0,end=len(string)):类似于 find()函数，不过是从右边开始查找.	
# rindex(str, beg=0,end=len(string)):类似于 index()函数，不过是从右边开始查找.

# replace(old, new [, max]):将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

print(str_e.replace('stock', 'equiaty'))

# 判断字符串类型
# isalnum()：如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# isalpha()：如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
# isdigit()：如果字符串只包含数字则返回 True 否则返回 False.
# islower()：如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# isnumeric():如果字符串中只包含数字字符，则返回 True，否则返回 False
# isspace()：如果字符串中只包含空白，则返回 True，否则返回 False.
# istitle()：检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
# isupper()：如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# isdecimal()：检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。

# 字符串处理
# join()：str.join(seq)
str1 = '-'
str2 = ''
seq = ('m', 'o', 'd', 'i', 'f', 'y')
print(str1.join(seq))
print(str2.join(seq))

# ljust()\rjust() 左对齐、右对齐
# lstrip()\rstrip()\strip()
# lower()\upper()\swapcase()\title()
# split():通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
str3 = str2.join(seq)
print(str3.split('o'))
