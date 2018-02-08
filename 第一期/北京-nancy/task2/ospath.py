# -* coding:utf-8 *-
__author__ = 'nancy'

import os

if __name__ == "__main__":
    # init
    path = __file__   # 显示文件当前位置
    print("current file full path is: %s" % path)

    #return True if dir exit
    print("if_dir_exit: %s" % os.path.isdir(path))

    #return True if file exit
    print("if_file_exit: %s" % os.path.isfile(path))

    #return True if dir/file exit
    print("if dir/file exit: %s" % os.path.exists(path))

    #return file size, if dir ,return 0
    print("get file size: %s" % os.path.getsize(path))

    print("get absolute path: %s" % os.path.abspath(path))
    print("standardization path: %s" % os.path.normpath(path))

    print("splite filename and ext：", end="")
    print(os.path.splitext(path))

    print("get file name: %s" % os.path.basename(path))
    print("get dir of the file: %s" % os.path.dirname(path))
