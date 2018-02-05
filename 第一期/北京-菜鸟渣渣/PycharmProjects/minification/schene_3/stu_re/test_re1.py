
import re
'''
str1="abcdef efs"
print re.search(".",str1).groups()
e = "abcdefhello"
print re.search("^abc(.+)hello$",e).groups()
'''



list1=["va1"]
print list1
print " ".join(list1)


'''
e="123po45645600"
print  re.search("123([op]+).",e).groups()

e = "hellojkgood"

e = "hellokgood"
ff = re.search("hello([jk]+)good$", e)
print ff.groups()

print "*" * 60
st = "Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; R8000 Build/JLS36C) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/6.7 (Baidu; P1 4.3)"
'''
st = "Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; R8000 Build/JLS36C) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/6.7 (Baidu; P1 4.3)"

# print re.search("^zh-[cnCN]]",st).groups()
print re.search("zh-[\w]+;\s(.+)\sBuild",st).groups()
# u = re.search("zh-[cnCN]+;\s(.+)\sBuild", st)

#print u.groups()
if __name__ != '__main__':


    e = "abcdefhello"

    ee= re.search("(.+)hello$",e)

    a=ee.groups()
    print  a

    e = "helloabce  edefgood"

    ff=re.search("^hello(.+)good$",e)
    print ff.groups()


    e = "hellojkjkjkjkjkjkjkjkgood"

    e = "hellokgood"
    ff=re.search("^hello([jk]+)good$",e)
    print ff.groups()

    print "*"*60
    st="Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; R8000 Build/JLS36C) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/6.7 (Baidu; P1 4.3)"


    u=re.search("zh-[cnCN]+;\s(.+)\sBuild",st)

    print u.groups()

