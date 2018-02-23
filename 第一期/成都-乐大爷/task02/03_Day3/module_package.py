# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
内建模块：sys、os
包和模块导入的路径问题，包名或模块名重复的问题
sys.builtin_module_names:查看内置模块的名称

"""

def _isGM_():
    print('尊敬的GM大人，欢迎您进入游戏！已为您打开所有GM权限')
    levels = ['权限1','权限2','权限3',...]

def _isUser_():
    print('亲爱的玩家，欢迎您进入游戏！')
    levels = '普通权限'

def check():
    if __name__ == '__main__':
        _isGM_()
    else:
        _isUser_()

check()