import csv
import sys

# 选取连续的行

# 列标题
inputfile = './supplier_data.csv'

outputfile = './supplier_data_unnecessary_header_footer.csv'
rowcount = 0
with open(inputfile, 'r', newline='') as csv_in_file:
    with open(outputfile, 'w', newline='')as csv_out_file:
        filerader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)

        for row in filerader:
            
            if rowcount > 3  and rowcount <= 15:
                print('content>>>>>>>>>>>>>{}'.format(row))
                content = [value.strip() for value in row]
                print('value---------------{}'.format(content))
                filewriter.writerow(content)

            rowcount += 1
