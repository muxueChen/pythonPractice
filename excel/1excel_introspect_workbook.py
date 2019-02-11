# 内省Excel工作簿

import sys
from xlrd import open_workbook

inputfile = './sales_2013.xlsx'
workbook = open_workbook(inputfile)
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRows:",\
         worksheet.nrows, "\tColumns:", worksheet.ncols)