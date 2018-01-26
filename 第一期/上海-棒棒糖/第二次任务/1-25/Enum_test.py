from enum import Enum
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
print(Month.Jan.value)
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

#自定义类
from enum import Enum,unique
@unique #装饰器检查保证没有重复值
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(1))
for name, member in Weekday.__members__.items():
    print(name, '=>', member)