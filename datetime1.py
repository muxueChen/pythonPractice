import datetime
import time
# datetime.date      # 表示日期的类。常用的属性有year, month, day；
# datetime.time      # 表示时间的类。常用的属性有hour, minute, second, microsecond；
# datetime.datetime  # 表示日期时间。 
# datetime.timedelta # 表示时间间隔，即两个时间点之间的长度。
# datetime.tzinfo    # 与时区有关的相关信息

# 字符串与datetime对象之间的转换
datetime1 = datetime.datetime.strptime('7时10分52秒', '%H时%M分%S秒')

def cal_difftime(starTime, endTime):
    starTimeTuple = time.strptime(starTime, '%H时%M分%S秒')
    endTimeTuple = time.strptime(endTime, '%H时%M分%S秒')
    # 因为默认年份为1900年，转换时间戳是会出现报错
    # overflowerror：mktime argument out of range
    # timearray 属于元组，不能修改其值
    # 所以我对其年份进行修改
    endTimeTuple = (2019, 2, 11, endTimeTuple[3], endTimeTuple[4], endTimeTuple[5])
    starTimeTuple = (2019, 2, 11, starTimeTuple[3], starTimeTuple[4], starTimeTuple[5])

    # 日期格式数组转换成时间戳
    endtimeStamp = int(time.mktime(endTimeTuple))
    startimestamp = int(time.mktime(starTimeTuple))

    # 计算时间戳差值
    timestamp = endtimeStamp - startimestamp
    m, s = divmod(timestamp, 60)
    h, m = divmod(m, 60)
    return "%02d时%02d分%02d"%(h, m, s)