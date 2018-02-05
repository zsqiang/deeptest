# coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

'''

什么是csv格式

逗号分隔值（Comma-Separated Values，CSV，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。

CSV文件由任意数目的记录组成，记录间以某种换行符分隔；

每条记录由字段组成，字段间的分隔符是其它字符或字符串，最常见的是逗号或制表符。

所有记录都有完全相同的字段序列，通常都是纯文本文件。

建议用nodepad++、sublime等编辑器进行编辑。

csv格式规则

开头是不留空，以行为单位。
可含或不含列名，含列名则居文件第一行。
一行数据不跨行，无空行。
以半角逗号（即,）作分隔符，列为空也要表达其存在。
列内容如存在半角引号（即"），替换成半角双引号（""）转义，即用半角引号（即""）将该字段值包含起来。
文件读写时引号，逗号操作规则互逆。
内码格式不限，可为 ASCII、Unicode 或者其他。
不支持特殊字符
Python csv模块
`
csv模式是python内置的标准模块，用于读写csv格式的文件。

在csv模块中提供了reader、writer来读写csv格式的文件，

'''
import csv

if __name__ != '__main__':
    logging.info(("python csv read&write file"))
    logging.info(("data -> file"))
    with open('csv_data.csv',"w",newline="") as csvfile:
        spamwriter=csv.writer(csvfile)
        spamwriter.writerow(['csv_demo' ]* 3 + ['DeepTest'])
        spamwriter.writerow(['hello','python3','AutoTest'])
        csvfile.close()

        """
          csv_writer = csv.writer(fileobj [, dialect='excel']
                                      [optional keyword args])
              for row in sequence:
                  csv_writer.writerow(row)

              [or]

              csv_writer = csv.writer(fileobj [, dialect='excel']
                                      [optional keyword args])
              csv_writer.writerows(rows)

          The "fileobj" argument can be any object that supports the file API.
          """
    logging.info(("file -> console"))
    with open('csv_data.csv', "r") as csvfile:
        spamreader=csv.reader(csvfile)

        for row in spamreader:
            logging.info([row," "])
            # csvfile.close()

        csvfile.close()

if __name__ == '__main__':


    '''
    
    在Python csv模块中还提供了另外一种方式来读写csv文件，就是通过字典方式来读写，
    其提供的主要方法为：DictReader、DictWriter，
    
    '''
    # 写csv文件
    logging.info("写入一些简单数据到csv_dict_data.csv文件中")

    with open('csv_dict_data.csv','w') as csvfile:

        write=csv.DictWriter(csvfile,['first_name','last_name'])
        write.writeheader()
        write.writerow({'first_name': 'Baked',
                         'last_name': 'Beans'})
        write.writerow({'first_name': 'Lovely',
                         'last_name': 'Spam'})
        write.writerow({'first_name': 'Wonderful',
                         'last_name': 'Spam'})

    logging.info("读取sv_dict_data.csv的内容")
    with open('csv_dict_data.csv',"r") as csvfile:
        reader=csv.DictReader(csvfile)

        for row in reader:
            print( row['first_name'],row['last_name'])
            print(row['first_name'], row['last_name'])

