import csv
print('写读csv文件')
with open('csv_data.csv','w',newline='')as csvfile:
    spamwriter=csv.writer(csvfile,delimiter=',') #delimiter分隔符
    spamwriter.writerow(['csv_demo']*5+['DeepTest'])
    spamwriter.writerow(['hello','Study Python3', 'Auto Testing'])
    csvfile.close()

print('读取csv文件内容')
with open('csv_data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print("row的类型： ", type(row))
        print(row)
        # 遍历每行中每个数据项
        for data in row:
            print(data, "  ")
    f.close()
