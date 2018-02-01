# -*- coding：utf-8 -*-
__author__ = "Lakisha"

import json
import os
# import re

class json_parse():

    def json2py(self, data):
        if '.' in data:
            with open(data, "r") as fp:
                return json.load(fp)
        else:
            return json.loads(data)

    def py2json(self, data, *fp):
        if fp:
            return json.dump(data, *fp, sort_keys=True, indent=4, separators=(',', ':'))
        else:
            return json.dumps(data)

if __name__ == "__main__":
    jdata = json_parse()
    # data = "json_tem.json"
    # print(jdata.json2py(data))
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    fp = open('nia.json', 'w')
    jdata.py2json(data, fp)
    fp.close()
