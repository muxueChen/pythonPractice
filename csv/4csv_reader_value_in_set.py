import csv
import sys

# 行中的值属于某个集合

# 输入路径 
inputfile = './supplier_data.csv'
# 输出路径
outputfile = './output_supplier_data.csv'

important_datas = ['1/20/14', '1/30/14']

# 基础python实现
# with open(inputfile, 'r', newline='') as csv_in_file:
#     with open(outputfile, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         # 取文件第一行
#         header = next(filereader)
#         # 把输入文件的第一行写入输出文件中
#         filewriter.writerow(header)

#         for row_list in filereader:
#             # 取出行中的第五个元素，对应输入文件中的日期
#             a_data = row_list[4]
#             # 判断日期是否包含在 important_datas 列表中
#             if a_data in important_datas:
#                 # 如果日期包含在 important_datas 列表中 则写入这行数据
#                 filewriter.writerow(row_list)

# pandas 实现
import pandas as pd

data_frame = pd.read_csv(inputfile)
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_datas), :]
data_frame_value_in_set.to_csv(outputfile, index=False)
