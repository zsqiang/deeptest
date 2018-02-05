'''
import re
test=input('请输入电话号码：')
if re.match(r'^\d{3}\-\d{3,8}$',test):
    print('ok')
else:
    print('failed')
'''
'''
版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
'''
import re
test=input('Email地址：')
if re.match(r'^([0-9a-zA-Z\.\s]+)@(\w+)(\.com|\.org)$',test):
    print('ok')
else:
    print('failed')

'''
版本二可以验证并提取出带名字的Email地址：
<Tom Paris> tom@voyager.org
'''
import re
def fun1(email):
    print(re.match(r'^([0-9a-zA-Z\.\s]+)@(\w+)(\.com|\.org)$',email).groups())
fun1('someone@gmail.com')
fun1('bill.gates@microsoft.com')

def fun2(email):
    m = re.match(r'^<([0-9a-zA-Z\.\s]+)>\s+(.+)$',email)
    if m:
        print(m.group(1),end=' ')
        fun1(m.group(2))
    else:
        fun1(email)
fun2('<Tom Paris> tom@voyager.org')
fun2('someone@gmail.com')
