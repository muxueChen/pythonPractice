import csv
import sys
import re

# 行中的值匹配于某个模式/正则表达式

# 输入路径 
inputfile = './supplier_data.csv'
# 输出路径
outputfile = './output_supplier_data.csv'

# 基础python实现方案
# pattern = re.compile(r'^001-.*', re.I)

# with open(inputfile, 'r', newline='') as csv_in_file:
#     with open(outputfile, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         header = next(filereader)
#         filewriter.writerow(header)
#         for row_list  in filereader:
#             invoice_number = row_list[1]
#             if pattern.search(invoice_number):
#                 filewriter.writerow(row_list)

# pandas 实现方案
import pandas as pd

data_frame = pd.read_csv(inputfile)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), :]

data_frame_value_matches_pattern.to_csv(outputfile, index=False)