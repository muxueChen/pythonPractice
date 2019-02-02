

# 计算一些列数值的均值

def getmean(numericValues):
    if len(numericValues) >0 :
        return sum(numericValues)/len(numericValues)
    else :
        float('nan')

my_list = [2, 2, 4, 4, 6, 6, 8, 8]
print("mean:{!s}".format(getmean(my_list)))