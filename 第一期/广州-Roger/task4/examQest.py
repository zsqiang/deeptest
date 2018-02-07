#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 19:33:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re,pyperclip,random
import isNum

class examQ():
    def __init__(self,dict):
        self.dict = dict

    def answer(self):
        question = list(self.dict.keys())
        answer = list(self.dict.values())
        questionR = random.choice(question)
        option = []
        option.append(self.dict.get(questionR,None))
        l = len(option)
        while len(option) < 4:
            answerR = random.choice(answer)
            if self.dict.get(questionR,None) == answerR:
                pass
            else:
                option.append(answerR)
        random.shuffle(option)
        answerO = 'ABCD'[option.index(dict.get(questionR,None))]
        option[0] = 'A: ' + option[0]
        option[1] = 'B: ' + option[1]
        option[2] = 'C: ' + option[2]
        option[3] = 'D: ' + option[3]
        questionRT = questionR + '的省会城市是：' + answerO
        option.insert(0,questionRT)
        return option,answerO

    def paper(self):
        paper = ''
        answerS = ''
        for i in range(5):
            f = examQ(dict).answer()
            paper = paper + '\n'.join(f[0]) + '\n' +'\n'
            answerS = answerS + f[1]
        return paper,answerS


if __name__ == '__main__':
    dict = {'广东':'gz','广西':'nl','湖南':'cs','湖北':'wh','江西':'nc','安徽':'hf'}
    f = examQ(dict).paper()
    print(f[0],f[1])