import csv
import sys

# 读写CSV文件（第2部分）

# 使用python内置CSV模块来处理CSV文件
# 输入路径 
inputfile = './supplier_data.csv'
# 输出路径
outputfile = './output_supplier_data.csv'

# 打开 inputfile 文件 并赋值给 csv_in_file
with open(inputfile, 'r', newline='') as csv_in_file:
    # 打开 outputfile 文件 并赋值给 csv_out_file
    with open(outputfile, 'w', newline='') as csv_out_file:
        # csv 模块中的 reader函数创建了一个文件读取对象，名为 filereader
        filereader = csv.reader(csv_in_file, delimiter=',')
        # csv 模块的writer 函数创建了一个写入对象，名为 filewriter。可以使用这个对象讲数据写入文件。
        # 这些函数中的第二个参数（就是delimiter=''）是默认分割符，所以如果你的输入文件和输出文件都是这个用逗号分割的， 就不需要指定这个参数。
        # 这里指定这个了这个分隔符，是为了防备你的处理的输入文件或要写入的输出文件具有不同的分隔符，例如，分好（;）制表符(\t).
        filewriter = csv.writer(csv_out_file, delimiter=',')
        # 遍历出 filereader 对象中所有行数据，这里每一行都是用‘,’来分割的list
        for  row_list in filereader:
            print(row_list)
            # filewriter对象中的writerow函数来讲每行中的列表写入输出文件中。
            filewriter.writerow(row_list)