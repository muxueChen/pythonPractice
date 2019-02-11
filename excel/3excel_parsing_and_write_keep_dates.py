# 格式化日期数据
# 从 datetime 模块导入 date 函数，
# 以使我们可以将数值转换成日期并对日期进行格式化。
from datetime import date
# 从 xlrd 模块中导入两个函数。在前面的示例中，
# 是使用第一个函数打开的 Excel 工作簿，
# 所以这里将重点介绍第二个函数。
# 函数 xldate_as_tuple 可以将 Excel 中代表日期、时间或日期时间的数值转换为元组。
# 只要将数值转换成了元组，
# 就可以提取出具体时间元素（例如：年、月、日）并将时间元素格式化成不同的时间格式（例如： 1/1/2010 或 January 1, 2010）
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = './sales_2013.xlsx'
output_file = './output/sales_2013.xlsx'

outputwork = Workbook()
outputsheet = outputwork.add_sheet('jan_2013_output')
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            # 创建了一个 if-else 语句来检验单元格类型是否为数字 3。
            # 如果你查看了 xlrd 模块的说明文档（https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html?p=4966#sheet.Cell-class），
            # 就会知道单元格类型为 3 表示这个单元格中包含日期数据
            if worksheet.cell_type(row_index, col_index) == 3:
                # 使用 worksheet 对象的 cell_value 函数和行列索引来引用单元格中的值。
                # 此外，你还可以使用 cell().value 函数，这两个函数可以给出同样的结果。
                # 这个单元格中的值作为 xldate_as_tuple 函数中的第一个参数，
                # 会被转换成元组中的一个代表日期的浮点数
                # 参数 workbook.datemode 是必需的，
                # 它可以使函数确定日期是基于 1900 年还是基于 1904 年，
                # 并据此将数值转换成正确的元组
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
                # 使用元组索引来引用元组 date_cell 中的前 3 个元素（也就是年、月、日）并将它们作为参数传给 date 函数，
                # 这个函数可以将这些值转换成一个 date 对象，date 对象在第 1 章中曾介绍过。然后，strftime 函数将 date 对象转换为一个具有特定格式的字符串。
                # 格式 '%m/%d/%Y' 表示像 2014 年 3 月 15 日这样的日期应该显示为 03/15/2014。
                # 格式化后的日期字符串被重新赋给变量 date_cell。
                date_cell = date(*date_cell[0:3]).strftime('%Y-%m-%d')
                row_list_output.append(date_cell)
                outputsheet.write(row_index, col_index, date_cell)
            else:
                # 使用 worksheet 对象的 cell_value 函数和行列索引引用单元格中的值，
                # 并将其赋给变量 non_date_cell
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                outputsheet.write(row_index, col_index, non_date_cell)

outputwork.save(output_file)