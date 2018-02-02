# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
猜字谜游戏：
1.输入一串字符；
2.如果输入的字符中包含某个特定意义的字符，则输出一串祝福语；
3.若输入的字符中，包含梅字，则输出一句与梅花相关的诗；同理：兰、竹、松。
4.如果同时包含梅兰竹松，则按排在最前面的那个字为准；
5.如果不包含，则输出特定语句中的一个。
"""

import random

plum = [1,"看取晚来风势，故应难看梅花","青梅花如豆柳如眉，日长蝴蝶飞","游伎皆秾李，行歌尽落梅花","素面翻嫌粉涴，洗妆不褪唇红"]
orchid = [1,"许多含蓄意，不肯露春情。待过清明后，精华入夏清。","多画春风不值钱，一枝青玉半枝妍。"]
bamboo = [1,"蜀魂飞绕百鸟臣，夜半一声山竹裂","斑竹枝，斑竹枝，泪痕点点寄相思。","疏篱护竹，莫碍观梅。"]
pine = [1,"白金换得青松树，君既先栽我不栽。幸有西风易凭仗，夜深偷送好声来。","南轩有孤松，柯叶自绵幂。清风无闲时，潇洒终日夕。"]
other = ["喔，你没有输中任何关键字"]

while(1):
    print("请输入一句你想说的话(如果不想输入任何话，请输入结束退出）：")
    what_you_say = input()
    if "梅" in what_you_say and plum[0]:
        try:
            what_you_get = plum.pop(random.randrange(1,len(plum)))
            print(what_you_get)
        except:
            plum[0] = 0
            print("今天的祝福送完了，请明天再来！输入结束，结束本次输入！")
    elif "兰" in  what_you_say and orchid[0]:
        try:
            what_you_get = orchid.pop(random.randrange(1,len(orchid)))
            print(what_you_get)
        except:
            orchid[0] = 0
            print("今天的祝福送完了，请明天再来！输入结束，结束本次输入！")
    elif "竹" in  what_you_say:
        try:
            what_you_get = bamboo.pop(random.randrange(1,len(bamboo)))
            print(what_you_get)
        except:
            print("今天的祝福送完了，请明天再来！输入结束，结束本次输入！")
    elif "松" in  what_you_say:
        try:
            what_you_get = pine.pop(random.randrange(1,len(pine)))
            print(what_you_get)
        except:
            print("今天的祝福送完了，请明天再来！输入结束，结束本次输入！")
    elif "结束" in what_you_say:
        print("成功结束本次输入！")
        break
    else:
        print(other[0])


# import requests
# html = requests.get("http://www.ruiwen.com/wenxue/shiju/403348.html")
# print(html.content)
