# -*- coding:utf-8 -*-
__author__ = "Lakisha"

import csv

if __name__ == "__main__":
    print("python csv文件字典写读操作示例")

    #写CSV文件
    print("写入一些简单的数据到CSV_dict_data.csv中")

    with open("csv_dict_data.csv", "w") as fwriter:
        # 写csv头
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(fwriter, fieldnames=fieldnames)
        writer.writeheader()

        #写CSV内容
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely',
                         'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful',
                         'last_name': 'Spam'})

    print("读取csv_dict_data.csv问内容")
    with open("csv_dict_data.csv", "r") as freader:
        reader = csv.DictReader(freader)
        for row in reader:
            # 遍历每行中的数据
            print(row['first_name'], row['last_name'])