# coding = utf-8
# 生成器函数读取10G大文件，每次只读100M，处理完成后再读取下一个100M，如此迭代下去

import sys


def read():
    try:
        f = open('E:/PycharmProjects/test.txt', 'r')
    with open('E:/PycharmProjects/test.txt', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    read()