import sys
from datetime import date
import time
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
# 返回当天最早一次打卡，最晚一次打卡的元组， 当周一到周五早上打卡早于九点时，让时间等于九点，下班打卡时间早于下午 7:30不计加班时间
def day_clock_in(name, clock_in_list):
    data_list = []
    # 上班时间
    be_on_duty = min(clock_in_list)
    # 下班时间
    off_duty = max(clock_in_list)

    # 取出日期
    today = time.strptime(be_on_duty, '%Y-%m-%d %H:%M')
    # 判断日期是周末/法定假日/正常上班

    # 转换上班时间
    be_on_duty = time.strptime(be_on_duty, '%Y-%m-%d %H:%M')
    be_on_duty_array = (today[0], today[1], today[2], be_on_duty[3], be_on_duty[4], be_on_duty[5],1,1,0)
    # 上班打卡时间戳
    be_on_dutyStamp = int(time.mktime(be_on_duty_array))

    # 转换下班时间
    off_duty = time.strptime(off_duty, '%Y-%m-%d %H:%M')
    off_duty_array = (today[0], today[1], today[2], off_duty[3], off_duty[4], off_duty[5],1,1,0)
    # 下班打卡时间戳
    off_dutyStamp = int(time.mktime(off_duty_array))

    # 转换成 小时:分钟 的格式，然后进行比较
    # 上班考勤
    be_on_duty_checking_in = time.strptime("09:00", "%H:%M")
    be_on_duty_checking_in_array = (today[0], today[1], today[2], be_on_duty_checking_in[3], be_on_duty_checking_in[4], be_on_duty_checking_in[5],1,1,0)
    # 上班考勤时间戳
    be_on_duty_checking_inStamp = int(time.mktime(be_on_duty_checking_in_array))

    # 下班考勤时间
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
    
    # 计算迟到, 迟到时间 = 上班打卡时间 - 上班考勤时间。
    # 迟到时间大于零记为迟到。当忘记打卡没有补卡的情况下，
    # 节假日不计迟到
    
    # 计算早退，早退时间 = 下班打卡时间 - 下班考勤时间。 
    # 当忘记打下班卡时，读入的下班卡时间会是上班卡时间，此时不计早退时间
    # 节假日不计早退

    # 加班时长 = 下班打卡时间 - 开始记加班时间戳
    # 节假日加班 加班时长 = 下班打卡时间 - 上班打卡时间 - 1小时
    # 加班时长不足一小时不计加班时间
    overtime_hours = 0
    if today[6] not in  [5, 6]:
        overtime_hours = off_dutyStamp - start_overtime_inStamp
    else:
        overtime_hours = off_dutyStamp - be_on_dutyStamp
    
    if overtime_hours < 60*60:
        overtime_hours = 0
    
    # 取分钟
    overtime_hours = int(overtime_hours/60)
    data_list.append(overtime_hours)
    # 加班餐补，只有当下班卡时间戳大于加班餐时间戳才有加班餐
    supper = (off_dutyStamp-overtime_supperStamp)>0
    if supper:
        print("餐补", name, time.strftime("%Y-%m-%d %H:%M:%S", off_duty))
    if overtime_hours>0:
        print("加班时长", name,time.strftime("%Y-%m-%d %H:%M:%S", off_duty),overtime_hours,"分钟")
    data_list.append(supper)
    # 返回时间
    return data_list

# 单个人每月打卡
def people_clock_in(name, clock_in_list):
    day_date_list = []
    # 取出每天的打卡
    date_list = []
    oldDay = ''
    for date_value in clock_in_list:
        # print(date_value)
        # 把date_value转换成具体的某一天
        day = time.strptime(date_value, '%Y-%m-%d %H:%M')
        dayStr = time.strftime('%Y-%m-%d',day)
        if oldDay == dayStr:
            date_list.append(date_value)
        else:
            if oldDay != '':
                overtime = day_clock_in(name, date_list)
                day_date_list.append(overtime)
            date_list = []
            oldDay = dayStr
            date_list.append(date_value)
           
        
    if oldDay != '':
        overtime = day_clock_in(name, date_list)
        day_date_list.append(overtime)

    # 当月加班总时长
    totalOverTime = 0
    # 当月总餐补
    totalMeal = 0
    for element in day_date_list:
        if element[1]:
            totalMeal += 1
        if element[0]:
            totalOverTime += element[0]

    # 返回值，一个列表0：姓名，1：加班总时长，2：餐补
    return [name, totalOverTime, totalMeal]

def openexcel(input_file, output_file):
    headers = ['姓名', '加班时长', '加班餐数']
    input_headers = ['姓名','打卡时间']
    output_workbook = Workbook()
    workOvertimeSheet = output_workbook.add_sheet('加班')
    with open_workbook(input_file) as workbook:
        data = []
        data.append(headers)
        clock_in_sheet = workbook.sheet_by_name('原始记录')
        header_list = clock_in_sheet.row_values(2)

        # 第一步取得单个人的打卡时间
        name = ''
        people_clock_in_list = []
        for row_index in range(3, clock_in_sheet.nrows):
            row_name = clock_in_sheet.cell_value(row_index, 0)
            row_date = clock_in_sheet.cell_value(row_index, 7)
            if row_name == name:
                people_clock_in_list.append(row_date)
            else:
                if name != '' :
                    row_list = people_clock_in(name, people_clock_in_list)
                    
                    data.append(row_list)
                people_clock_in_list = []
                people_clock_in_list.append(row_date)
                name = row_name
        if name != '':
            row_list = people_clock_in(name, people_clock_in_list)
            data.append(row_list)
        
        for row_index, row_list in enumerate(data):
            for column_index, element in enumerate(row_list):
                workOvertimeSheet.write(row_index, column_index, element)
        output_workbook.save(output_file)
if __name__ == '__main__':
    input_file = './2019_1.xlsx'
    output_file = './output/2019_1.xlsx'
    openexcel(input_file, output_file)
