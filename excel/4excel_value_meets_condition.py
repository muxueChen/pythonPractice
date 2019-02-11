# 筛选特定行
# 行中的值满足某个条件
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook

input_file = './sales_2013.xlsx'
output_file = './output/sales_2013.xlsx'
# 基础python实现方案
# output_workbook = Workbook()

# output_worksheet = output_workbook.add_sheet('jan_2013_output')
# sale_amout_column_index = 3

# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     data = []
#     header = worksheet.row_values(0)
#     data.append(header)

#     for row_index in range(1, worksheet.nrows):
#         row_list = [ ]
#         sale_amout = worksheet.cell_value(row_index, sale_amout_column_index)
#         print('>>>>>>>>>>>>>>>>>>{}'.format(sale_amout))
#         if sale_amout > 1400.0:
#             for column_index in range(worksheet.ncols):
#                 cell_value = worksheet.cell_value(row_index, column_index)
#                 cell_type = worksheet.cell_type(row_index, column_index)
#                 if cell_type == 3:
#                     date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                     date_cell = date(*date_cell[0:3]).strftime('%Y-%m-%d')
#                     row_list.append(date_cell)
#                 else:
#                     row_list.append(cell_value)
#         if row_list:
#             data.append(row_list)
#     for list_index, output_list in enumerate(data):
#         for element_index, element in enumerate(output_list):
#             output_worksheet.write(list_index, element_index, element)

# output_workbook.save(output_file)

# pandas 实现方案
 
import pandas as pd
import sys

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]
writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()