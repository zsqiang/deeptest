# _*_ coding : utf-8 _*_
__author__ = "Jason"

import os

if __name__ == "__main__":
    # 初始化当前文件全路径变量
    myPath = __file__
    print("当前文件全路径为：%s" % myPath)
    #当前文件全路径为：D:/code/hlbtest/deeptest/第一期/上海-Jason/pyLearn/task02/osExample2.py

    # 判断是否为目录，是目录返回True，否则返回False
    print("目录判断：%s" % os.path.isdir(myPath))
    #目录判断：False

    # 判断是否为文件，是文件返回True，否则返回False
    print("文件判断：%s" % os.path.isfile(myPath))
    #文件判断：True

    # 判断目录或文件是否存在
    print("判断目录/文件是否存在：%s" % os.path.exists(myPath))
    #判断目录 / 文件是否存在：True

    # 获取文件大小，若目标为目录则返回0
    print("获取文件大小：%s" % os.path.getsize(myPath))
    #获取文件大小：1532

    # 获取文件的绝对路径
    print("获取文件的绝对路径：%s" % os.path.abspath(myPath))
    #获取文件的绝对路径：D:\code\hlbtest\deeptest\第一期\上海-Jason\pyLearn\task02\osExample2.py

    # 将目标路径规范化，即更规范的路径表达式
    print("规范化路径：%s" % os.path.normpath(myPath))
    #规范化路径：D:\code\hlbtest\deeptest\第一期\上海-Jason\pyLearn\task02\osExample2.py

    # 将文件名和目录分割
    # 若传入的是目录，则将最后的目录名作为文件名分割
    print("目录和文件名分割：", end="")
    print(os.path.split(myPath))
    #目录和文件名分割：('D:/code/hlbtest/deeptest/第一期/上海-Jason/pyLearn/task02', 'osExample2.py')

    # 分离文件名和扩展名
    print("文件名和扩展名分离：", end="")
    print(os.path.splitext(myPath))
    #文件名和扩展名分离：('D:/code/hlbtest/deeptest/第一期/上海-Jason/pyLearn/task02/osExample2', '.py')

    # 获取文件名
    print("文件名为：%s" % os.path.basename(myPath))
    #文件名为：osExample2.py

    # 获取文件所在目录
    print("文件目录为：%s" % os.path.dirname(myPath))
    #文件目录为：D:/code/hlbtest/deeptest/第一期/上海-Jason/pyLearn/task02