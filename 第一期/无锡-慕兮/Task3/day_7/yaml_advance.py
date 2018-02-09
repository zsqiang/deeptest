# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import yaml

class Hero:
    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp
    def __repr__(self):
        return "%s(name=%r, hp=%r, sp=%r)" % (
             self.__class__.__name__, self.name, self.hp, self.sp)
    def __str__(self):
        return "%s:{name=%r, hp=%r, sp=%r}" % (
             self.__class__.__name__, self.name, self.hp, self.sp)

#不懂
print(yaml.load("""
 !!python/object:__main__.Hero
name: Welthyr Syxgon
hp: 1200
sp: 0
"""))

#不懂
print (yaml.dump(range(5), canonical=True))
print (yaml.dump(range(50), width=50, indent=4))
print (yaml.dump(range(50)))


class Monster(yaml.YAMLObject):
    yaml_tag = '!Monster'
    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks
    def __repr__(self):
        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)

data = ("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
""")
py_data = yaml.load(data)
print(py_data)

ya_data = yaml.dump(py_data)
print(ya_data)