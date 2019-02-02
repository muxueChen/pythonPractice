from math import exp, log, sqrt
import re

from datetime import date, time, datetime, timedelta

# 打印出今天的日期形式，以及年、月、日
today = date.today()
print("today:{0!s}".format(today))
print("today:{0!s}".format(today.year))
print("today:{0!s}".format(today.month))
print("today:{0!s}".format(today.day))
print("today:{0!s}".format(datetime.today()))

# 使用timedelta计算一个新的日期

one_day = timedelta(days=-1)
yesterday = today + one_day
print("yesterday:{0!s}".format(yesterday))

eight_hours = timedelta(hours=-8)
print("{0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

# 计算两个日期之间的天数
date_diff = today - yesterday
print("{0!s}".format(date_diff))
print("{0!s}".format(str(date_diff).split()[0]))

# 根据一个日期对象创建具有特定格式的字符串
print("{:s}".format(today.strftime('%m/%d/%Y')))
print("{:s}".format(today.strftime('%b %d, %Y')))
print("{:s}".format(today.strftime('%Y-%m-%d')))
print("{:s}".format(today.strftime('%B %d, %Y')))

date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

# 基于4个具有不同日期格式的字符串创建2个datetime对象和2个date对象
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))
# 仅显示日期部分
print("Output #56: {!s}".format(datetime.date(datetime.strptime\
(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime\
(date4, '%B %d, %Y'))))
