l = [x * x for x in range(10)] # 这是一个列表
g = (x * x for x in range(10))  # 这是一个生成器
# g.next() 通过g.next() 来调用生成器
for n in g:
    print(n)

def fib(max):
    n = 0
    a = 0
    b = 1
    while n<max:
        print(b)
        a,b = b,a+b
        n= n+1
print(fib(6))
