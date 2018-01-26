#--coding:utf-8--
import json
if __name__=="__main__":
    #定义一个json串 注意最好定义成str.因为loads的参数必须是str或bytes或bytearray
    json_str='["1","2","3","4"]'
     
    print(type(json_str))   #转化前的类型

    #返回解码json后 即json转化为py对象的类型
    changed1=json.loads(json_str) #转化为py对象
    print(type(changed))
    


    #定义一个dict,用于转化成json
    dict_json={
        "a":1,
        "b":2
    }

    #py对象编码成json
    jsoned=json.dumps(dict_json)
    print(jsoned)
    #查看转化为json后的类型
    print(type(jsoned))

    #转化为json后再次转化回去即py对象
    dict3_json=json.loads(jsoned)
    print(type(dict3_json))
   


   #dumps loads是针对具体数据的转化
   #若文件中有json要转化,或转化后保存为文件存储用dump load

   #已经定义好一个包含json的ss.txt
   #把json读进来转化为py对象
    with  open('ss.txt',encoding='utf-8') as f:
        data=json.load(f)
        print(type(data))   #转化后为dict
        #把转化为的py对象打印出来
        for (k,v) in data.items():
            print(k,":",v)
    

    #定义一个dict,转化为json并保存到文件中
    dict2_jison={
        "a":"aa",
        "b":"bb"
    }
    #定义保存的文件名ss2.txt
    with open('ss2.txt','w') as ff:
        json.dump(dic2t_jison,ff)   #开始转化并保存

    ff.close()  #不要忘记,否则不能在磁盘生成文件