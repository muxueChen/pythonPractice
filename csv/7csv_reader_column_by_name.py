# 列标题

import csv
import sys
# 列标题
inputfile = './supplier_data.csv'

outputfile = './output_supplier_data.csv'

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = [ ]

# with open(inputfile, 'r', newline='') as csv_in_file:
#     with open(outputfile, 'r', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filerwriter = csv.writer(csv_out_file)
#         header = next(filereader, None)
#         for index_value in range(len(header)):
#             if header[index_value] in my_columns:
#                 my_columns_index.append(index_value)
        
#         filerwriter.writerow(my_columns)
#         for row_list in filereader:
#             row_list_output = [ ]
#             for index_value in my_columns_index:
#                 row_list_output.append(row_list[index_value])
#             filerwriter.writerow(row_list_output)

import pandas as pd

data_frame = pd.read_csv(inputfile)
data_frame_column_by_name = data_frame.loc[:,my_columns]
data_frame_column_by_name.to_csv(outputfile, index = False)