# -*- coding:utf-8 -*-
import json

import re

__author__ = 'beck'

def processJson(inputJsonFile, outputJsonFile):
    fin = open(inputJsonFile,'r',encoding='utf-8')
    fout = open(outputJsonFile,'w',encoding='utf-8')
    for eachline in fin:
        print(eachline)
        line = eachline.strip().encode('utf-8').decode('utf-8')
        print(line)
        line = line.strip(',')
        print(line)
        js = None
        try:
            #test = re.sub('\'', '\"', line)
            js = json.loads(line)
            print(js + '+++++++++++++++++++++')
        except Exception as e:
            print('bad line')
            continue
        js["Country Name"]= "Arab3 World"
        print(js+'==============')
        outstr = json.dumps(js,ensure_ascii=False)+','
        fout.write(outstr.strip().encode('utf-8')+'\n')
    fin.close()
    fout.close()


if __name__ == '__main__':
    #将json转化为dict形式
    json_str = '{"name":"开源优测","url":"www.testingunion.com","id":"DeepTest"}'
    print(type(json_str))
    dict_str = json.loads(json_str)
    print(type(dict_str))
    for element in  dict_str.items():
        print("各个取值：%s,%s"% (element,dict_str.get(element," ")))
    for(k,v) in dict_str.items():
        print(k,":",v)
    #将dict转化为json的形式
    dict_str_two ={"name":u"开源优测","url":"www.testingunion.com","id":"DeepTest"}
    print(type(dict_str_two))
    #ensure_ascii是为了确保汉字转码的正常，否则会出现乱码
    json_str_two = json.dumps(dict_str_two,ensure_ascii=False)
    print(type(json_str_two))
    print(json_str_two)
    #json的高级转化形式
    print("JSON的高级转化形式：")
    json_demo="""
            {
                "weixin": [
                    {
                        "name": "开源优测",
                        "uid": "DeepTest",
                        "desc": "分享开源测试技术"
                    },
                    {
                        "name": "开源优测_demo",
                        "uid": "DeepTest_demo",
                        "desc": "分享开源测试技术_demo"
                    }
                ],
                "web": [
                    {
                        "url": "www.testingunion.com",
                        "name": "开源优测社区",
                        "desc": "分享各类开源测试技巧"
                    },
                    {
                        "url": "www.testingunion.com_demo",
                        "name": "开源优测社区_demo",
                        "desc": "分享各类开源测试技巧_demo"
                    }
                ]
            }
        """
    dict_demo = json.loads(json_demo)
    for (k,v) in dict_demo.items():
        print(k,":",v)
        for data in v:
            for (data_k,data_v) in data.items():
                print(data_k,":",data_v)

    #对json文件进行操作
    filename = 'list.json'
    with open(filename,"r") as file:
        pop_data = json.load(file)
    for data in pop_data:
        Country_Nama = data['Country Name']
        Value = data['Value']
        print(Country_Nama,Value)

    f = open("read.json",encoding='utf-8')
    setting = json.load(f)
    fontFamily = setting['fontFamily']
    fontSize = setting['fontSize']
    size = setting['BaseSettings']['size']
    print(fontFamily)
    print(fontSize)
    print(size)

    #读取原来的json文件并写入到新的json文件中
    processJson('list.json','myOutput.json')

