import numpy as np
my_array = np.array([1,2,3,4,5])
print(my_array)

print(my_array.shape)

# 我们也可以打印各个元素。就像普通的Python数组一样，NumPy数组的起始索引编号为0。
print(my_array[0])
print(my_array[1])

# 我们还可以修改NumPy数组的元素。例如，假设我们编写以下2个命令
my_array[0] = -1
print(my_array)

# 现在假设，我们要创建一个长度为5的NumPy数组，但所有元素都为0，我们可以这样做吗？是的。NumPy提供了一种简单的方法来做同样的事情。
my_new_array = np.zeros((5))
print(my_new_array)

# 如果我们想创建一个随机值数组怎么办？我们使用的是随机函数，它为每个元素分配0到1之间的随机值。
my_random_array = np.random.random(5)
print(my_random_array)

# 现在让我们看看如何使用NumPy创建二维数组。
my_2d_array = np.zeros((2, 3))
print(my_2d_array)

# 猜猜以下代码的输出结果如何
my_2d_array_new = np.ones((2, 4)) 
print(my_2d_array_new)