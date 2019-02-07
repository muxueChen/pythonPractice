# 列索引值
import csv
import sys


# 列索引值
inputfile = './supplier_data.csv'

outputfile = './output_supplier_data.csv'

# 基础python实现方案
# my_columns = [0, 3]
# with open(inputfile, 'rb') as csv_in_file:
#     with open(outputfile, 'wb') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         print("{}".format(filereader))
#         for row_list in filereader:
#             row_list_output = [ ]
#             for index_value in my_columns:
#                 row_list_output.append(row_list[index_value])
            
#             filewriter.writerow(row_list_output)

# pandas实现方案
import pandas as pd

data_frame = pd.read_csv(inputfile)
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
data_frame_column_by_index.to_csv(outputfile, index=False)
