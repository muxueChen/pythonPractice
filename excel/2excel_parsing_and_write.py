# 读写Excel文件
# 导入 xlrd 模块的 open_workbook 函数，
from xlrd import open_workbook
# 导入 xlwt 模块的 Workbook 对象。
from xlwt import Workbook

input_file = './sales_2013.xlsx'
output_file = './output/sales_2013.xlsx'

# 实例化一个 xlwt Workbook 对象
output_workbook = Workbook()
# 使用 xlwt 的 add_sheet 函数为输出工作簿添加一个工作表 jan_2013_output。
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 使用 xlrd 的 open_workbook 函数打开用于输入的工作簿，并将结果赋给一个 workbook 对象
with open_workbook(input_file) as Workbook:
    # 使用这个 workbook 对象的 sheet_by_name 函数引用名称为 january_2013 的工作表。
    worksheet = Workbook.sheet_by_name('january_2013')
    # 创建了行与列索引值上的 for 循环语句，
    # 使用 range 函数和 worksheet 对象的 nrows 属性和 ncols 属性，
    # 在工作表的每行和每列之间迭代
    for row_index in range(worksheet.nrows):
        for colmun_index in range(worksheet.ncols):
            # 使用 xlwt 的 write 函数和行与列的索引将每个单元格的值写入输出文件的工作表。
            output_worksheet.write(row_index, colmun_index, worksheet.cell_value(row_index, colmun_index))
# 保存并关闭输出工作簿。
output_workbook.save(output_file)
