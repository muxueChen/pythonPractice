#文件读写
# 读取文件
# 读取单个文本文件
import os
import os.path

# 遍历文件
# 深层遍历
rootdir = "./"
# for parent, dirnames, filenames in os.walk(rootdir):
#     # for dirname in dirnames:
#     #     print("{}".format(dirname))
#     for filename in filenames:
#         print("{}".format(filename))

# 单层遍历
for filename in os.listdir(rootdir):
    print("{}".format(filename))

fo = open("file_to_read.txt", "w")

# print("文件名:{}".format(fo.name))
# print("是否关闭：{}".format(fo.closed))
# print("访问模式：{}".format(fo.mode))

# 写文件
fo.write('This is a test.\nReally,it is.')
fo.close()

# 读文件
file = open('file_to_read.txt')
# file.read()
print("{}".format(file.read()))
file.close()

# 基于行的读写 line
file1 = open("file_to_read.txt")
print(file1.readline())
print(file1.readline())
file1.close()

file2 = open("file_to_read.txt")
print(file2.read(1))
print(file2.seek(4))
print(file2.read(1))
file2.close()