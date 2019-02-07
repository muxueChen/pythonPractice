import csv
import glob
import os
import sys

# 列索引值
input_base = './supplier_data.csv'

outputfile = './output_supplier_data.csv'

output_header_list = ['file_name', 'total_sales', 'average_sale']

csv_out_file = open(outputfile, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)
for inputfile in glob.glob(os.path.join(input_base, '*.csv')):
    with open(inputfile, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = [ ]
        output_list.append(os.path.basename(inputfile))
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            total_sales += float(str(sale_amount).strip('$').replace(',',''))
            number_of_sales += 1
        # 平均值
        average_sales = '{0:.2f}'.format(total_sales/number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
# 关闭文件
csv_out_file.close()

