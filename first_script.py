my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = './outfile_file'
filewriter = open(output_file, 'w')

for index_value in range(len(my_letters)):
    if index_value < (max_index - 1):
        filewriter.write(my_letters[index_value] + '\t')
    else:
        filewriter.write(my_letters[index_value] + '\n')

filewriter.close()

print("Output written to file")

# 写入CSV文件
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
filewriter = open(output_file, 'a')
for index_value in range(max_index):
    if index_value < (max_index - 1):
        filewriter.write(str(my_numbers[index_value]) + ',')
    else:
        filewriter.write(str(my_numbers[index_value]) + '\n')

filewriter.close()
