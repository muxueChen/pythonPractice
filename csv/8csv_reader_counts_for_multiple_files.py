import csv
import glob
import os
import sys

# 文件计数与文件中的行列计数
inputbase = './'
file_count = 0
for inputfile in glob.glob(os.path.join(inputbase, '*.csv')):
    row_count = 1
    with open(inputfile, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader, None)
        for row in filereader:
            row_count += 1
        
        print('{0!s}: \n{1:d} rows\n{2:d} columns'.format(os.path.basename(inputfile), row_count, len(header)))
    file_count += 1

print('Number of files:{0:d}'.format(file_count))

