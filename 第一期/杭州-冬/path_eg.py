#--coding:utf-8--:
import os
if __name__=="__main__":
    #返回当前位于哪个路径
    print("当前目录 %s" % os.getcwd())

    #改变当前目录：
    #os.chdir("D:/deeptest/第一期/杭州-冬/第一次任务")
    #print("改变后的目录 %s" % os.getcwd())

    #创建一个不存在的目录：
    #os.mkdir("testing")

    #重命名目录-刚新建的文件
    #os.rename("testing","tested")

    #删除目录--目录下一定无子文件 子目录
    #os.removedirs("tested")
    print("下面是path模块-----")

    pathed=__file__ #路径名：当前模块从哪加载的路径
    print("当前模块加载的绝对路径 %s"  % os.path.abspath(pathed))

    #判断是否为目录：true false
    print("是否目录 %s" %os.path.isdir(pathed))

    #判断是否为文件
    print("是否为文件 %s" % os.path.isfile(pathed))

    #判断目录或文件是否 存在
    print("是否存在 %s" % os.path.exists(pathed))

    #返回标准化形式的路径
    print("标准路径 %s" % os.path.normpath("D:/deeptest/第一期/"))

    #返回文件大小 是目录则返回0
    print("返回 文件大小 %s" % os.path.getsize(pathed))

    #分割目录和文件 返回一个元祖
    print(os.path.split("D:/deeptest/第一期/杭州-冬/第一次任务/calc.py"))

    #分割文件名和扩展名 返回元祖
    print(os.path.splitext("calc.py"))
    #print("文件扩展名分离 %s" % os.path.splitext("calc.py")) --元祖等不能用 % 来格式化输出 会报错

    #返货文件所在目录
    print("文件所在目录 %s" % os.path.dirname("D:/deeptest/第一期/杭州-冬/第一次任务/calc.py"))