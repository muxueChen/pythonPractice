# -*- coding: utf-8 -*-
import time
from datetime import date, datetime, timedelta
# 获取当前时间
# localtime = time.localtime(time.time())
# print(">>>>>>>>>{0!s}{1!s}".format(localtime, type(localtime)))
# 三种时间的转化

# 1.时间戳------->时间元组:
# time1 = time.time()
# tuple1 = time.localtime(time1)

# for t in tuple1:
#     print("--------------{0:d}{1!s}".format(t,type(t)))

# 输出结果如下
# --------------2019
# --------------2
# --------------11
# --------------10
# --------------1
# --------------21
# --------------0
# --------------42
# --------------0


# 时间元组 转字符串
# tuples = time.localtime()
# strTime = time.strftime("%Y-%m-%d %H:%M:%S", tuples)
# print(strTime)
# 输出结果
# 2019-02-11 10:15:53
# strtime2  = time.strftime("%Y{y}%m{m}%d{d} %H{h}%M{m1}%S{s}", tuples).format(y="年", m="月", d="日", h="时", m1="分", s="秒")
# print(strtime2)
# 输出结果
# 2019年02月11日 10时22分08秒


# asctime() 方法
# t = time.localtime()
# print(type(t), t)
# print(time.asctime(t))
# 输出结果
# <class 'time.struct_time'> time.struct_time(tm_year=2019, tm_mon=2, tm_mday=
# 11, tm_hour=10, tm_min=12, tm_sec=0, tm_wday=0, tm_yday=42, tm_isdst=0)
# Mon Feb 11 10:12:00 2019

# 时间戳计算时间差
#根据时间戳来计算（注意时间戳时秒还是毫秒）

#1、天数
# time.time()+86400*7 #当前时间的后7天

#2、小时
# time.time()+3600*7 #当前时间的后7小时

#3、分钟
# time.time()+60*7 #当前时间的后7分钟

# 字符串形式计算时间差
start ="2018-06-19 17:37:31"
end = "2018-06-19 17:39:35"
# 返回开始时间元组
start=time.strptime(start, "%Y-%m-%d %H:%M:%S")
# 返回结束时间元组
end=time.strptime(end, "%Y-%m-%d %H:%M:%S")
# 
userStart = datetime(start[0], start[1], start[2])
userEnd = datetime(end[0], end[1], end[2])
# 天数
print('天数>>>>>',(userEnd-userStart).days)
times = time.mktime(end) - time.mktime(start)
m,s = divmod(times, 60)
h, m = divmod(m, 60)
# 精确到秒
print(">>>>",h, m, s)

