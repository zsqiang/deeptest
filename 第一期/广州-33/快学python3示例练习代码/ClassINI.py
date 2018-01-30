# coding = utf-8
# 用类封装一个通用的ini文件操作类

# 导入模块
import configparser

class ClassINI:
    def __init__(self):
        print("初始化")

    def write(self,fileName):
        with open('fileName', 'r') as fileName:
            fileName.write(fileName)


if __name__ == "__main__":