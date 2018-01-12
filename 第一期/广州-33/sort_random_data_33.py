#coding=utf-8
'''
随机生成100个10至1000之间的数，对生成的100个数进行排序
'''
import random

def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength-1):
            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i] = bubbleList[i] + bubbleList[i+1]
                bubbleList[i+1] = bubbleList[i] - bubbleList[i+1]
                bubbleList[i] = bubbleList[i] - bubbleList[i+1]
        listLength = listLength - 1
    print bubbleList

if __name__ == '__main__':
    bubbleList = []
    bubbleList = random.sample(range(10,1000),100)
    bubble(bubbleList)