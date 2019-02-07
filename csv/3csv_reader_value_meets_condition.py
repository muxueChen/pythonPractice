import csv
import sys

# 行中的值满足某个条件
# 输入路径 
inputfile = './supplier_data.csv'
# 输出路径
outputfile = './output_supplier_data.csv'

# 基础python
# with open(inputfile, 'r', newline='') as csv_in_file:
#     with open(outputfile, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         # csv 中的next函数读出输入文件的第一行，赋值给名为header的列表变量，
#         header = next(filereader)
#         filewriter.writerow(header)
#         for row_list in filereader:
#             # 取每一行的第一个元素数据，对应的是元数据的供应商
#             supplier = str(row_list[0]).strip()
#             # 取每一行的 第4个元素，对应元数据中的价格，然后使用strip函数从字符串中把美元符号给删除掉
#             cost = str(row_list[3]).strip('$').replace(',', '')
#             if supplier == 'Supplier Z' or float(cost) > 600.0:
#                 filewriter.writerow(row_list)

# pandas 
import pandas as pd

data_frame = pd.read_csv(inputfile)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(outputfile, index=False)