from datetime import date
from datetime import time
from datetime import datetime
today = date.today()
print('今天是%s'%today)
print('今天是%s %s %s'% (today.day,today.month,today.year))
weekday_num = today.weekday()
print('今天weekday是%s'% weekday_num)
