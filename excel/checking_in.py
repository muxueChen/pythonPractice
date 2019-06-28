import sys
from datetime import date
import time
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

# 返回当天最早一次打卡，最晚一次打卡的元组， 当周一到周五早上打卡早于九点时，让时间等于九点，下班打卡时间早于下午 7:30不计加班时间
def day_clock_in(clock_info):

    if isinstance(clock_info,dict) == False:
        return None
    # {'name':row_name, 'date':row_date, 'clock_in_time':clock_in_time,'clock_out_time':clock_out_time}
    # data_list = []
    # 上班时间
    if 'clock_in_time' not in clock_info.keys() or len(clock_info['clock_in_time']) == 0:
        return None
    be_on_duty = clock_info['clock_in_time']

    if 'clock_out_time' not in clock_info.keys() or len(clock_info['clock_out_time']) == 0:
        return None
    if 'date' not in clock_info.keys() or len(clock_info['date']) == 0:
        return None
    # 下班打卡存在次日打卡的情况
    off_duty_list = clock_info['clock_out_time'].split(' ')

    today = '20' + clock_info['date'].split(' ')[0]
    # 取出日期
    today = time.strptime(today, '%Y-%m-%d')

    # 转换上班时间
    be_on_duty = time.strptime(be_on_duty, '%H:%M')
    be_on_duty_array = (today[0], today[1], today[2], be_on_duty[3], be_on_duty[4], be_on_duty[5],1,1,0)
    # 上班打卡时间戳
    be_on_dutyStamp = int(time.mktime(be_on_duty_array))
    off_dutyStamp = 0
    # 下班打卡时间戳
    if len(off_duty_list) == 2:
        print(off_duty_list[1])
        off_duty = time.strptime(off_duty_list[1], '%H:%M')
        off_duty_array = (today[0], today[1], today[2] + 1, off_duty[3], off_duty[4], off_duty[5],1,1,0)
        off_dutyStamp = int(time.mktime(off_duty_array))
    else:
        off_duty = time.strptime(off_duty_list[0], '%H:%M')
        off_duty_array = (today[0], today[1], today[2], off_duty[3], off_duty[4], off_duty[5],1,1,0)
        off_dutyStamp = int(time.mktime(off_duty_array))

    # 转换成 小时:分钟 的格式，然后进行比较
    # 当天上班考勤时间
    be_on_duty_checking_in = time.strptime("09:00", "%H:%M")
    be_on_duty_checking_in_array = (today[0], today[1], today[2], be_on_duty_checking_in[3], be_on_duty_checking_in[4], be_on_duty_checking_in[5],1,1,0)
    # 上班考勤时间戳
    be_on_duty_checking_inStamp = int(time.mktime(be_on_duty_checking_in_array))

    # 当天下班考勤时间
    off_duty_checking_in = time.strptime("18:00", "%H:%M")
    off_duty_checking_in_array = (today[0], today[1], today[2], off_duty_checking_in[3], off_duty_checking_in[4], off_duty_checking_in[5],1,1,0)
    # 下班考勤时间戳
    off_duty_checking_inStamp = int(time.mktime(off_duty_checking_in_array))

    #开始记加班时间 
    start_overtime_in = time.strptime("18:30", "%H:%M")
    start_overtime_in_array = (today[0], today[1], today[2], start_overtime_in[3], start_overtime_in[4], start_overtime_in[5],1,1,0)
    # 开始记加班时间戳
    start_overtime_inStamp = int(time.mktime(start_overtime_in_array))

    # 加班餐考勤时间
    overtime_supper = time.strptime("20:30", "%H:%M")
    overtime_supper_array = (today[0], today[1], today[2], overtime_supper[3], overtime_supper[4], overtime_supper[5],1,1,0)
    # 加班餐时间戳
    overtime_supperStamp = int(time.mktime(overtime_supper_array))
    # 加班时长
    overtime_hours = 0
    # 迟到时长
    beLateTime = 0
    # 是否记迟到,1：为记迟到，0：为不记迟到
    isBeLate = 1

    # 周五和周六算加班，不是节假日
    # 正常加班 加班时长 = 下班打卡时间 - 开始记加班时间戳
    if today[6] not in  [5, 6] and today[2] not in [7]:
        # 当天的加班时间
        overtime_hours = off_dutyStamp - start_overtime_inStamp

        # 当天的迟到时间, 迟到时间 = 上班打卡时间 - 上班考勤时间。
        beLateTime = be_on_dutyStamp - be_on_duty_checking_inStamp
        
        # 节假日加班 加班时长 = 下班打卡时间 - 上班打卡时间 - 1小时
    else:
        # 当天的加班时间
        overtime_hours = off_dutyStamp - be_on_dutyStamp - 60 * 60
        # 节假日不算上班迟到。。。
    
    # 加班时长不足一小时不计加班时间
    if overtime_hours < 60*60:
        overtime_hours = 0
    
    # 迟到大于五分钟才计算迟到
    if beLateTime < 60*5:
        beLateTime = 0
        isBeLate = 0
     # 加班餐补，只有当下班卡时间戳大于等于加班餐时间戳才有加班餐
    supper = (off_dutyStamp-overtime_supperStamp)>=0
    # 取分钟
    overtime_hours = overtime_hours/(60*60)
    beLateTime = int(beLateTime/60)
    data_list = []
    data_list.append(overtime_hours)
    data_list.append(supper)
    data_list.append(isBeLate)
    data_list.append(beLateTime)
    # 返回时间
    return data_list

# 单个人每月打卡
def people_clock_in(name, clock_in_list):
    # 当月加班总时长
    totalOverTime = 0
    # 当月总餐补
    totalMeal = 0
    # 迟到总次数
    beLateCount = 0
    # 迟到总时间
    totalBeLateTime = 0
    number_of_days = 0
    # 对单日的信息进行处理
    for element in clock_in_list:
        dayCheckResult = day_clock_in(element)
        if dayCheckResult:
            number_of_days += 1
            if dayCheckResult[0]:
                totalOverTime += dayCheckResult[0]
            if dayCheckResult[1]:
                totalMeal += 1
            if dayCheckResult[2]:
                beLateCount += 1
            if dayCheckResult[3]:
                totalBeLateTime += dayCheckResult[3]
    # 返回值，一个列表0：姓名，1：加班总时长，2：餐补, 3：总出勤天数, 4:迟到次数, 5:迟到总时间
    return [name, totalOverTime, totalMeal, number_of_days, beLateCount, totalBeLateTime]


def openexcel(input_file, output_file):
    headers = ['姓名', '加班时长（分钟）', '加班餐数（次）','总出勤天数（天）', '迟到次数（次）', '迟到总时间（分钟）']
    input_headers = ['姓名','打卡时间']
    output_workbook = Workbook()
    workOvertimeSheet = output_workbook.add_sheet('加班')
    with open_workbook(input_file) as workbook:
        data = []
        data.append(headers)
        clock_in_sheet = workbook.sheet_by_name('每日统计')
        header_list = clock_in_sheet.row_values(2)
        # 第一步取得单个人的打卡时间
        name = ''
        people_clock_in_list = []
        for row_index in range(4, clock_in_sheet.nrows):
            # 姓名
            row_name = clock_in_sheet.cell_value(row_index, 0)
            # 日期
            row_date = clock_in_sheet.cell_value(row_index, 5)
            # 上班打卡时间
            clock_in_time = clock_in_sheet.cell_value(row_index, 7)
            # 下班打卡时间
            clock_out_time = clock_in_sheet.cell_value(row_index, 9)
            # 当天打卡的信息
            info = {'name':row_name, 'date':row_date, 'clock_in_time':clock_in_time,'clock_out_time':clock_out_time}
            # 
            if row_name == name:
                people_clock_in_list.append(info)
            else:
                if name != '' :
                    row_list = people_clock_in(name , people_clock_in_list)
                    data.append(row_list)
                people_clock_in_list = []
                people_clock_in_list.append(row_date)
                name = row_name
        if name != '':
            row_list = people_clock_in(name ,people_clock_in_list)
            data.append(row_list)
        
        # 将数据吸入
        for row_index, row_list in enumerate(data):
            for column_index, element in enumerate(row_list):
                workOvertimeSheet.write(row_index, column_index, element)
        output_workbook.save(output_file)

if __name__ == '__main__':
    input_file = './input/杭州源石云科技有限公司_考勤报表_20190526-20190625.xlsx'
    output_file = './output/杭州源石云科技有限公司_考勤报表_20190526-20190625.xlsx'
    openexcel(input_file, output_file)