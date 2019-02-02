# y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', \
# 'Holly', 'Isabel', 'Jenny']

# for month in y:
#     print("{!s}".format(month))

# print("index value: name in list")
# for i in range(len(z)):
#     print("{0!s}:{1:s}".format(i, z[i]))

# print("access elements in y wity z's index values")

# for j in range(len(z)):
#     if y[j].startswith('J'):
#         print("{!s}".format(y[j]))

# another_dict = {1:'1', 2:'2', 3:'3'}
# for key, value in another_dict.items():
#     print("{0}, {1}".format(key, value))

# 简化for循环：列表、集合与字典生成式
# 列表生成式
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #130 (list comprehension): {}".format(rows_to_keep))

# 集合生成式
my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuples1 = {x for x in my_data}
print("Output #131 (set comprehension): {}".format(set_of_tuples1))
set_of_tuples2 = set(my_data)
print("Output #132 (set function): {}".format(set_of_tuples2))