# 选取特定列

# 有些时候，你并不需要工作表中所有的列。在这种情况下，可以使用 Python 选取出你需要保留的列。

# 有两种通用方法可以在 Excel 文件中选取特定的列。下面的小节演示了这两种选取列的方法：

# 使用列索引值

# 使用列标题

# 列索引值

import sys
from datetime import date
from xlrd import open_workbook, xldate_as_datetime
from xlwt import Workbook

input_file = './sales_2013.xlsx'
output_file = './output/sales_2013.xlsx'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
my_columns = [1 ,4]

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [ ]
    for row_index in range(worksheet.nrows):
        row_list = [ ]
        for column_index in my_columns:
            cell_value = worksheet.cell_value(row_index, column_index)
            cell_type = worksheet.cell_type(row_index, column_index)
            if cell_type == 3:
                date_cell = xldate_as_datetime(cell_value, workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m%d%Y')
                row_list.append(date_cell)
            else:
                row_list.append(cell_value)
        data.append(row_list)
    
    for list_index, output_list in enumerate(data):
        for column_index, element in enumerate(output_list):
            output_worksheet.write(list_index, column_index, element)

output_workbook.save(output_file)
