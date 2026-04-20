## datetime module
### 目录
```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```
关注date，datetime，time，timedelta
### datetime
```py
from datetime import datetime
now = datetime.now()#返回now对象
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()#时间戳指的是从1970/1/1开始经过的秒数
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38
```

### strftime
格式化日期  
now = datetime.now()#操作均要对于now对象进行
语法：time_one = now.strftime("关于%m，%d，%Y，%H，%M，%S的表达式")  
除此之外还要%a%A等有不同的description，可以查阅文档
```py
from datetime import datetime
# 当前日期和时间
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S 格式
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S 格式
print("time two:", time_two)
time: 01:05:01
time one: 12/05/2019, 01:05:01
time two: 05/12/2019, 01:05:01
```

### strptime
字符串转化为时间  
```py
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")#使用要满足一致的格式，返回的是now对象
print("date_object =", date_object)
```
### date
date对象的格式为(year,month,day)  
可以手动创建:d = date(2020,1,1)
可以调用函数创建:tody = date.today()或者d.today()
date对象的访问：tody.month,tody.year.tody.day

### time
time对象的格式为(hour=0,minute=0,second=0,microsecond)
```py
from datetime import time
# time(hour = 0, minute = 0, second = 0)默认值
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
```

### timedelta
datetime，date，time对象之间可直接进行加减
```py
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# 距离新年的时间：27天，0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # 距离新年：26天，23:01:00
```