# -* coding:utf-8 *-
__author__ = 'nancy'

import os

# walk返回值说明： 返回值为一个迭代器对象，它的每个部分包含一个元组，
# 即(目录X, [目录X下的目录列表], [目录X下的文件列表])

def walk_dir(target_dir):
    # root: current dir
    # dirs: subdir
    # files: subfile
    walk_result = os.walk(target_dir)

    for root, dirs, files in walk_result:
        print("-", root)

        for dirname in dirs:
            print("--", dirname)

        for filename in  files:
            print("---", filename)


if __name__ == "__main__":
    target_dir = os.curdir
    walk_dir(target_dir)
