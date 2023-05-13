"""datetime库的使用
"""
from datetime import datetime

dt = datetime(2023, 5, 13, 13, 30)  # 用指定日期时间创建datetime
print(dt)
# 结果: 2023-05-13 13:30:00

now = datetime.now()  # 获取当前datetime
print(now)
# 结果: 2023-05-13 13:39:04.400620

"""时间戳"""
print("-" * 15, "timestamp", "-" * 15)
dt = datetime(2023, 5, 13, 13, 30)  # 用指定日期时间创建datetime

# 把datetime转换为timestamp
ts = dt.timestamp()
print(ts)  # 结果:1683955800.0
# 注意Python的timestamp是一个浮点数，整数位表示秒。

# timestamp转换为datetime
t = 1683955800.0
print(datetime.fromtimestamp(t))  # 本地时间 2023-05-13 13:30:00
print(datetime.utcfromtimestamp(t))  # UTC时间 2023-05-13 05:30:00

"""time与str的转换"""
print("-" * 15, "time-str", "-" * 15)
cday = datetime.strptime('2023-5-13 13:30:00', '%Y-%m-%d %H:%M:%S')
print(cday)  # 结果: 2023-05-13 13:30:00

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))  # 结果: Sat, May 13 13:43

"""datetime的加减"""
print("-" * 15, "timedate-op", "-" * 15)
from datetime import timedelta

now = datetime.now()
print(now)  # 2023-05-13 13:47:36.114240
now += timedelta(hours=10)
print(now)  # 2023-05-13 23:47:36.114240
now -= timedelta(days=2, hours=12)
print(now)  # 2023-05-11 11:48:43.946695

"""时区转换"""
from datetime import timezone

print("-" * 15, "timezone", "-" * 15)
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
"""
一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
如果系统时区恰好是UTC+6:00，那么上述代码就是正确的，否则，不能强制设置为UTC+6:00时区。
实际上我们处于+8时区, 但是强行设置+6时区, 结果仍然显示的是+8时区
"""
tz_utc_6 = timezone(timedelta(hours=6))  # 创建时区UTC+6:00
now = datetime.now()
print("utc_timezone: ", utc_dt)  # utc_timezone:  2023-05-13 05:54:32.071999+00:00
dt = now.replace(tzinfo=tz_utc_6)  # 强制设置为UTC+6:00
print("utc_6_timezone: ", dt)  # utc_8_timezone:  2023-05-13 13:54:32.071999+06:00

# 使用astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# 使用astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# 将北京时间转换为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(bj_dt)  # 2023-05-13 14:04:50.697779+08:00
print(tokyo_dt)  # 2023-05-13 15:04:50.697779+09:00
print(tokyo_dt2)  # 2023-05-13 15:04:50.697779+09:00
