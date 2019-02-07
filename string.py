
# 下面的两个示例展示了如何使用 split 函数来将一个字符串拆分成一个子字符串列表，
# 列表中的子字符串正好可以构成原字符串。
# （列表是 Python 中的另一种内置数据类型，本章后面将会讨论。）
# split 函数可以在括号中使用两个附加参数。第一个附加参数表示使用哪个字符进行拆分。
# 第二个附加参数表示进行拆分的次数（例如：进行两次拆分，可以得到 3 个子字符串）：
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
.format(string1_list2[0], string1_list2[1], string1_list2[2]))
string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[5],\
string2_list[-1]))