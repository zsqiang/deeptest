#元组、列表、字符串、字典的遍历
str='加勒比海盗'
tuple=('加勒比海盗','骇客帝国','第一滴血')
list = ['指环王','霍比特人','速度与激情']
list_tuple=[('指环王','喜欢看'),('第一滴血','不喜欢看')]
dit={'test': '开源优测', 'book': 'python3'}

print("-"*5+"字符串的遍历"+"-"*5)
for a in str:
    print(a)
print("-"*5+"元组的遍历"+"-"*5)
for b in tuple:
    print(b)
print("-"*5+"列表的遍历"+"-"*5)
for c in list:
    print(c)
print("-" * 5 + "列表中包含元组的遍历" + "-" * 5)
for x,y in list_tuple:
    print(x,y)
    #字典遍历需要将字典变为列表中包含元组，使用.items()方法
print("-"*5+"字典的遍历"+"-"*5)
print("遍历字典方式一： ")
for d,e in dit.items():
    #需要将字典变为列表中包含元组，使用.items()方法
    print(d,e)
    # 先遍历keys，在关联值
print("遍历字典方式二： ")
for f in dit:
    print(f, dit[f])


#range(start, end, step)以指定步长生成一个指定范围的数值序列
