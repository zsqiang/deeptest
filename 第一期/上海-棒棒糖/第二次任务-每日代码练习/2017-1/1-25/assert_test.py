'''
def foo(s):
    n=int(s)
    print('>>>n=%d'%n)  #把可能有问题的变量打印出来看看
    return 10/n
def main():
    foo('0')
main()
'''
'''

def foo(s):
    n=int(s)
    assert  n!=0,'n is zero'# !=是不等于  表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
    return 10/n               #断言失败，assert语句本身就会抛出AssertionError：
def main():
    foo('0')
main()
'''
import logging
logging.basicConfig(level=logging.INFO)
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)
