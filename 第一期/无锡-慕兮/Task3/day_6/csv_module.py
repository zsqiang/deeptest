# -*-coding:utf-8 -*-
__author__ = "Lakisha"

import csv

if __name__ == "__main__":
    print("python csv文件读写操作示例")

    #写入一些简单的数据到csv_data.csv文件中
    with open("csv_data.csv", "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",")
        spamwriter.writerow(["csv_demo"]*5 + ["DeepTest"])
        spamwriter.writerow(["hello", "study python3", "Auto Testing"])
        csvfile.close()

    print("读取csv_data.csv问内容")
    with open("csv_data.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            print("row的类型：", type(row))
            print(row)

            # 遍历每行中每个数据项
            for data in row:
                print(data, end=" ")

    f.close()
    f.close()


