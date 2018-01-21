# -* coding:utf-8 *-
__author__ = 'nancy'


def sum(a, b):
    c = a + b
    return c

def multi():
    data = []
    for i in range(1, 10):
        line = []
        for j in range(i, 10):
            line.append(u"%d * %d = %2d" % (i, j, i*j))
        data.append(line)
    return data

def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum + s
    return sum

def str_join(str1, str2, str3):
    return str1 + str2 + str3

if __name__ == "__main__":
    c = sum(1, 2)
    print(c)

    data = multi()
    print(data)
    for d in data:
        print(d)

    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    print(tuple1)
    sum = sum_tuple(tuple1)
    print(sum)

    str1 = u"str1"
    str2 = u"str2"
    str3 = u"str3"
    str_j = str_join(str1, str2, str3)
    print(str_j)
