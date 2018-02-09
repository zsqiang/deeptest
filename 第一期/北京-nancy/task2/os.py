# -* coding:utf-8 *-
__author__ = 'nancy'

import os

if __name__ == "__main__":
    # dir operate
    print("current work dir", end=': ')
    print(os.getcwd())

    print("current dir", end=': ')
    print(os.curdir)

    print("make dir(if not exit,throws exception)")
    os.mkdir("test_mkdir")

    print("rename dir")
    os.rename("test_mkdir", "test_newdir")

    print("remove dir(no subdir or subfile,,if not exit,throws exception)")
    os.removedirs("test_newdir")

    print("change work dir", end=": ")
    os.chdir("c:")
    print(os.getcwd())
