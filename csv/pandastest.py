import sys
import pandas as pd

# 初始化路径
inputfile = './supplier_data.csv'
outputfile = './output_supplier_data.csv'

# 文件内容
data_frame = pd.read_csv(inputfile)
print(data_frame)

data_frame.to_csv(outputfile, index=False)
