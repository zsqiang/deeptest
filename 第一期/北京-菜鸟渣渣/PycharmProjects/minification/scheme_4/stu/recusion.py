#coding=utf-8
def sum_c(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i


    print  sum
# sum_c(200)
def sum_r(n):

    if  n>0:
        sum =n+sum_r(n-1)
    else:
        sum=0
    return  sum
print sum_r(100)
