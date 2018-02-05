#第一种方法计算0-100间所有偶数和
if __name__=='__main__':
    sum=0
    print('计算0-100间所有偶数和')
    #方法1，使用for
    for i in range(0,101,2):
        sum+=i
    print(sum)
#第二种方法计算0-100间所有偶数和
    sum=0
    i=0
    while i <=100:
        sum += i
        i+=2
    print(sum)

    # 打印99乘法表
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d*%d=%d\t" % (j, i, i * j), end='')
            j += 1
        print("")
        i += 1
    # while和for
    n = 1
    while n <= 9:
        for m in range(n, 10):
            print('%d*%d=%d' % (n, m, n * m), end=' ')
        print('')
        n += 1

