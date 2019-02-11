# 筛选特定行
# 行中的值属于某个集合
input_file = './sales_2013.xlsx'
output_file = './output/sales_2013.xlsx'
importtant_datas = ['01/24/2013', '01/31/2013']

# # 基础python实现
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
purchas_data_column_index = 4
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for  row_index in range(1, worksheet.nrows):
        purchse_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchas_data_column_index), workbook.datemode)
        purchase_date = date(*purchse_datetime[0:3]).strftime('%m/%d/%Y')
        row_list = [ ]
        if purchase_date in importtant_datas:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%Y-%m-%d')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)

# pandas实现
# import pandas as pd

# data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
# data_frame_value_in_set = data_frame[data_frame['PurchaseDate'].isin(important_dates)]
# writer = pd.ExcelWriter(output_file)
# data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
# writer.save()