# -*- coding:utf-8 -*-
__author__ = "Lakisha"

def avg(data):
    return sum(data)/len(data)

def drop_first_last(grades):
    first, *middle, last = grades
    print (middle)
    return avg(middle)

def do_foo(x, y):
    print("foo", x, y)

def do_bar(s):
    print("bar", s)

def record(records):
    for tag, *args in records:
        if tag == "foo":
            do_foo(*args)
            # print(*args)
            # print(args) #args返回的是列表[]，*args返回参数
        elif tag == "bar":
            do_bar(*args)


def sum_items(items):
    head, *tail = items
    return head + sum(tail) if tail else head

if __name__ == "__main__":
    grades = (100, 98, 73, 54, 68, 1000)
    print(drop_first_last(grades))

    records = [("foo", 1, 2), ("bar", "hello"), ("foo", 3, 4)]

    record(records)

    line = 'nobody:*:-2:-2:Unprivileged User:/Var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(":")
    print(uname, homedir, sh)

    data = sum_items(items=[1, 10, 16, 88, 3])
    print(data)
