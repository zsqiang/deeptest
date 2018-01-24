# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
目录遍历
os.walk
    walk返回值说明：
    返回值为一个迭代器对象，它的每个部分包含一个元组，
    即（目录X,[目录X下的目录列表],[目录X下的文件列表]）
'''
import os

def walk_dir(Target_dir):
    #root 当前根目录
    #dirs :root下的子目录
    #files :root下的子文件
    walk_result = os.walk(target_dir)
    print(type(walk_result))#<class 'generator'>

    for root,dirs,files in walk_result:
        print(type(root),type(dirs),type(files))
        print("-",root)

        #遍历当前子目录
        for name in dirs:
            print(" --",name)

        #遍历当前目录的子文件
        for filename in files:
            print(" --",filename)

if __name__ == "__main__":
    target_dir = os.curdir
    walk_dir(target_dir)

'''
<class 'str'> <class 'list'> <class 'list'>
- .
 -- breakAndContinue.py
 -- buildInFunctions.py
 -- classFuncdation.py
 -- forControlExample.py
 -- FuncExample.py
 -- ifControlExample.py
 -- iniConfig.ini
 -- iniFileWR.py
 -- moduleExample.py
 -- mult99.py
 -- numberExample.py
 -- numberFuncExample.py
 -- numberTypeExchangeExample.py
 -- osExample.py
 -- osExample2.py
 -- osExample3.py
 -- packageExample.py
 -- stringFindAndReplace.py
 -- stringJoinAndSplit.py
 -- stringJudgeTpye.py
 -- stringStrip.py
 -- whileControlExample.py
 -- __init__.py
'''