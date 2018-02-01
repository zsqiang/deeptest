#-*- coding:utf-8 -*-

__author__ = 'VV'

import json

if __name__ == '__main__':
    print("python json standard lib demo")

    # python obj turn to json obj
    data = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

    json_data = json.dumps(data)

    # print to show
    print("Before trans")
    print(type(data))
    print(data)
    print("*" * 40)
    print("After trans")
    print(type(json_data))
    print(json_data)

    # json obj turn to python obj
    print()
    print("Trans json obj to python obj")
    python_data = json.loads(json_data)
    print(type(python_data))
    print(python_data)

    print("-" * 40)

    # list
    list_data = [2, 3, 4, 5, 6, 7, 10]

    json_list_data = json.dumps(list_data)

    print("Before trans")
    print(type(list_data))
    print(list_data)
    print("*" * 40)
    print("After trans")
    print(type(json_list_data))
    print(json_list_data)

    print("-" * 40)

    # int
    int_data = 33333333333

    json_int_data = json.dumps(int_data)

    print("Before trans")
    print(type(int_data))
    print(int_data)
    print("*" * 40)
    print("After trans")
    print(type(json_int_data))
    print(json_int_data)

    print("-" * 40)

    print("Format demo: ")
    json_data2 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))

    print(type(json_data2))
    print(json_data2)

    print("-" * 40)

    print("Read json file demo: ")

    fp = open('json_data.json', 'r')

    json_data3 = json.load(fp)
    print(type(json_data3))
    print(json_data3)

    fp.close()

    print("-" * 40)

    print("Write json file demo: ")

    fp2 = open('json_write.json', 'w')

    # write to the file
    json.dump(data, fp2, sort_keys=True, indent=4, separators=(',', ":"))

    fp2.close()


    # NOTE: json.loads/json.dumps use to function; json.load/json.dump use to file.
