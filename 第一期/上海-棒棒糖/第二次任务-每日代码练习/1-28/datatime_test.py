'''
from datetime import datetime
now=datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20)
print(dt)

from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt.timestamp())# 把timestamp转换为datetime

from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

from datetime import datetime
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

'''

from datetime import datetime, timedelta
now = datetime.now()
print(now)
a=now + timedelta(hours=10)
print(a)
b=now - timedelta(days=1)
print(b)
c=now + timedelta(days=2, hours=12)
print(c)


