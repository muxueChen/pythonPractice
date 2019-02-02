y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', \
'Holly', 'Isabel', 'Jenny']

for month in y:
    print("{!s}".format(month))

print("index value: name in list")
for i in range(len(z)):
    print("{0!s}:{1:s}".format(i, z[i]))

print("access elements in y wity z's index values")

for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}".format(y[j]))

another_dict = {1:'1', 2:'2', 3:'3'}
for key, value in another_dict.items():
    print("{0}, {1}".format(key, value))